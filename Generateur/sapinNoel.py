#!/usr/bin/env python
import os
from jinja2 import Environment, FileSystemLoader

PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, 'templates')),
    trim_blocks=True,
    lstrip_blocks=True)


### sapin de noel
def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)


def create_index_html():
    fname = "sapin_noel.html"
    photo = "images/sapin_noel/sapin_noel.jpg"
    nom_pattern = "Christmas tree"
    description = ""

    materiels = [
      "Dark green wool",
    ]

    sapin = [
        {"rg": "1", "val": "3 sc in magic ring <b>(3)</b>"},
        {"rg": "2", "val": "*blo* <b>(3)</b>"},
        {"rg": "3", "val": "inc with blo* <b>(6)</b>"},
        {"rg": "4", "val": "inc with flo*, turn wool<b>(12)</b>"},
        {"rg": "5", "val": "*slst, none, 7dc, none* (3 times) <b>(24)</b>"},
        {"rg": "6", "val": "*sc, 2none, sc, 2none, sc 2none, sc* (3times) put wool turn 4 (turn 5 = leaf) <b>(12)</b>"},
        {"rg": "7", "val": "*inc,sc,sc* <b>(16)</b>"},
        {"rg": "8", "val": "*7dc, none, slst, none* (4 times) <b>(32)</b>"},
        {"rg": "9", "val": "*sc, 2none, sc, 2none, sc, 2none, sc* <b>(16) (4 times) put wool turn 7 (turn 8 = leaf)</b>"},
        {"rg": "10", "val": "*inc, sc, sc* <b>(22)</b>"},
        {"rg": "11", "val": "*7dc, none, slst, none* (5 times) + slst, none <b>(41)</b>"}
    ]


    etapes_pattern = [
        {"partie": "Christmas tree", "laine": "Dark green", "rangs": sapin}
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
