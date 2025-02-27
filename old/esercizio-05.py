# ------------------------------------- #
# Baricentro di un triangolo equilatero #
# ------------------------------------- #
import turtle
from math import sqrt

tom = turtle.Turtle()
tom.shape('turtle')

# ---------------------------------------------- #
# 1a parte: costruzione del triangolo equilatero #
# (codice riciclato da esercizio-01)             #
# ---------------------------------------------- #

lato = 200

def triangolo_eq(n, l):
    for _ in range(3):
        n.forward(l)
        n.left(120)
        
triangolo_eq(tom, lato)
tom.penup()

# -------------------------------------------------------- #
# 2a parte: conduzione della tartaruga verso il baricentro #
# -------------------------------------------------------- #

# L'altezza di un triangolo equilatero è pari alla
# metà del suo lato per la radice quadrata di 3 e
# coincide con la mediana.
mediana = 1/2 * lato * sqrt(3)

# Dirigo la tartaruga nel punto medio del lato e
# la faccio ruotare in modo che la sua direzione
# sia perpendicolare al lato e il verso punti
# all'interno del triangolo equilatero. La scelta
# del lato è irrilevante.
tom.forward(lato / 2)
tom.left(90)

# Muovo la tartaruga verso il baricentro facendole
# percorrere 1/3 della mediana.
tom.forward(mediana * 1/3)

tom.down()
tom.pencolor('red')
tom.dot(10)
tom.hideturtle()