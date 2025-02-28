# -------------------------- #
# Triangolo equilatero v.1.4 #
# -------------------------- #
import turtle

# Assegnazioni delle variabili
tom = turtle.Turtle()

# Attributi della tartaruga
tom.shape('turtle')
tom.pensize(3)
tom.fillcolor('lightblue')
tom.pencolor('red')
tom.speed(1)
#tom.pen(pensize=3, fillcolor='lightblue', pencolor='red', speed=1) <--- Attributi in un unica soluzione

# Azioni della tartaruga
def triangolo_eq(nome, lato):
    for _ in range(3):
        nome.forward(lato)
        nome.left(120)

tom.begin_fill()
triangolo_eq(tom, 150) # Chiamata della funzione 'triangolo_eq()'
tom.end_fill()