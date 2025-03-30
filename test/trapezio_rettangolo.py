# ----------------------------------- #
# Costruzione del trapezio rettangolo #
# ----------------------------------- #
import turtle

tom = turtle.Turtle()
tom.shape('turtle')

b1 = 180 # Base maggiore
b2 = 100 # Base minore
h  =  80 # altezza
x = b1-b2

# A, B, C, D sono le coordinate dei vertici del trapezio
A = (0,0)
B = (b1,0)
C = (b2,h)
D = (0,h)

# Costruzione del trapezio isoscele...
tom.goto(A)
tom.goto(B)
tom.goto(C)
tom.goto(D)
tom.goto(A)

tom.hideturtle()

