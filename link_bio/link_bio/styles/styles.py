import reflex as rx
from enum import Enum

#constantes
MAX_WIDTH="600PX"

#Sizes
class size(Enum):
    SAMLL="0.5em"
    MEDIUM="0.8em"
    DEFAULT="1em"
    BIG="2em"
#sirve para tamaños permitidos entre 1 y 9
class sizeNum(Enum):
    BIG="6"
    MEDIUM="4"
    SMALL="2"

#stilos 
STYLES={
    rx.button:{
        "width":"100%",
        "height":"100%",
        "display":"block",
        "padding":size.SAMLL.value,
        "border_radius":size.DEFAULT.value
    },
    rx.link:{
        "text_decoration":"none",
        "_hover":{},
    }
}
title_style=dict(
    size="8",
    width="100%",
    padding_top=size.DEFAULT.value
)

button_title_stily= dict(
    font_size=size.DEFAULT.value,

)
button_body_stily= dict(
    font_size=size.MEDIUM.value,
    
)
       