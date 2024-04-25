import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.styles.styles import sizeNum as sizeNum
from link_bio.components.info_text import info_text


def header() ->rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(src="fash.enc", size="7",color_scheme="iris",radius="full"),
            rx.vstack(
                rx.heading("Hola son Angel Alonso Rodriguez Dominguez ", size="8"),
                rx.text("Siguem en mis redes sociales:",rx.text.strong("@Rdangellons")),
                rx.text("Soy ingeniero en sistemas computacionales y estamos aprendiendo desarrollo web con python.")
            ),
            spacing=sizeNum.BIG.value
        ),
        rx.hstack(
                link_icon("https://lucide.dev/icons/corner-up-right"),
                link_icon("https://lucide.dev/icons/corner-up-right"),
                link_icon("https://lucide.dev/icons/corner-up-right"),
                link_icon("https://lucide.dev/icons/corner-up-right"),
              
        ),
      
        rx.flex(
            info_text("+13","años de experiencia"),
            rx.spacer(),
            info_text("+13","años de experiencia"),
            rx.spacer(),
            info_text("+13","años de experiencia"),
            width="100%"
        ),
       
        rx.text("Hola Mundo estamos aprendiendo a progrmar en reflex jeje y vamos ganando mas confianza"
        ),

        align="center",
        #sirve para tamaños permitidos sobre 1 al 9
        spacing=sizeNum.BIG.value

    )