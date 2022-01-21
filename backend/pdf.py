from pathlib import Path
from io import BytesIO
import base64
from datetime import datetime as dt

from flask import current_app, render_template
from weasyprint import HTML

try:
    from staticmap import StaticMap, Line
except ImportError:
    print('cannot import staticmap, map generation in pdf will be unavailable')

from .utils import get_main_picture_id, get_file_path


def get_main_picture(id_zh: int):
    id_media = get_main_picture_id(id_zh)
    if id_media:
        file_path: str = get_file_path(id_media)
        with open(file_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        return "data:image/jpeg;base64," + encoded_string.decode()
    return None


def gen_map(coordinates, url_template=None):
    if url_template is None:
        url_template = 'http://c.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png'
    if coordinates:
        m = StaticMap(width=600, height=300, url_template=url_template)
        for coord in coordinates:
            poly = Line(coord, 'blue', 4)
            m.add_line(poly)
        image = m.render()
        with BytesIO() as output:
            image.save(output, format='PNG')
            contents =  base64.b64encode(output.getvalue())
        return "data:image/jpeg;base64," + contents.decode()
    return None


def multi_to_polys(multi):
    polys = []
    for mul in multi:
        polys += mul
    return tuple(polys)


def gen_pdf(id_zh, dataset, filename = "rapport.pdf"):
    coordinates = dataset.get('geometry', {}).get('coordinates', [[]])
    poly_type = dataset.get('geometry', {}).get('type', '')
    if poly_type is not None:
        if poly_type == 'Polygon':
            coordinates = coordinates
        else:
            coordinates = multi_to_polys(coordinates)
    try:
        # For now, the url_template cannot be taken from the config since
        # StaticMap does not support urls like : 
        # {s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png with the "{s}"
        dataset['map'] = gen_map(coordinates)
    except Exception as e:
        print('Cannot generate the map inside the pdf... Continuing')
    
    try:
        dataset['image'] = get_main_picture(id_zh=id_zh)
    except Exception as e:
        print('Cannot find image')

    pdf_file = generate_pdf_from_template("fiche_template_pdf.html", dataset, filename)
    return Path(pdf_file)

@current_app.template_filter('datetime_format')
def datetime_format(value: str, format="%d-%m-%y"):
    date = dt.strptime(value, '%Y-%m-%d %H:%M:%S')
    return date.strftime(format)

def generate_pdf_from_template(template, data, filename):
    template_rendered = render_template(template, data=data)
    html_file = HTML(string=template_rendered, base_url=current_app.config['API_ENDPOINT'], encoding="utf-8")
    html_file.write_pdf(filename)
    return filename
