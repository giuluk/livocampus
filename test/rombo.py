# ----------------------- #
# Costruzione di un rombo #
# (versione "avanzata")   #
# ----------------------- #
import turtle

tom = turtle.Turtle()
tom.shape('turtle')

def rombo(nome, lato, angolo):
    # Questo serve a "raddrizzare" il rombo
    nome.left((180-angolo) / 2)
    # Questo 'if' serve a escludere che possano essere
    # immessi valori dell'angolo non consentiti
    if angolo < 180 and angolo > 0 and angolo != 90:
        for i in range(4):
            nome.forward(lato)
            if i % 2 != 0:
                nome.left(180-angolo)
            else:
                nome.left(angolo)
    else:
        quit()
            
rombo(tom, 150, 40)
tom.hideturtle()