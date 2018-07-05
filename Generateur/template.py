#!/usr/bin/env python
import os
from jinja2 import Environment, FileSystemLoader

PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, 'templates')),
    trim_blocks=True,
    lstrip_blocks=True)


### oddish
def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)


def create_index_html():
    fname = "oddish.html"
    photo = "images/oddish/oddish.jpg"
    nom_pattern = "Oddish"
    description = "Assemblage : Place the eyes on body,"

    materiels = [
      "Rico Baby cotton yarn 50 g/125 m in medium blue",
      "Rico Baby cotton yarn 50 g/125 in dark green ",
    ]

    head = [
        {"rg": "1", "val": "6 sc in magic ring <b>(6)</b>"},
        {"rg": "2", "val": "Inc around <b>(12)</b>"},
        {"rg": "3", "val": "*sc, inc* <b>(18)</b>"},
    ]


    etapes_pattern = [
        {"partie": "head", "laine": "Medium blue", "rangs": head}
    ]
    context = {
        'nom_pattern': nom_pattern,
        'photo': photo,
        'description': description,
        'materiels': materiels,
        'etapes_pattern': etapes_pattern
    }
    with open(fname, 'w') as f:
        html = render_template('strucPatternjinja.html', context)
        f.write(html)

def main():
    create_index_html()

########################################

if __name__ == "__main__":
    main()
