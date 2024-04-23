import reflex as rx


def header() ->rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(src="fash.enc", size="7",color_scheme="iris",radius="full"),
            rx.vstack(
                rx.heading("Hola son Angel Alonso Rodriguez Dominguez ", size="8"),
                rx.text("Siguem en mis redes sociales:",rx.text.strong("@Rdangellons")),
                rx.text("Soy ingeniero en sistemas computacionales y estamos aprendiendo desarrollo web con python.")
            ),
            
        ),
        rx.text("Hola Mundo estamos aprendiendo a progrmar en reflex jeje y vamos ganando mas confianza"
        ),

        align="center"
    )