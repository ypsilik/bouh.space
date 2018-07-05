#!/usr/bin/env python
import os
from jinja2 import Environment, FileSystemLoader

PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, 'templates')),
    trim_blocks=True,
    lstrip_blocks=True)

### grandmere
def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)

def create_index_html():
    fname = "grandmere.html"
    nom_pattern = "Grand-mère"
    photo = "images/grandma/grandma.jpg"
    description = "This a crochet project for beginners to intermediate. You will practice how to crochet different amigurumi structures as well as how to add felt details to amigurumis. What will happen to Santa Claus without her beloved partner Mama Santa? She helps him with the daily activities in the Factory. Preparing the presents of all the kids of the world is not a easy task, you need help of hundreds of elves plus the love and talent of Mama Santa. Mama Santa lives with Santa Claus in \"Ear fell\" in the Finnish Lappland. Amigurumi Mama Santa We made Santa Claus a companion \"Mama Santa\" because togehter both of them are the personification of the importance of female and male energies on our planet. We as individuals are created of the same stardust and we complement each other in everything we do. One could not live without the other.:) The hook ninja mascot."

    materiels = [
      "White felt",
      "Red Yarn 4mm",
      "Peach Yarn 4mm",
      "White Yarn 4mm",
      "Black Yarn 4mm",
      "Felting Needle",
      "Optional pink felt for the cheeks",
      "1 pair of safety eyes",
      "Fiber filling",
      "A Hook 4mm",
      "A piece of copper wire",
      "Tweezers"
    ]

    head = [
      {"rg": "1", "val": "6 sc in magic ring <b>(6 sts)</b>"},
      {"rg": "2", "val": "Inc around <b>(12 sts)</b>"},
      {"rg": "3", "val": "*Inc, sc*, around <b>(18 sts)</b>"},
      {"rg": "4", "val": "*Inc, 2sc*, around <b>(24 sts)</b>"},
      {"rg": "5", "val": "*Inc, 3sc*,around <b>(30 sts)</b>"},
      {"rg": "6", "val": "*Inc, 4sc*, around <b>(36 sts)</b>"},
      {"rg": "7", "val": "*Inc, 5sc*, around <b>(42 sts)</b>"},
      {"rg": "8 - 13", "val": "Sc around <b>(42 sts)</b>"},
      {"rg": "14", "val": "*Dec, 5sc*, around <b>(36 sts)</b>"},
      {"rg": "15", "val": "*Dec, 4sc*, around <b>(30 sts)</b>"},
      {"rg": "16", "val": "*Dec, 3sc*, around <b>(24 sts)</b>"},
      {"rg": "17", "val": "*Dec, 2sc*, around <b>(18 sts)</b>"},
      {"rg": "18", "val": "*Dec, sc*, around <b>(12 sts)</b>"},
      {"rg": "19", "val": "Dec around <b>(6 sts)</b>"},
      {"rg": "20", "val": "Fasten off and weave in ends."}
    ]

    body = [
      {"rg": "1", "val": "6 sc in magic ring <b>(6 sts)</b>"},
      {"rg": "2", "val": "Inc around <b>(12 sts)</b>"},
      {"rg": "3", "val": "*Inc, sc* around <b>(18 sts)</b>"},
      {"rg": "4", "val": "*Inc, 2sc* around <b>(24 sts)</b>"},
      {"rg": "5 - 8", "val": "sc around <b>(24 sts)</b>"},
      {"rg": "9", "val": "*Dec, sc* around <b>(18 sts)</b>"},
      {"rg": "10", "val": "Fasten off and leave a tail to sew later."},
      {"rg": "11", "val": "Fill the head with stuffing."}
    ]

    apron = [
        {"rg": "1", "val": "ch13"},
        {"rg": "2", "val": "sc in each, turn and sc in each 5 times."},
        {"rg": "3", "val": "Fasten off, weave the ends"}
    ]

    # ajouté a belt : <img src="images/grandma/belt.jpg" title="belt">
    belt = [
        {"rg": "1", "val": "Chain 30 sew as shown in the picture."}
    ]

    hand = [
		{"rg": "1", "val": "Sc 4 into mr <b>(4 sts)</b>"},
		{"rg": "2", "val": "Inc around, place marker <b>(8 sts)</b>"},
		{"rg": "-", "val": "Switch to red yarn"},
		{"rg": "3 - 6", "val": "sc around <b>(8 sts)</b>"},
		{"rg": "7", "val": "Fasten off, leave a tail for sewing to the body."}
    ]

    feet = [
        {"rg": "1", "val": "Sc 5 into mr <b>(5 sts)</b>"},
        {"rg": "2", "val": "Inc around <b>(10 sts)</b>"},
        {"rg": "3", "val": "Sc around <b>(10 sts)</b>"},
        {"rg": "4", "val": "Fasten off, leave a tail to sew to the body."}
    ]

    glasses = [
        {"rg": "1", "val": "Ch 61 sts, Fasten off and tie with a bow"},
        {"rg": "-", "val": "En fil de fer"},
        {"rg": "1", "val": "Take the piece of copper wire and your tweezers, cut a piece measuring app 10 cm."},
        {"rg": "2", "val": "with the help pf the tweezers twist the wire starting from the outer part inwards, cut the remain wire."},
        {"rg": "3", "val": "Sew them on place with white thread."}
    ]

    etapes_pattern = [
        {"partie": "head", "laine": "White", "rangs": head},
        {"partie": "body", "laine": "Red", "rangs": body},
        {"partie": "apron", "laine": "White", "rangs": apron},
        {"partie": "belt", "laine": "White", "rangs": belt},
        {"partie": "hand", "laine": "Peach & red", "rangs": hand},
        {"partie": "feet", "laine": "Black", "rangs": feet},
        {"partie": "glasses", "laine": "Black", "rangs": glasses}
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
