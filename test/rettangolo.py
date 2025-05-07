# -------------------------- #
# Costruzione del rettangolo #
# -------------------------- #
import turtle

tom = turtle.Turtle()
tom.shape('turtle')

lato1 = 250
lato2 = 150

# ----------------------------------------------------- #
# 'def' introduce una funzione dal nome rettangolo().   #
# La funzione accetta due valori in ingresso:           #
# - il nome della tartaruga 'n'                         #
# - la lunghezza del lato 'l1'                          #
# - la lunghezza del lato 'l2'                          #
# e restituisce il disegno del rettangolo oppure quello #
# del quadrato se i lati hanno la stessa lunghezza.     #
# ----------------------------------------------------- #
def rettangolo(n, l1, l2):
    for _ in range(2):
        n.forward(l1)
        n.left(90)
        n.forward(l2)
        n.left(90)

# Costruzione del rettangolo...
rettangolo(tom, lato1, lato2)

# ... e delle sue diagonali
tom.pencolor('red')
tom.goto(lato1, lato2)
tom.penup()
tom.goto(lato1,0)
tom.pendown()
tom.goto(0,lato2)
tom.hideturtle()

