import csv
import sys
import uuid
from datetime import datetime as dt
from pathlib import Path
from urllib.parse import urljoin

import sqlalchemy.exc as exc
from flask import Blueprint, Response, jsonify, request, send_file, g
from flask.helpers import send_file
from geojson import FeatureCollection
from geonature.core.gn_commons.models import TMedias

# import des fonctions utiles depuis le sous-module d'authentification
from geonature.core.gn_permissions import decorators as permissions
from geonature.core.gn_permissions.tools import get_scopes_by_action
from ref_geo.models import BibAreasTypes, LAreas, LiMunicipalities
from geonature.utils.config import config
from geonature.utils.env import DB, ROOT_DIR
from geonature.utils.utilssqlalchemy import json_resp
from pypnnomenclature.models import TNomenclatures
from pypnusershub.db.models import Organisme, User
from sqlalchemy import desc, func, text
from sqlalchemy.orm import aliased
from utils_flask_sqla.generic import GenericQuery
from utils_flask_sqla.response import json_resp_accept_empty_list

from .api_error import ZHApiError
from .forms import (
    create_zh,
    post_file_info,
    update_actions,
    update_activities,
    update_corine_biotopes,
    update_corine_landcover,
    update_delim,
    update_fct_delim,
    update_functions,
    update_hab_heritages,
    update_inflow,
    update_instruments,
    update_managements,
    update_outflow,
    update_ownerships,
    update_protections,
    update_refs,
    update_tzh,
    update_urban_docs,
    update_zh_tab0,
    update_zh_tab6,
)

# from .forms import *
from .geometry import set_area, set_geom
from .hierarchy import Hierarchy, get_all_hierarchy_fields
from .model.cards import Card
from .model.repositories import ZhRepository
from .model.zh import ZH
from .model.zh_schema import (
    TZH,
    BibActions,
    BibOrganismes,
    BibSiteSpace,
    CorLimList,
    CorZhArea,
    CorZhRef,
    THydroArea,
    TReferences,
    TRiverBasin,
)
from .nomenclatures import get_ch, get_nomenc
from .pdf import gen_pdf
from .search import main_search
from .upload import upload_process
from .utils import (
    check_ref_geo_schema,
    delete_file,
    get_file_path,
    get_last_pdf_export,
    get_main_picture_id,
    get_user_cruved,
)

blueprint = Blueprint("pr_zh", __name__, "../static", template_folder="templates")


# Route pour afficher liste des zones humides
@blueprint.route("", methods=["GET", "POST"])
@permissions.check_cruved_scope("R", get_scope=True, module_code="ZONES_HUMIDES")
@json_resp
def get_zh(info_role):
    try:
        coauthor = aliased(User, name="coauthor")
        coorganism = aliased(Organisme, name="coorganism")
        q = (
            DB.session.query(TZH)
            .join(TNomenclatures, TZH.sdage)
            .join(User, TZH.authors)
            .join(coauthor, TZH.coauthors)
            .join(Organisme, User.organisme)
            .join(coorganism, coauthor.organisme)
        )

        parameters = request.args
        limit = int(parameters.get("limit", 100))
        page = int(parameters.get("offset", 0))
        orderby = str(parameters.get("orderby", "update_date"))
        order = str(parameters.get("order", "desc"))

        payload = request.json or None

        if payload is not None:
            q = main_search(q, payload)

        return get_all_zh(
            info_role=info_role,
            query=q,
            limit=limit,
            page=page,
            orderby=orderby,
            order=order,
        )
    except Exception as e:
        exc_type, value, tb = sys.exc_info()
        raise ZHApiError(
            message="filter_zh_error",
            details=str(exc_type) + ": " + str(e.with_traceback(tb)),
        )


def get_all_zh(info_role, query, limit, page, orderby=None, order="asc"):
    try:
        # Pour obtenir le nombre de résultat de la requete sans le LIMIT
        nb_results_without_limit = query.count()
        user = info_role
        user_cruved = get_user_cruved()

        if orderby in TZH.__table__.columns:
            col = getattr(TZH, orderby, None)
            if col is not None:
                if order == "desc":
                    col = col.desc()
                query = query.order_by(col)

        if orderby in [
            "sdage",
            "author",
            "update_author",
            "organism",
            "update_organism",
        ]:
            if orderby == "sdage":
                desc_query = TNomenclatures.label_default
            elif orderby == "author":
                desc_query = User.nom_role
            elif orderby == "update_author":
                desc_query = text("coauthor.nom_role")
            elif orderby == "organism":
                desc_query = Organisme.nom_organisme
            elif orderby == "update_organism":
                desc_query = text("coorganism.nom_organisme")
            if order == "desc":
                desc_query = desc(desc_query)
            query = query.order_by(desc_query)

        # Order by id because there can be ambiguity in order_by(col) depending
        # on the column so add on order_by id makes it clearer
        data = query.order_by(TZH.id_zh).limit(limit).offset(page * limit).all()

        is_ref_geo = check_ref_geo_schema()

        featureCollection = []
        for n in data:
            releve_cruved = n.get_releve_cruved(user, user_cruved)
            feature = n.get_geofeature(relationships=())
            feature["properties"]["rights"] = releve_cruved
            featureCollection.append(feature)

        return {
            "total": nb_results_without_limit,
            "total_filtered": len(data),
            "page": page,
            "limit": limit,
            "items": FeatureCollection(featureCollection),
            "check_ref_geo": is_ref_geo,
        }, 200
    except Exception as e:
        if e.__class__.__name__ == "ZHApiError":
            raise ZHApiError(message=str(e.message), details=str(e.details))
        exc_type, value, tb = sys.exc_info()
        raise ZHApiError(
            message="get_zh_list_error",
            details=str(exc_type) + ": " + str(e.with_traceback(tb)),
        )
    finally:
        DB.session.close()


