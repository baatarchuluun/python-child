import turtle

t_screen = turtle.Screen()
t_screen.bgcolor("green")
t_screen.title("My turtle")

# курсор
t = turtle.Turtle()
t.color("#00FFFF")
t.forward(200)
t.left(90)

t.fd(200)
t.lt(90)

t.fd(200)
t.lt(90)

t.fd(200)
t.lt(90)

t1 = turtle.Turtle()
t1.setx(-100)
t1.color("red")
t1.circle(100)

turtle.done()