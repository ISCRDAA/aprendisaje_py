import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title


def links() ->rx.Component:
    return rx.vstack(
        title("Bienvenidos"),
        link_button(
            "hola mundo",
            "Buenas tardes",
            "https://www.google.com/?hl=es"
        ),
        title("Comunidad"),
        link_button(
            "youtube",
            "vamos con todo",
            "https://www.google.com/?hl=es"
            ),
        title("Redes sociales"),
        link_button(
            "discord",
            "Vamos a hablar",
            "https://www.google.com/?hl=es"
            ),
        width="100%"
    )