# Route pour afficher liste des zones humides
@blueprint.route("/check_ref_geo", methods=["GET"])
@permissions.check_cruved_scope("R", module_code="ZONES_HUMIDES")
@json_resp
def check_ref_geo():
    try:
        # check if municipalities and dep in ref_geo
        return {"check_ref_geo": check_ref_geo_schema()}, 200
    except Exception as e:
        if e.__class__.__name__ == "ZHApiError":
            raise ZHApiError(message=str(e.message), details=str(e.details))
        exc_type, value, tb = sys.exc_info()
        raise ZHApiError(
            message="check_ref_geo_route_error",
            details=str(exc_type) + ": " + str(e.with_traceback(tb)),
        )
    finally:
        DB.session.close()


@blueprint.route("/<int:id_zh>", methods=["GET"])
@permissions.check_cruved_scope("R", module_code="ZONES_HUMIDES")
@json_resp
def get_zh_by_id(id_zh):
    """Get zh form data by id"""
    try:
        zh = ZH(id_zh)
        user_cruved = get_user_cruved()
        if zh.zh.user_is_allowed_to(g.current_user, user_cruved["R"]):
            return zh.__repr__()

        raise ZHApiError(
            message="user_not_allowed", details="You are not allowed to see this zh"
        )
    except Exception as e:
        exc_type, value, tb = sys.exc_info()
        if e.__class__.__name__ == "NoResultFound":
            raise ZHApiError(
                message="is_zh_id_exists",
                details=str(exc_type) + ": " + str(e.with_traceback(tb)),
            )
        if e.__class__.__name__ == "DataError":
            raise ZHApiError(
                message="get_zh_by_id_db_error",
                details=str(e.orig.diag.sqlstate + ": " + e.orig.diag.message_primary),
                status_code=400,
            )
        if e.__class__.__name__ == "ZHApiError":
            raise ZHApiError(message=str(e.message), details=str(e.details))
        raise ZHApiError(
            message="get_zh_by_id_error",
            details=str(exc_type) + ": " + str(e.with_traceback(tb)),
        )
    finally:
        DB.session.close()


@blueprint.route("/<int:id_zh>/complete_card", methods=["GET"])
@permissions.check_cruved_scope("R", module_code="ZONES_HUMIDES")
@json_resp
def get_complete_info(id_zh):
    """Get zh complete info"""
    try:
        zh = ZH(id_zh)
        user_cruved = get_user_cruved()
        if zh.zh.user_is_allowed_to(g.ucrrent_user, user_cruved["R"]):
            # get other referentials needed for the module from the config file
            return get_complete_card(id_zh)
        raise ZHApiError(
            message="user_not_allowed", details="You are not allowed to see this zh"
        )
    except Exception as e:
        exc_type, value, tb = sys.exc_info()
        if e.__class__.__name__ == "NoResultFound":
            raise ZHApiError(
                message="is_zh_id_exists",
                details=str(exc_type) + ": " + str(e.with_traceback(tb)),
            )
        if e.__class__.__name__ == "DataError":
            raise ZHApiError(
                message="get_complete_info_db_error",
                details=str(e.orig.diag.sqlstate + ": " + e.orig.diag.message_primary),
                status_code=400,
            )
        if e.__class__.__name__ == "ZHApiError":
            raise ZHApiError(message=str(e.message), details=str(e.details))
        raise ZHApiError(
            message="get_complete_info_error",
            details=str(exc_type) + ": " + str(e.with_traceback(tb)),
        )
    finally:
        DB.session.close()


def get_complete_card(id_zh: int) -> Card:
    ref_geo_config = [
        ref for ref in blueprint.config["ref_geo_referentiels"] if ref["active"]
    ]
    return Card(id_zh, "full", ref_geo_config).__repr__()


@blueprint.route("/eval/<int:id_zh>", methods=["GET"])
@permissions.check_cruved_scope("R", module_code="ZONES_HUMIDES")
@json_resp
def get_zh_eval(id_zh):
    """Get zh form data by id"""
    try:
        zh_eval = ZH(id_zh).get_eval()
        return zh_eval
    except Exception as e:
        exc_type, value, tb = sys.exc_info()
        if e.__class__.__name__ == "NoResultFound":
            raise ZHApiError(
                message="is_zh_id_exists",
                details=str(exc_type) + ": " + str(e.with_traceback(tb)),
            )
        if e.__class__.__name__ == "ZHApiError":
            raise ZHApiError(message=str(e.message), details=str(e.details))
        raise ZHApiError(
            message="get_zh_eval_error",
            details=str(exc_type) + ": " + str(e.with_traceback(tb)),
        )
    finally:
        DB.session.close()


