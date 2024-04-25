import reflex as rx
from link_bio.styles.styles import sizeNum as sizeNum
 

def info_text(title:str, body:str)->rx.Component:
 return rx.box(
  rx.text(title,font_weight="bold",color="blue",as_="span"),
  f" {body}",font_size=sizeNum.SMALL.value
 )