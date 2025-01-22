# ------------------------------------ #
# Costruzione del triangolo equilatero #
# ------------------------------------ #
import turtle

tom = turtle.Turtle()
tom.shape('turtle')

lato = 200

# ----------------------------------------------------- #
# 'def' introduce una funzione dal nome triangolo_eq(). # 
# La funzione accetta due valori in ingresso:           #
# - il nome della tartaruga 'n'                         #
# - la lunghezza del lato 'l'                           #
# e restituisce il disegno del triangolo equilatero.    #
# ----------------------------------------------------- #
def triangolo_eq(n, l):
    for _ in range(3):
        n.forward(l)
        n.left(120)
        
triangolo_eq(tom, lato)
tom.hideturtle()