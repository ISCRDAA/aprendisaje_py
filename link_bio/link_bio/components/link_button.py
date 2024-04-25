import reflex as rx
import link_bio.styles.styles as styles


def link_button(title:str,body:str,url:str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
               
                rx.icon(tag="corner-up-right",width=styles.size.BIG.value),
                rx.vstack(
                    rx.text(title,style=styles.button_title_stily),
                    rx.text(body,style=styles.button_body_stily),
                    
                )
            ),

         width="100%",
         color_scheme="crimson"
        ),
        href=url,
        is_external=True,    
        width="100%",
        
        
    )