import reflex as rx
from link_bio.styles.styles import size as size
import datetime
def footer()->rx.Component:
    return rx.vstack(
        rx.image(src="imagen perfil blog.jpg",width="10em",height="10em"),
        rx.link(f"2014-{datetime.date.today().year} Aleana & Carlup", href="https://www.instagram.com/aleana_carlup_mx/",is_external=True,font_size=size.MEDIUM.value),

        rx.text("aleana carlup todos los derechos reservados",
                margin_top="0px !important"
        ),
        


        align="center",
        margin_bottom=size.BIG.value
        )
        