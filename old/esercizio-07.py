# ------------------------------- #
# Costruzione del parallelogramma #
# ------------------------------- #
import turtle

tom = turtle.Turtle()
tom.shape('turtle')

lato1  = 200
lato2  = 150
angolo = 130

# ---------------------------------------------------------- #
# 'def' introduce una funzione dal nome parallelogramma().   #
# La funzione accetta quattro valori in ingresso:            #
# - il nome della tartaruga 'n'                              #
# - la lunghezza del lato 'l1'                               #
# - la lunghezza del lato 'l2'                               #
# - l'ampiezza di angolo 'ang'                               #
# ---------------------------------------------------------- #
def parallelogramma(n, l1, l2, ang):
    for _ in range(2):
        n.forward(l1)
        n.left(180-ang)
        n.forward(l2)
        n.left(ang)
        
parallelogramma(tom, lato1, lato2, angolo)
tom.hideturtle()
