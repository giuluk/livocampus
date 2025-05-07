# Rettangolo inscritto in una circonferenza

import turtle
from math import sqrt, atan, degrees


tom = turtle.Turtle()
tom.shape('turtle')

base    = 100
altezza =  80
raggio  = sqrt(base**2+altezza**2) / 2

def rettangolo(n, l1, l2):
    for _ in range(2):
        n.forward(l1)
        n.left(90)
        n.forward(l2)
        n.left(90)
        
rettangolo(tom,base,altezza)

tom.right(90-degrees(atan(altezza/base))) # Questa linea di codice utilizza la Trigonometria per determinare 

tom.circle(raggio)