@blueprint.route("/municipalities/<int:id_zh>", methods=["GET"])
@permissions.check_cruved_scope("R", module_code="ZONES_HUMIDES")
@json_resp
def get_municipalities(id_zh):
    """Get municipalities list"""
    try:
        if not CorZhArea.get_municipalities_info(id_zh):
            raise ZHApiError(
                message="no_municipality_error",
                details="Empty list of municipality returned from get_municipalities_info db request",
            )
        return [
            {
                "municipality_name": municipality.LiMunicipalities.nom_com,
                "id_area": municipality.CorZhArea.id_area,
            }
            for municipality in CorZhArea.get_municipalities_info(id_zh)
        ]
    except Exception as e:
        exc_type, value, tb = sys.exc_info()
        if e.__class__.__name__ == "NoResultFound":
            raise ZHApiError(
                message="is_zh_id_exists",
                details=str(exc_type) + ": " + str(e.with_traceback(tb)),
            )
        if e.__class__.__name__ == "ZHApiError":
            raise ZHApiError(message=str(e.message), details=str(e.details))
        raise ZHApiError(
            message="get_municipalities_error",
            details=str(exc_type) + ": " + str(e.with_traceback(tb)),
        )
    finally:
        DB.session.close()


@blueprint.route("/forms", methods=["GET"])
@permissions.check_cruved_scope("R", module_code="ZONES_HUMIDES")
@json_resp
def get_tab():
    """Get form metadata for all tabs"""
    try:
        metadata = get_nomenc(blueprint.config["nomenclatures"])
        metadata["BIB_ORGANISMES"] = BibOrganismes.get_bib_organisms("operator")
        metadata["BIB_SITE_SPACE"] = BibSiteSpace.get_bib_site_spaces()
        metadata["BIB_MANAGEMENT_STRUCTURES"] = BibOrganismes.get_bib_organisms(
            "management_structure"
        )
        metadata["BIB_ACTIONS"] = BibActions.get_bib_actions()
        return metadata
    except Exception as e:
        exc_type, value, tb = sys.exc_info()
        if e.__class__.__name__ == "ZHApiError":
            raise ZHApiError(message=str(e.message), details=str(e.details))
        raise ZHApiError(
            message="get_tab_data_error",
            details=str(exc_type) + ": " + str(e.with_traceback(tb)),
        )
    finally:
        DB.session.close()


@blueprint.route("/forms/cahierhab/<string:lb_code>", methods=["GET"])
@permissions.check_cruved_scope("R", module_code="ZONES_HUMIDES")
@json_resp
def get_cahier_hab(lb_code):
    """Get cahier hab list from corine biotope lb_code"""
    try:
        return get_ch(lb_code)
    except Exception as e:
        if e.__class__.__name__ == "ZHApiError":
            raise ZHApiError(message=str(e.message), details=str(e.details))
        exc_type, value, tb = sys.exc_info()
        raise ZHApiError(
            message="get_cahier_hab_route_error",
            details=str(exc_type) + ": " + str(e.with_traceback(tb)),
        )
    finally:
        DB.session.close()


@blueprint.route("/pbf", methods=["GET"])
def get_pbf():
    sql = """
    SELECT ST_AsGeobuf(q, 'geom') as pbf
    FROM (SELECT id_zh, geom from pr_zh.t_zh tz) AS q;
    """
    query = DB.session.execute(sql)
    row = query.first()
    if row["pbf"]:
        return Response(bytes(row["pbf"]), mimetype="application/protobuf")
    return jsonify(None)


@blueprint.route("/pbf/complete", methods=["GET"])
def get_pbf_complete():
    sql = """
    SELECT St_asgeobuf(q, 'polygon_4326') AS pbf
    FROM   (SELECT tz.id,
               tz.nom,
               tz.slug,
               tz.code,
               tz.date,
               tz.polygon_4326,
               tz.superficie,
               tz.operateur,
               tz.type_code,
               tz.type,
               tz.menaces,
               tz.diagnostic_bio,
               tz.diagnostic_hydro,
               Json_build_object('criteres_delim', tz.criteres_delim,
                         'communes',
                         tz.communes,
                         'bassin_versant', tz.bassin_versant) as json_arrays
        FROM   pr_zh.atlas_app tz) AS q;
    """
    query = DB.session.execute(sql)
    row = query.first()
    if row["pbf"]:
        return Response(bytes(row["pbf"]), mimetype="application/protobuf")


@blueprint.route("/geojson", methods=["GET"])
def get_json():
    sql = """
    SELECT jsonb_build_object(
    'type',     'FeatureCollection',
    'features', json_agg(features.feature)
    )::json as geojson
    FROM (
    SELECT jsonb_build_object(
        'type',       'Feature',
        'id',         inputs.id,
        'geometry',   ST_AsGeoJSON(inputs.polygon_4326)::jsonb,
        'properties', to_jsonb(inputs) - 'polygon_4326'
    ) AS feature
    FROM (SELECT * FROM pr_zh.atlas_app tz) inputs) features;
    """
    query = DB.session.execute(sql)
    row = query.first()
    return row["geojson"]


