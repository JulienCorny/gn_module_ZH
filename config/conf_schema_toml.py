'''
   Spécification du schéma toml des paramètres de configurations
   La classe doit impérativement s'appeller GnModuleSchemaConf
   Fichier spécifiant les types des paramètres et leurs valeurs par défaut
   Fichier à ne pas modifier. Paramètres surcouchables dans config/config_gn_module.tml
'''

from marshmallow import Schema, fields


class MapListConfig(Schema):
    pass


default_map_list_conf = [
    {"prop": "main_name", "name": "Nom principal"},
    {"prop": "code", "name": "Code"},
    {"prop": "sdage", "name": "Typologie SDAGE", "sortable": False},
    {"prop": "bassin_versant", "name": "Bassin versant"}
]


available_maplist_column = [
    {"prop": "main_name", "name": "Nom principal"},
    {"prop": "code", "name": "Code"},
    {"prop": "sdage", "name": "Typologie SDAGE"},
    {"prop": "bassin_versant", "name": "Bassin versant"},
    {"prop": "author", "name": "Auteur"},
    {"prop": "organism", "name": "Organisme"},
    {"prop": "update_author", "name": "Auteur dernière modification"},
    {"prop": "update_organism", "name": "Organisme de dernière modification"},
    {"prop": "create_date", "name": "Date de création"},
    {"prop": "update_date", "name": "Date de modification"}
]


nomenclatures = [
    'SDAGE-SAGE', 'SDAGE', 'CORINE_BIO', 'CRIT_DELIM', 'CRIT_DELIM', 'CRIT_DEF_ESP_FCT',
    'OCCUPATION_SOLS', 'ACTIV_HUM', 'LOCALISATION', 'IMPACTS', 'EVAL_GLOB_MENACES',
    'STATUT_PROPRIETE', 'TYP_DOC_COMM', 'PLAN_GESTION', 'PROTECTIONS', "INSTRU_CONTRAC_FINANC",
    'ENTREE_EAU', 'SORTIE_EAU', 'PERMANENCE_ENTREE', 'PERMANENCE_SORTIE', 'SUBMERSION_FREQ',
    'SUBMERSION_ETENDUE', 'TYPE_CONNEXION', 'FONCTIONNALITE_HYDRO', 'FONCTIONNALITE_BIO',
    'FONCTIONS_HYDRO', 'FONCTIONS_BIO', 'INTERET_PATRIM', 'VAL_SOC_ECO',
    'FONCTIONS_QUALIF', 'FONCTIONS_CONNAISSANCE', 'ETAT_CONSERVATION',
    'NIVEAU_PRIORITE'
]


eval_mnemonique = [
    'Moyenne', 'Forte'
]


ref_geo_referentiels = [
    {
        "zh_name": "ZNIEFF Terre Type 1",
        "type_code_ref_geo": "ZNIEFF1",
        "active": True
    },
    {
        "zh_name": "ZNIEFF Terre Type 2",
        "type_code_ref_geo": "ZNIEFF2",
        "active": True
    },
    {
        "zh_name": "RAMSAR",
        "type_code_ref_geo": "SRAM",
        "active": True
    },
    {
        "zh_name": "Natura 2000 - Directive Habitat (ZSC)",
        "type_code_ref_geo": "SIC",
        "active": True
    },
    {
        "zh_name": "Site de l’observatoire national des zones humides",
        "type_code_ref_geo": "",
        "active": False
    }
]
# pour ajouter un référentiel :
# - créer dans ref_geo.bib_areas_types la ligne correspondante au référentiel si celui n'est pas déjà répertorié
# - reporter le type_code du référentiel dans "type_code_ref_geo" et mettre "active"=True dans conf_schema_toml.py


vertebrates_view_name = {
    "schema_name": "pr_zh",
    "table_name": "vertebrates",
    "category": "vertebrates"
}


invertebrates_view_name = {
    "schema_name": "pr_zh",
    "table_name": "invertebrates",
    "category": "invertebrates"
}


flora_view_name = {
    "schema_name": "pr_zh",
    "table_name": "flora",
    "category": "flora"
}


allowed_extensions = ['.pdf', '.jpg']

max_pdf_size = 1.5  # Mo

max_jpg_size = 0.5  # Mo

filename_validated = True

fileformat_validated = True

file_path = "static"

module_dir_name = 'gn_module_zones_humides'

# Name of the source of species data (tab5)
species_source_name = 'GeoNature'


class GnModuleSchemaConf(Schema):
    default_maplist_columns = fields.List(
        fields.Dict(), load_default=default_map_list_conf)
    available_maplist_column = fields.List(
        fields.Dict(), load_default=available_maplist_column
    )
    nomenclatures = fields.List(fields.String, load_default=nomenclatures)
    ref_geo_referentiels = fields.List(
        fields.Dict(), load_default=ref_geo_referentiels
    )
    vertebrates_view_name = fields.Dict(load_default=vertebrates_view_name)
    invertebrates_view_name = fields.Dict(load_default=invertebrates_view_name)
    flora_view_name = fields.Dict(load_default=flora_view_name)
    allowed_extensions = fields.List(fields.String, load_default=allowed_extensions)
    max_pdf_size = fields.Float(load_default=max_pdf_size)
    max_jpg_size = fields.Float(load_default=max_jpg_size)
    fileformat_validated = fields.Boolean(load_default=fileformat_validated)
    filename_validated = fields.Boolean(load_default=filename_validated)
    file_path = fields.String(load_default=file_path)
    module_dir_name = fields.String(load_default=module_dir_name)
    species_source_name = fields.String(load_default=species_source_name)
