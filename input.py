from turtle import *

import turtle
 
from turtle import *
import turtle as turt

ws = turt.Screen()

tur = turt.Turtle()
tur.color("cyan")
tur.shape("turtle")
tur.penup()

def goForward():
    ans = int(ws.textinput("Python guides", "Enter the values in pixels"))
    tur.forward(ans)

def goBackward():
    tur.backward(5)

turt.listen()
turt.onkey(goForward,"Up")
turt.onkey(goBackward, "Down")
turt.done()