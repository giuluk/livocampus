import turtle

t = turtle.Turtle()
t.shape('turtle')

# Questa funzione costruisce un quadrato
def quadrato(tartaruga, lato):
    for _ in range(4):
        tartaruga.forward(lato)
        tartaruga.right(90)
        
t.left(60)
t.forward(200)
t.right(120)
t.forward(200)
t.right(30)

quadrato(t, 200)

t.forward(200)
t.right(90)
t.forward(200/3)
t.right(90)
t.forward(50)
t.circle(200/6, 180)
t.forward(50)
t.hideturtle()