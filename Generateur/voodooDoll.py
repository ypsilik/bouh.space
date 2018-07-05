#!/usr/bin/env python
import os
from jinja2 import Environment, FileSystemLoader

PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, 'templates')),
    trim_blocks=True,
    lstrip_blocks=True)


### voodoo doll
def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)


def create_index_html():
    fname = "voodoo_doll.html"
    photo = "images/voodoo_doll/voodoo_doll.jpg"
    nom_pattern = "Voodoo Doll"
    description = "Assembly : 1. Set the head on top of the body and stitch the two together. 2. Pinch the top of the leg and stitch it closed. 3. Stitch the leg to the body at the base of the doll’s belly. Put another way, attach the leg in such a way that the doll can sit upright unassisted. Repeat for the other leg. 4. Sew the whole arm to the left side of the body (your right, doll’s left). 5. Sew the torn arm to the right side of the body (your left, doll’s right). 6. Stitch the buttons onto the face using your sewing (or tapestry) needle and thread. 7. Add stitches as desired using scraps of dark brown thread."

    materiels = [
      "Pale brown",
			"Chocolate brown",
			"White or off-white",
			"Two mismatched buttons"
    ]

    head = [
        {"rg": "1", "val": "5 sc in magic ring <b>(5)</b>"},
        {"rg": "2", "val": "*inc* <b>(10)</b>"},
				{"rg": "3", "val": "*inc* <b>(20)</b>"},
				{"rg": "4", "val": "*3sc, inc* <b>(25)</b>"},
				{"rg": "5", "val": "*4sc, inc* <b>(30)</b>"},
				{"rg": "6", "val": "*5sc, inc* <b>(35)</b>"},
				{"rg": "7", "val": "*6sc, inc* <b>(40)</b>"},
				{"rg": "8-11", "val": "*sc* <b>(40)</b>"},
				{"rg": "12", "val": "*6sc, dec* <b>(35)</b>"},
				{"rg": "13", "val": "*5sc, dec* <b>(30)</b>"},
				{"rg": "14", "val": "*4sc, dec* <b>(25)</b>"},
				{"rg": "15", "val": "*3sc, dec* <b>(20)</b>"},
				{"rg": "16", "val": "Fasten off, leaving a long tail for stitching the head to the body"}
    ]

		body = [
				{"rg": "1", "val": "5 sc in magic ring <b>(5)</b>"},
        {"rg": "2", "val": "*inc* <b>(10)</b>"},
				{"rg": "3", "val": "*inc* <b>(20)</b>"},
				{"rg": "4", "val": "*3sc, inc* <b>(25)</b>"},
				{"rg": "5-8", "val": "*sc* <b>(25)</b>"},
				{"rg": "9", "val": "*3sc, dec* <b>(20)</b>"},
				{"rg": "10-11", "val": "*sc* <b>(20)</b>"},
				{"rg": "11", "val": "*2sc,dec* <b>(15)</b>"},
				{"rg": "12", "val": "Fasten off"}
		]
		
		leg = [
				{"rg": "1", "val": "5 sc in magic ring <b>(5)</b>"},
        {"rg": "2", "val": "*inc* <b>(10)</b>"},
				{"rg": "3", "val": "*inc* <b>(20)</b>"},
				{"rg": "4", "val": "*blo* <b>(20)</b>"},
				{"rg": "5-6", "val": "*sc* <b>(20)</b>"},
				{"rg": "7", "val": "*2sc, dec* <b>(15)</b>"},
				{"rg": "8", "val": "*sc* <b>(15)</b>"},
				{"rg": "9", "val": "*sc,dec* <b>(10)</b>"},
				{"rg": "10", "val": "*sc* <b>(10)</b>"},
				{"rg": "11", "val": "Fasten off, leaving a very long tail for sewing the leg closed AND attaching the leg to the body"},
				{"rg": "", "val": "Stuff leg roughly HALFWAY full. You will be pinching the top of the leg closed before sewing it to the body."}	
		]
		
		Whole_Arm = [
				{"rg": "1", "val": "5 sc in magic ring <b>(5)</b>"},
        {"rg": "2", "val": "*inc* <b>(10)</b>"},
				{"rg": "3", "val": "*blo* <b>(10)</b>"},
				{"rg": "4-7", "val": "*sc* <b>(10)</b>"},
				{"rg": "8", "val": "Fasten off, leaving a long tail for stitching the whole arm to the body"}
		]
		
		Torn_Arm = [
				{"rg": "1", "val": "5 sc in magic ring <b>(5)</b>"},
        {"rg": "2", "val": "*inc* <b>(10)</b>"},
				{"rg": "3", "val": "*blo* <b>(10)</b>"},
				{"rg": "4", "val": "sc next 4st"},
				{"rg": "5", "val": "Fasten off"}
		]

		Torn_Arm_Stuffing = [
				{"rg": "1", "val": "5 sc in magic ring <b>(5)</b>"},
        {"rg": "2", "val": "*inc* <b>(10)</b>"},
				{"rg": "3", "val": "3sc next st, dec, sc, ch2, sc, ch3, sc ,next 3 st"},
				{"rg": "4", "val": "Fasten off, leaving a long tail"},
				{"rg": "5", "val": "Weave the tail through the stitches in Row 2, pulling the stuffing together so it bunches and puckers."},
				{"rg": "6", "val": "FAttach the stuffing securely to Torn Arm"}
		]
		
    etapes_pattern = [
        {"partie": "Head", "laine": "Pale brown", "rangs": head},
				{"partie": "Body", "laine": "Pale brown", "rangs": body},
				{"partie": "Leg (make 2)", "laine": "Pale brown", "rangs": leg},
				{"partie": "Whole Arm", "laine": "Pale brown", "rangs": Whole_Arm},
				{"partie": "Torn Arm", "laine": "Pale brown", "rangs": Torn_Arm},
				{"partie": "Torn Arm Stuffing", "laine": "White or off-white", "rangs": Torn_Arm_Stuffing}
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
