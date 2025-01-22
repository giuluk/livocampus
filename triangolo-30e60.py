# ---------------------------------------- #
# Costruzione del triangolo rettangolo con #
# angoli acuti di 30° e 60°                #
# ---------------------------------------- #
import turtle
from math import sqrt

tom = turtle.Turtle()
tom.shape('turtle')

ipotenusa = 300
cateto_minore = ipotenusa / 2
cateto_maggiore = ipotenusa / 2 * sqrt(3)

tom.forward(ipotenusa)
tom.left(120)
tom.forward(cateto_minore)
tom.left(90)
tom.forward(cateto_maggiore)

tom.hideturtle()


# ---------------------------------------#
# La parte di codice che segue serve a   #
# evidenziare l'angolo retto ed è quindi #
# non necessaria per la costruzione del  #
# triangolo rettangolo.                  #
# -------------------------------------- #

vertice = (ipotenusa * 3 / 4, ipotenusa * sqrt(3) / 4)
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