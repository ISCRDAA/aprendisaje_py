import reflex as rx
import datetime
def footer()->rx.Component:
    return rx.vstack(
        rx.image(src="imagen perfil blog.jpg",width="10em",height="10em"),
        rx.link(f"2014-{datetime.date.today().year} Aleana & Carlup", href="https://www.instagram.com/aleana_carlup_mx/",is_external=True),
        rx.text("aleana carlup todos los derechos reservados"),
        align="center"
        )
        