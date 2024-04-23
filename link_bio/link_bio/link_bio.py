import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.views.header.header import header
from link_bio.links.links import links
from link_bio.components.footer import footer
import link_bio.styles.styles as styles
from link_bio.styles.styles import size as size



class State(rx.State):
    pass

def index()-> rx.Component:
    return rx.box(
        navbar(),
     rx.center(
        rx.vstack(
            header(),
            links(), 
            max_width=styles.MAX_WIDTH,
            align="center",
            width="100%",
            margin_y=size.DEFAULT.value,

         ),
     ),
    

    footer()
)
        

app = rx.App(
    style=styles.STYLES
)
app.add_page(index)
app.compile()
