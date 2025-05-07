# ----------------------------------- #
# Triangolo rettangolo isoscele v.1.0 #
# ----------------------------------- #
import turtle
from math import sqrt # sqrt() è una funzione per radice quadrata

# Assegnazioni delle variabili
tom = turtle.Turtle()
ipotenusa = 180
cateto = ipotenusa * sqrt(2) / 2

# Attributi della tartaruga
tom.shape('turtle')

# Azioni della tartaruga
tom.forward(cateto)
tom.left(135)
        
tom.forward(ipotenusa)
tom.left(135)

tom.forward(cateto)
tom.left(90)