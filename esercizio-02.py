# ------------------------- #
# Baricentro di un quadrato #
# ------------------------- #
import turtle
from math import sqrt 

tom = turtle.Turtle()
tom.shape('turtle')

lato = 200

# ------------------------------------------------- #
# 'def' introduce una funzione dal nome quadrato(). # 
# La funzione accetta due valori in ingresso:       #
# - il nome della tartaruga 'n'                     #
# - la lunghezza del lato 'l'                       #
# e restituisce il disegno del quadrato.            #
# ------------------------------------------------- #
def quadrato(n, l):
    for _ in range(4):
        n.forward(l)
        n.left(90)
        
quadrato(tom, lato)

# La lunghezza della diagonale di un quadrato è 
# data dal prodotto del lato per la radice di 2
diagonale = lato * sqrt(2) 

tom.penup()

tom.left(45)
# Il baricentro è nel punto medio
# della diagonale del quadrato
tom.forward(diagonale / 2)

tom.down()
tom.pencolor('red')
tom.dot(10)
tom.hideturtle() # Nasconde la tartaruga