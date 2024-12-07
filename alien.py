import pgzrun
import random
title="good shot"
width=500
height=500
msg=""
alien=Actor("alien")
def draw():
    screen.clear()
    screen.fill(color=(128,0,0))
    alien.draw()
    screen.draw.text(msg,center=(400,10),fontsize=30)
def place_alien():
    alien.x=random.randint(50,width-50)
    alien.y=random.randint(50,width-50)
def on_mouse_down(pos):
    global msg 
    if alien.collidepoint(pos):
        msg="good shot"
        place_alien()
    else:
        msg="next time"
place_alien()
pgzrun.go()