@blueprint.route("/geometries", methods=["GET"])
@permissions.check_cruved_scope("R", module_code="ZONES_HUMIDES")
@json_resp
def get_geometries():
    """Get list of all zh geometries (contours)"""
    try:
        if not DB.session.query(TZH).all():
            raise ZHApiError(
                message="no_geometry",
                details="Empty list of zh returned from get_zh_list db request",
            )
        return [
            {
                "geometry": zh.get_geofeature()["geometry"],
                "id_zh": zh.get_geofeature()["properties"]["id_zh"],
            }
            for zh in DB.session.query(TZH).all()
        ]
    except Exception as e:
        if e.__class__.__name__ == "ZHApiError":
            raise ZHApiError(message=str(e.message), details=str(e.details))
        exc_type, value, tb = sys.exc_info()
        raise ZHApiError(
            message="get_geometries_error",
            details=str(exc_type) + ": " + str(e.with_traceback(tb)),
        )
    finally:
        DB.session.close()


@blueprint.route("/references/autocomplete", methods=["GET"])
@permissions.check_cruved_scope("R", module_code="ZONES_HUMIDES")
@json_resp
def get_ref_autocomplete():
    try:
        params = request.args
        search_title = params.get("search_title")
        # search_title = 'MCD'
        q = DB.session.query(
            TReferences,
            func.similarity(TReferences.title, search_title).label("idx_trgm"),
        )

        search_title = search_title.replace(" ", "%")
        q = q.filter(TReferences.title.ilike("%" + search_title + "%")).order_by(
            desc("idx_trgm")
        )

        limit = request.args.get("limit", 20)
        print(q)

        data = q.limit(limit).all()
        if data:
            return [d[0].as_dict() for d in data]
        else:
            return "No Result", 404
    except Exception as e:
        if e.__class__.__name__ == "ZHApiError":
            raise ZHApiError(message=str(e.message), details=str(e.details))
        exc_type, value, tb = sys.exc_info()
        raise ZHApiError(
            message="get_ref_autocomplete_error",
            details=str(exc_type) + ": " + str(e.with_traceback(tb)),
        )
    finally:
        DB.session.close()


@blueprint.route("/<int:id_zh>/files", methods=["GET"])
@permissions.check_cruved_scope("R", module_code="ZONES_HUMIDES")
@json_resp_accept_empty_list
def get_file_list(id_zh):
    """get a list of the zh files contained in static repo"""
    try:
        # FIXME: to optimize... See relationships and lazy join with sqlalchemy
        zh_uuid = DB.session.query(TZH).filter(TZH.id_zh == id_zh).one().zh_uuid
        q_medias = (
            DB.session.query(TMedias, TNomenclatures.label_default)
            .filter(TMedias.unique_id_media == zh_uuid)
            .join(
                TNomenclatures,
                TNomenclatures.id_nomenclature == TMedias.id_nomenclature_media_type,
            )
            .order_by(TMedias.meta_update_date.desc())
            .all()
        )
        res_media, image_medias = [], []
        for media, media_type in q_medias:
            res_media.append(media)
            if media_type == "Photo":
                image_medias.append(media)
        return {
            "media_data": [media.as_dict() for media in res_media],
            "main_pict_id": get_main_picture_id(id_zh, media_list=image_medias),
        }
    except Exception as e:
        exc_type, value, tb = sys.exc_info()
        raise ZHApiError(
            message="get_file_list_error",
            details=str(exc_type) + ": " + str(e.with_traceback(tb)),
        )
    finally:
        DB.session.close()


@blueprint.route("files/<int:id_media>", methods=["DELETE"])
@permissions.check_cruved_scope("C", module_code="ZONES_HUMIDES")
def delete_one_file(id_media):
    """delete file by id_media in TMedias and static directory"""
    try:
        delete_file(id_media)
        return ("", 204)
    except Exception as e:
        DB.session.rollback()
        if e.__class__.__name__ == "ZHApiError":
            raise ZHApiError(message=str(e.message), details=str(e.details))
        raise ZHApiError(message="delete_one_file_error", details=str(e))
    finally:
        DB.session.close()


@blueprint.route("files/<int:id_media>", methods=["GET"])
@permissions.check_cruved_scope("C", module_code="ZONES_HUMIDES")
def download_file(id_media):
    """download file by id_media in static directory"""
    try:
        return send_file(get_file_path(id_media), as_attachment=True)
    except Exception as e:
        if e.__class__.__name__ == "ZHApiError":
            raise ZHApiError(message=str(e.message), details=str(e.details))
        raise ZHApiError(message="download_file_error", details=str(e))
    finally:
        DB.session.close()


