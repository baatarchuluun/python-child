import turtle

def f():
    turtle.fd(50)
    turtle.lt(60)

screen = turtle.Screen()
screen.onkey(f, "Up")
screen.listen()

turtle.done()