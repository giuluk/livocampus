# ------------------------------------ #
# Triangolo rettangolo 30° e 60° v.1.0 #
# ------------------------------------ #
import turtle
from math import sqrt # sqrt() è una funzione per radice quadrata

# Assegnazioni delle variabili
tom = turtle.Turtle()
ipotenusa = 180
cateto1 = ipotenusa / 2
cateto2 = ipotenusa * sqrt(3) / 2

# Attributi della tartaruga
tom.shape('turtle')

# Azioni della tartaruga
tom.forward(cateto1)
tom.left(120)
        
tom.forward(ipotenusa)
tom.left(150)

tom.forward(cateto2)
tom.left(90)