# ------------------------ #
# Costruzione del trapezio #
# ------------------------ #
import turtle

tom = turtle.Turtle()
tom.shape('turtle')

h  =  90 # altezza
b1 = 200 # base maggiore
b2 = 160 # base minore

# 'm' è la proiezione di un lato obliquo sulla base maggiore il cui
# valore deve essere minore della differenza delle due basi
# 'n' è la proiezione dell'altro lato obliquo sulla base maggiore
m  =  25
n  = b1 - b2 - m

# Vertici del trapezio espressi in termini di coordinate
puntoA = (0,0)
puntoB = (b1,0)
puntoC = (m+b2,h)
puntoD = (m,h)

tom.goto(puntoB)
tom.goto(puntoC)
tom.goto(puntoD)
tom.goto(puntoA)
tom.hideturtle()