@blueprint.route("<int:id_zh>/main_pict/<int:id_media>", methods=["PATCH"])
@permissions.check_cruved_scope("C", module_code="ZONES_HUMIDES")
def post_main_pict(id_zh, id_media):
    """post main picture id in tzh"""
    try:
        # FIXME: after insert+after update on t_zh => update_date=dt.now()
        DB.session.query(TZH).filter(TZH.id_zh == id_zh).update(
            {TZH.main_pict_id: id_media, TZH.update_date: dt.now()}
        )
        DB.session.commit()
        return ("", 204)
    except Exception as e:
        DB.session.rollback()
        if e.__class__.__name__ == "DataError":
            raise ZHApiError(
                message="post_main_pict_db_error",
                details=str(e.orig.diag.sqlstate + ": " + e.orig.diag.message_primary),
                status_code=400,
            )
        exc_type, value, tb = sys.exc_info()
        raise ZHApiError(
            message="post_main_pict_error",
            details=str(exc_type) + ": " + str(e.with_traceback(tb)),
        )
    finally:
        DB.session.close()


@blueprint.route("<int:id_zh>/photos", methods=["GET"])
@json_resp
def get_all_photos(id_zh: int):
    q_medias = (
        DB.session.query(TZH.main_pict_id, TMedias.id_media, TMedias.media_path)
        .join(TZH, TZH.zh_uuid == TMedias.unique_id_media)
        .join(
            TNomenclatures,
            TNomenclatures.id_nomenclature == TMedias.id_nomenclature_media_type,
        )
        .order_by(TMedias.meta_update_date.desc())
        .filter(TNomenclatures.label_default == "Photo")
        .filter(TZH.id_zh == id_zh)
        .all()
    )
    api_uri = urljoin(
        f"{config['API_ENDPOINT']}/",
        f"{blueprint.config['MODULE_CODE'].lower()}/{blueprint.config['file_path']}/",
    )
    return [
        {"url": urljoin(api_uri, Path(media[-1]).name)}
        for media in sorted(q_medias, key=lambda x: x[0] != x[1])
    ]


from shapely.geometry import asShape
from geoalchemy2.shape import from_shape, to_shape


