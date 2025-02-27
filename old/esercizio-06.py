# -------------------------------------- #
# Costruzione del triangolo isoscele con #
# angoli alla base di 30°                #
# -------------------------------------- #
import turtle
from math import sqrt

tom = turtle.Turtle()
tom.shape('turtle')

lato_obliquo = 200

# L'altezza di un triangolo isoscele con angoli alla base di
# ampiezza 30° è pari al prodotto tra il lato obliquo e la
# radice quadrata di 3 e coincide con la mediana.
base = lato_obliquo * sqrt(3)

tom.forward(base)
tom.left(150)
tom.pencolor('red')
tom.forward(lato_obliquo)
tom.left(60)
tom.forward(lato_obliquo)

tom.hideturtle()