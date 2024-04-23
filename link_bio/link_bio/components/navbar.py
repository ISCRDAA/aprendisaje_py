import reflex as rx
from link_bio.styles.styles import size as size

def navbar() -> rx.Component:
    return rx.vstack(
    rx.text("Aleana & Carlup",color="black", high="80px"
    ),
   
    width="100%",
    position="sticky",
    bg="ligthgray",
    padding_x=size.DEFAULT.value,
    padding_y=size.DEFAULT.value,
    z_index="999",
    top="0"
    )