@blueprint.route("/form/<int:id_tab>", methods=["POST", "PATCH"])
@permissions.check_cruved_scope("C", module_code="ZONES_HUMIDES")
@json_resp
def get_tab_data(id_tab):
    """Post zh data"""
    form_data = request.json or {}
    form_data["update_author"] = g.current_user.id_role
    form_data["update_date"] = dt.now()
    print("OHHH", form_data["geom"])
    shape = asShape(form_data["geom"]["geometry"])
    geom_4326 = from_shape(shape, srid=4326)

    # try:
    if id_tab == 0:
        # set name
        if form_data["main_name"] == "":
            raise ZHApiError(
                message="empty_field_error",
                details="empty main name field",
                status_code=400,
            )

        # select active geo refs in config
        active_geo_refs = [
            ref for ref in blueprint.config["ref_geo_referentiels"] if ref["active"]
        ]
        intersection = None
        # Check on geometry that should always exist (PATCH or POST)
        if len(form_data["geom"]["geometry"]["coordinates"]) == 0:
            raise ZHApiError(
                message="empty_geometry",
                details="You must provide a geometry when creating a zh",
            )
        # POST / PATCH
        if "id_zh" not in form_data.keys():
            # set geometry from coordinates
            # geom = set_geom(form_data["geom"]["geometry"])
            # geom area
            # area = set_area(geom)
            # create_zh
            zh = create_zh(
                form_data,
                g.current_user,
                form_data["update_date"],
                geom_4326,
                1200,
                active_geo_refs,
            )
            # FIXME
            intersection = True
            # intersection = geom["is_intersected"]
        else:
            # edit geometry
            geom = set_geom(form_data["geom"]["geometry"], form_data["id_zh"])
            # geom area
            area = set_area(geom)
            # edit zh
            zh = update_zh_tab0(
                form_data,
                geom["polygon"],
                area,
                g.current_user,
                form_data["update_date"],
                active_geo_refs,
            )
            intersection = geom["is_intersected"]

        DB.session.commit()
        print("LAAAA???????????", intersection)
        return jsonify({"id_zh": zh, "is_intersected": intersection})

    if id_tab == 1:
        update_tzh(form_data)
        update_refs(form_data)
        DB.session.commit()
        return {"id_zh": form_data["id_zh"]}, 200

    if id_tab == 2:
        update_tzh(form_data)
        update_delim(form_data["id_zh"], form_data["critere_delim"])
        update_fct_delim(form_data["id_zh"], form_data["critere_delim_fs"])
        DB.session.commit()
        return {"id_zh": form_data["id_zh"]}, 200

    if id_tab == 3:
        update_tzh(form_data)
        update_corine_biotopes(form_data["id_zh"], form_data["corine_biotopes"])
        update_corine_landcover(form_data["id_zh"], form_data["id_corine_landcovers"])
        update_activities(
            form_data["id_zh"], form_data["activities"]
        )  # , form_data['id_cor_impact_types'])
        DB.session.commit()
        return {"id_zh": form_data["id_zh"]}, 200

    if id_tab == 4:
        update_outflow(form_data["id_zh"], form_data["outflows"])
        update_inflow(form_data["id_zh"], form_data["inflows"])
        update_tzh(form_data)
        DB.session.commit()
        return {"id_zh": form_data["id_zh"]}, 200

    if id_tab == 5:
        update_functions(
            form_data["id_zh"], form_data["fonctions_hydro"], "FONCTIONS_HYDRO"
        )
        update_functions(
            form_data["id_zh"], form_data["fonctions_bio"], "FONCTIONS_BIO"
        )

        update_functions(
            form_data["id_zh"], form_data["interet_patrim"], "INTERET_PATRIM"
        )

        update_functions(form_data["id_zh"], form_data["val_soc_eco"], "VAL_SOC_ECO")
        update_tzh(form_data)
        update_hab_heritages(form_data["id_zh"], form_data["hab_heritages"])
        DB.session.commit()
        return {"id_zh": form_data["id_zh"]}, 200

    if id_tab == 6:
        update_ownerships(form_data["id_zh"], form_data["ownerships"])
        update_managements(form_data["id_zh"], form_data["managements"])
        update_instruments(form_data["id_zh"], form_data["instruments"])
        update_protections(form_data["id_zh"], form_data["protections"])
        update_zh_tab6(form_data)
        update_urban_docs(form_data["id_zh"], form_data["urban_docs"])
        DB.session.commit()
        return {"id_zh": form_data["id_zh"]}, 200

    if id_tab == 7:
        update_tzh(form_data)
        update_actions(form_data["id_zh"], form_data["actions"])
        DB.session.commit()
        return {"id_zh": form_data["id_zh"]}, 200

    if id_tab == 8:
        # try:
        # FIXME: temp fix
        form_data["id_zh"] = request.form.to_dict()["id_zh"]
        update_tzh(form_data)
        ALLOWED_EXTENSIONS = blueprint.config["allowed_extensions"]
        MAX_PDF_SIZE = blueprint.config["max_pdf_size"]
        MAX_JPG_SIZE = blueprint.config["max_jpg_size"]
        FILE_PATH = blueprint.config["file_path"]
        MODULE_NAME = blueprint.config["MODULE_CODE"].lower()

        upload_resp = upload_process(
            request,
            ALLOWED_EXTENSIONS,
            MAX_PDF_SIZE,
            MAX_JPG_SIZE,
            FILE_PATH,
            MODULE_NAME,
        )

        DB.session.commit()

        return jsonify(
            {
                "media_path": upload_resp["media_path"],
                "secured_file_name": upload_resp["secured_file_name"],
                "id_media": upload_resp["id_media"],
            }
        )
        # except Exception as e:
        #     exc_type, value, tb = sys.exc_info()
        #     raise ZHApiError(
        #         message="upload_file_post_error",
        #         details=str(exc_type) + ": " + str(e.with_traceback(tb)),
        #     )

    # except KeyError or TypeError as e:
    #     raise ZHApiError(
    #         message="likely_empty_mandatory_field_error", details=str(e), status_code=400
    #     )
    # except exc.IntegrityError as e:
    #     raise ZHApiError(message="ZH_main_name_already_exists", details=str(e), status_code=400)
    # except exc.DataError as e:
    #     raise ZHApiError(
    #         message="post_tab_form_db_error",
    #         details=str(e.orig.diag.sqlstate + ": " + e.orig.diag.message_primary),
    #         status_code=400,
    #     )
    # except ZHApiError as e:
    #     raise ZHApiError(message=str(e.message), details=str(e.details))
    # except Exception as e:
    #     exc_type, value, tb = sys.exc_info()
    #     raise ZHApiError(
    #         message="post_tab_form_error", details=str(exc_type) + ": " + str(e.with_traceback(tb))
    #     )
    # finally:
    #     DB.session.rollback()
    #     DB.session.close()


@blueprint.route("files/<int:id_media>", methods=["PATCH"])
@permissions.check_cruved_scope("C", module_code="ZONES_HUMIDES")
@json_resp
def patch_file(id_media):
    """edit file upload from tab8"""
    try:
        ALLOWED_EXTENSIONS = blueprint.config["allowed_extensions"]
        MAX_PDF_SIZE = blueprint.config["max_pdf_size"]
        MAX_JPG_SIZE = blueprint.config["max_jpg_size"]
        FILE_PATH = blueprint.config["file_path"]
        MODULE_NAME = blueprint.config["MODULE_CODE"].lower()

        upload_resp = upload_process(
            request,
            ALLOWED_EXTENSIONS,
            MAX_PDF_SIZE,
            MAX_JPG_SIZE,
            FILE_PATH,
            MODULE_NAME,
            id_media=id_media,
        )

        DB.session.commit()

        return {
            "media_path": upload_resp["media_path"],
            "secured_file_name": upload_resp["secured_file_name"],
            "id_media": upload_resp["id_media"],
        }, 200
    except ZHApiError as e:
        raise ZHApiError(message=str(e.message), details=str(e.details))
    except Exception as e:
        exc_type, value, tb = sys.exc_info()
        raise ZHApiError(
            message="upload_file_patch_error",
            details=str(exc_type) + ": " + str(e.with_traceback(tb)),
        )


