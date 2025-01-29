# ----------------------- #
# Costruzione di un rombo #
# (versione semplificata) #
# ----------------------- #
import turtle

tom = turtle.Turtle()
tom.shape('turtle')

# -------------------------------------------- #
# Il rombo non è un poligono regolare perché,  #
# sebbene la lunghezza dei lati sia la stessa, #
# solo gli angoli opposti hanno la stessa      #
# ampiezza. In generale, in un quadrilatero la #
# somma delle ampiezze degli angoli interni è  #
# 360°, di conseguenza gli angoli adiacenti di #
# ogni lato del rombo sono supplementari       #
# ovvero la somma delle loro ampiezze è pari a #
# quella di un angolo piatto (180°).           #
# -------------------------------------------- #
lato = 200
angolo = 80

tom.left((180-angolo) / 2) # Serve per 'raddrizzare' il rombo

for _ in range(2):
    tom.forward(lato)
    tom.left(angolo)
    tom.forward(lato)
    tom.left(180-angolo) # Gli angoli adiacenti di ogni lato sono supplementari


tom.hideturtle()