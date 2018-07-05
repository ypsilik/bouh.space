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
    description = "Assemblage : Place the eyes on body, then embroider the mouth. Take three from the leaves, and place two behind the first one – overlapping behind it. Place them on the head with a sewing needle, then secure with sewing them on the head, using a tapestry needle. Sew the two others behind the first three, where the gaps are. Make the feet."

    materiels = [
      "Rico Baby cotton yarn 50 g/125 m in medium blue",
      "Rico Baby cotton yarn 50 g/125 in dark green ",
      "3 mm crochet hook ",
      "Polyester fiberfill ",
      "A pair of 6 mm black craft eyes ",
      "Craft glue ",
      "Tapestry needle ",
      "Black embroidery floss and needle"
    ]

    head = [
        {"rg": "1", "val": "6 sc in magic ring <b>(6)</b>"},
        {"rg": "2", "val": "Inc around <b>(12)</b>"},
        {"rg": "3", "val": "*sc, inc* <b>(18)</b>"},
        {"rg": "4", "val": "*2sc, inc* <b>(24)</b>"},
        {"rg": "5 - 7", "val": "sc around <b>(24)</b>"},
        {"rg": "8", "val": "*2sc, dec* <b>(18)</b>"},
        {"rg": "9", "val": "sc around "},
        {"rg": "10", "val": "*sc, dec* Stuff with polyfil firmly"},
        {"rg": "11", "val": "Dec FO and weave in."}
    ]

    leaf = [
        {"rg": "1", "val": "Start with a loop, leaving a long tail for sewing."},
        {"rg": "2", "val": "ch 10, sl st 3, ch 3, hdc 2, last: hdc 4, turn around."},
        {"rg": "3", "val": "hdc next 3, sc next 3, sl st the rest. Do not join yet. Ch 2, sl st to the second ch from hook. Join. FO and weave in."},
        {"rg": "4", "val": "Make four more."}
    ]

    feet = [
        {"rg": "1", "val": "Using crocheting on the surface technique, slip in your loop."},
        {"rg": "2", "val": "Ch 2. Dc to the second ch from hook. Sl st back to the same place. "},
        {"rg": "3", "val": "If you find it complicated you can also do it with the regular crochet technique using the same pattern and sew it on the body."}
    ]

    etapes_pattern = [
        {"partie": "head", "laine": "Medium blue", "rangs": head},
        {"partie": "leaf", "laine": "Dark green", "rangs": leaf},
        {"partie": "feet", "laine": "Medium blue", "rangs": feet}
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
