# --------------------------------- #
# Triangolo equilatero circoscritto #
# a una circonferenza v.1.0         #
# --------------------------------- #
import turtle
from math import sqrt # sqrt() è una funzione per radice quadrata

# Assegnazioni delle variabili
tom = turtle.Turtle()
lato = 180
raggio = lato / (2 * sqrt(3))

# Attributi della tartaruga
tom.shape('turtle')

# Azioni della tartaruga

# Costruzione del triangolo equilatero
for _ in range(3):
    tom.forward(lato)
    tom.left(120)

# Costruzione della circonferenza
tom.forward(lato / 2)
tom.pencolor('red')
tom.circle(raggio)
tom.hideturtle()