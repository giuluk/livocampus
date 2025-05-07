# --------------------------------- #
# Costruzione del trapezio isoscele #
# --------------------------------- #
import turtle

tom = turtle.Turtle()
tom.shape('turtle')

b1 = 180 # Base maggiore
b2 = 100 # Base minore
h  =  80 # altezza
x = (b1-b2) / 2

# A, B, C, D sono le coordinate dei vertici del trapezio
A = (0,0)
B = (b1,0)
C = (b2+x,h)
D = (x,h)
H = (x,0)

# Costruzione del trapezio isoscele...
tom.goto(A)
tom.goto(B)
tom.goto(C)
tom.goto(D)
tom.goto(A)

# ... e della sua altezza
tom.penup()
tom.goto(H)
tom.left(90)
tom.pendown()
tom.pencolor('red')
tom.forward(h)

tom.hideturtle()
