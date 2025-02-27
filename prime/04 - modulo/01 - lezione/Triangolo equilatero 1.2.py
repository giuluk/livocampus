# -------------------------- #
# Triangolo equilatero v.1.2 #
# -------------------------- #
import turtle

# Assegnazioni delle variabili
tom = turtle.Turtle()
lato = 150

# Attributi della tartaruga
tom.shape('turtle')

# Azioni della tartaruga
for _ in range(3):
    tom.forward(lato)
    tom.left(120)