@blueprint.route("/<int:id_zh>", methods=["DELETE"])
@permissions.check_cruved_scope("D", module_code="ZONES_HUMIDES")
@json_resp
def deleteOneZh(id_zh):
    """Delete one zh

    :params int id_zh: ID of th*e zh to delete

    """
    try:
        zhRepository = ZhRepository(TZH)

        # delete references
        DB.session.query(CorZhRef).filter(CorZhRef.id_zh == id_zh).delete()

        # delete criteres delim
        id_lim_list = DB.session.query(TZH).filter(TZH.id_zh == id_zh).one().id_lim_list
        DB.session.query(CorLimList).filter(
            CorLimList.id_lim_list == id_lim_list
        ).delete()

        # delete cor_zh_area
        DB.session.query(CorZhArea).filter(CorZhArea.id_zh == id_zh).delete()

        # delete files in TMedias and repos
        zh_uuid = DB.session.query(TZH).filter(TZH.id_zh == id_zh).one().zh_uuid
        q_medias = (
            DB.session.query(TMedias).filter(TMedias.unique_id_media == zh_uuid).all()
        )
        for media in q_medias:
            delete_file(media.id_media)

        zhRepository.delete(id_zh, g.current_user)
        DB.session.commit()

        return {"message": "delete with success"}, 200
    except Exception as e:
        DB.session.rollback()
        if e.__class__.__name__ == "ZHApiError":
            raise ZHApiError(
                message=str(e.message), details=str(e.details), status_code=400
            )
        raise ZHApiError(message="error_during_zh_delete", details=str(e))
    finally:
        DB.session.close()


