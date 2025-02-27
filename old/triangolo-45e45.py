# --------------------------------------------- #
# Costruzione del triangolo rettangolo isoscele #
# --------------------------------------------- #
import turtle
from math import sqrt

tom = turtle.Turtle()
tom.shape('turtle')

ipotenusa = 200
cateto = ipotenusa / 2 * sqrt(2)

tom.forward(ipotenusa)
tom.left(135)
tom.forward(cateto)
tom.left(90)
tom.forward(cateto)

tom.hideturtle()

# -------------------------------------- #
# La parte di codice che segue serve a   #
# evidenziare l'angolo retto ed è quindi #
# non necessaria per la costruzione del  #
# triangolo rettangolo.                  #
# -------------------------------------- #

vertice = (ipotenusa / 2, ipotenusa / 2)
tom.penup()
tom.goto(vertice)
tom.pencolor('red')

def quadrato(tartaruga,lato):
    for i in range(4):
        tartaruga.pendown()
        if i == 0 or i == 3:
            tartaruga.penup()
        tartaruga.forward(lato)
        tartaruga.left(90)

quadrato(tom, ipotenusa/15)
