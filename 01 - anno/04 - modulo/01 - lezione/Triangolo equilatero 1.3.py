# -------------------------- #
# Triangolo equilatero v.1.3 #
# -------------------------- #
import turtle

# Assegnazioni delle variabili
tom = turtle.Turtle()

# Attributi della tartaruga
tom.shape('turtle')

# Azioni della tartaruga
# ----------------------------------------------------- #
# 'def' introduce una funzione dal nome triangolo_eq(). # 
# La funzione accetta due valori in ingresso:           #
# - il nome della tartaruga 'nome'                      #
# - la lunghezza del lato 'lato'                        #
# e restituisce il disegno del triangolo equilatero.    #
# ----------------------------------------------------- #
def triangolo_eq(nome, lato):
    for _ in range(3):
        nome.forward(lato)
        nome.left(120)
        
triangolo_eq(tom, 150) # Chiamata della funzione 'triangolo_eq()'