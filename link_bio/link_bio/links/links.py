import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title
from link_bio.styles.styles import sizeNum as sizeNum
import link_bio.links_pages as links


def links() ->rx.Component:
    return rx.vstack(
        title("youtube"),
        link_button(
            "Pagina de youtube",
            "Comparte y suscribite",
            "https://www.google.com/?hl=es"
        ),
        link_button(
            "Buenas",
            "Libros recomendados",
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
        width="100%",
        spacing=sizeNum.MEDIUM.value
    )