# ------------------------- #
# Baricentro di un quadrato #
# ------------------------- #
import turtle

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
        n.right(90)

# Costruzione del "tetto"
tom.left(60)
tom.forward(lato)
tom.right(120)
tom.forward(lato)
tom.right(30)

quadrato(tom, 200)
tom.hideturtle()

# ----------------------------------------------- #
# La parte di codice che segue serve a  disegnare #
# una porta e non necessaria per soddisfare le    #
# richieste dell'esercizio                        #
# ----------------------------------------------- #
tom.forward(200)
tom.right(90)
tom.forward(200/3)
tom.right(90)
tom.forward(50)
tom.circle(200/6, 180)
tom.forward(50)