@blueprint.errorhandler(ZHApiError)
def handle_geonature_zh_api(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@blueprint.route("/<int:id_zh>/taxa")
@permissions.check_cruved_scope("C", module_code="ZONES_HUMIDES")
def write_csv(id_zh):
    try:
        names = []
        FILE_PATH = blueprint.config["file_path"]
        MODULE_NAME = blueprint.config["MODULE_CODE"].lower()
        zh_code = DB.session.query(TZH).filter(TZH.id_zh == id_zh).one().code
        # author name
        user = (
            DB.session.query(User).filter(User.id_role == g.current_user.id_role).one()
        )
        author = user.prenom_role + " " + user.nom_role
        for i in [
            "vertebrates_view_name",
            "invertebrates_view_name",
            "flora_view_name",
        ]:
            query = GenericQuery(
                DB=DB,
                tableName=blueprint.config[i]["table_name"],
                schemaName=blueprint.config[i]["schema_name"],
                filters={"id_zh": id_zh},
                limit=-1,
            )
            results = query.return_query().get("items", [])
            current_date = dt.now()
            if results:
                rows = [
                    {
                        "Groupe d'étude - classe": row.get("group_class"),
                        "Groupe d'étude - ordre": row.get("group_order"),
                        "Nom Scientifique": row.get("scientific_name"),
                        "Nom vernaculaire": row.get("vernac_name"),
                        "Types de Statuts": row.get("statut_type"),
                        "Statuts d’évaluation, de protection et de menace": row.get(
                            "statut"
                        ),
                        "Article": row.get("article"),
                        "Lien Article": row.get("doc_url"),
                        "Nombre d'observations": row.get("obs_nb"),
                        "Date de la dernière observation": row.get("last_date"),
                        "Dernier observateur": row.get("observer"),
                        "Organisme": row.get("organisme"),
                    }
                    for row in results
                ]
                name_file = (
                    blueprint.config[i]["category"]
                    + "_"
                    + blueprint.config["species_source_name"]
                    + "_"
                    + zh_code
                    + "_"
                    + current_date.strftime("%Y-%m-%d-%H:%M:%S")
                    + ".csv"
                )
                media_path = Path("external_modules", MODULE_NAME, FILE_PATH, name_file)
                full_name = ROOT_DIR / media_path
                names.append(str(full_name))
                with open(full_name, "w", encoding="utf-8-sig", newline="") as f:
                    writer = csv.DictWriter(f, delimiter=";", fieldnames=rows[0].keys())
                    writer.writeheader()
                    writer.writerows(rows)

                id_media = post_file_info(
                    id_zh,
                    name_file.split(".csv")[0],
                    author,
                    "Liste des taxons générée sur demande de l'utilisateur dans l'onglet 5",
                    ".csv",
                )

                DB.session.flush()

                # update TMedias.media_path with media_filename
                DB.session.query(TMedias).filter(TMedias.id_media == id_media).update(
                    {"media_path": str(media_path)}
                )

                DB.session.commit()
        return {"file_names": names}, 200
    except Exception as e:
        DB.session.rollback()
        if e.__class__.__name__ == "DataError":
            raise ZHApiError(
                message="csv_taxa_db_error",
                details=str(e.orig.diag.sqlstate + ": " + e.orig.diag.message_primary),
                status_code=400,
            )
        if e.__class__.__name__ == "ZHApiError":
            raise ZHApiError(message=str(e.message), details=str(e.details))
        exc_type, value, tb = sys.exc_info()
        raise ZHApiError(
            message="csv_taxa_error",
            details=str(exc_type) + ": " + str(e.with_traceback(tb)),
        )
    finally:
        DB.session.close()


@blueprint.route("/user/cruved", methods=["GET"])
@permissions.check_cruved_scope("R")
@json_resp
def returnUserCruved():
    # récupérer le CRUVED complet de l'utilisateur courant
    user_cruved = get_scopes_by_action(module_code=blueprint.config["MODULE_CODE"])
    return user_cruved


@blueprint.route("/user/rights/<int:id_zh>", methods=["GET"])
@permissions.check_cruved_scope("R")
def userRights(id_zh):
    user_cruved = get_user_cruved()
    zh = ZH(id_zh).zh
    return {
        k: zh.user_is_allowed_to(g.current_user, user_cruved[k])
        for k in user_cruved.keys()
    }


@blueprint.route("/export_pdf/<int:id_zh>", methods=["GET"])
def download(id_zh: int):
    """
    Downloads the report in pdf format
    """
    zh = ZH(id_zh=id_zh).zh
    author_role = zh.authors
    author = f"{author_role.prenom_role} {author_role.nom_role.upper()}"
    last_date = zh.update_date
    media = get_last_pdf_export(id_zh=id_zh, last_date=last_date)
    if media is None:
        dataset = get_complete_card(id_zh)
        dataset["config"] = blueprint.config
        module_name = blueprint.config["MODULE_CODE"].lower()
        upload_path = blueprint.config["file_path"]
        filename = f'{id_zh}_fiche_{dt.now().strftime("%Y-%m-%d")}.pdf'
        stored_filename = f"{uuid.uuid4()}.pdf"
        media_path = Path(
            ROOT_DIR, "external_modules", module_name, upload_path, stored_filename
        )
        pdf_file = gen_pdf(id_zh=id_zh, dataset=dataset, filename=media_path)
        post_file_info(
            id_zh=id_zh,
            title=filename,
            author=author,
            description="Fiche de synthèse de la zone humide",
            extension=".pdf",
            media_path=str(media_path),
        )

        return send_file(pdf_file, as_attachment=True)
    else:
        return send_file(get_file_path(media.id_media), as_attachment=True)


@blueprint.route("/departments", methods=["GET"])
@json_resp
def departments():
    query = (
        DB.session.query(LAreas)
        .with_entities(
            LAreas.area_name, LAreas.area_code, LAreas.id_type, BibAreasTypes.type_code
        )
        .join(BibAreasTypes, LAreas.id_type == BibAreasTypes.id_type)
        .filter(BibAreasTypes.type_code == "DEP")
        .filter(LAreas.enable)
        .order_by(LAreas.area_code)
    )
    resp = query.all()
    return [{"code": r.area_code, "name": r.area_name} for r in resp]


@blueprint.route("/communes", methods=["POST"])
@json_resp
def get_area_from_department() -> dict:
    code = request.json.get("code")
    if code:
        query = (
            DB.session.query(LiMunicipalities)
            .with_entities(LiMunicipalities.id_area, LAreas.area_name, LAreas.area_code)
            .join(LAreas, LiMunicipalities.id_area == LAreas.id_area)
            .filter(LiMunicipalities.insee_com.like("{}%".format(code)))
            .filter(LAreas.enable)
        )
        query = query.order_by(LAreas.area_code)
        resp = query.all()
        return [{"code": r.area_code, "name": r.area_name} for r in resp]

    return []


@blueprint.route("/bassins", methods=["GET"])
@json_resp
def bassins():
    query = DB.session.query(TRiverBasin).with_entities(
        TRiverBasin.id_rb, TRiverBasin.name
    )
    resp = query.order_by(TRiverBasin.name).all()
    return [{"code": r.id_rb, "name": r.name} for r in resp]


@blueprint.route("/zones_hydro", methods=["POST"])
@json_resp
def get_hydro_zones_from_bassin() -> dict:
    code = request.json.get("code")
    if code:
        query = (
            DB.session.query(THydroArea)
            .with_entities(THydroArea.id_hydro, THydroArea.name, TRiverBasin.id_rb)
            .filter(TRiverBasin.id_rb == code)
            .join(
                TRiverBasin,
                func.ST_Contains(
                    func.ST_SetSRID(TRiverBasin.geom, 4326),
                    func.ST_SetSRID(THydroArea.geom, 4326),
                ),
            )
        )

        resp = query.order_by(THydroArea.name).all()
        return [{"code": r.id_hydro, "name": r.name} for r in resp]

    return []


@blueprint.route("/<int:id_zh>/hierarchy", methods=["GET"])
@permissions.check_cruved_scope("R", module_code="ZONES_HUMIDES")
@json_resp
def get_hierarchy(id_zh):
    """Get zh note"""
    try:
        hierarchy = Hierarchy(id_zh).__str__()
        return hierarchy
    except ZHApiError as e:
        raise ZHApiError(
            message=str(e.message), details=str(e.details), status_code=e.status_code
        )
    except Exception as e:
        exc_type, value, tb = sys.exc_info()
        raise ZHApiError(
            message="get_hierarchy_error",
            details=str(exc_type) + ": " + str(e.with_traceback(tb)),
        )
    finally:
        DB.session.rollback()
        DB.session.close()


@blueprint.route("/hierarchy/fields/<int:id_rb>", methods=["GET"])
@permissions.check_cruved_scope("R", module_code="ZONES_HUMIDES")
@json_resp
def get_hierarchy_fields(id_rb):
    return get_all_hierarchy_fields(id_rb=id_rb)
