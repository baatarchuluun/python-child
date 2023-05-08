import turtle
def draw_circle(rad):
    turtle.up()
    turtle.goto(0, -rad)
    turtle.down()
    turtle.circle(rad)

turtle.speed(10)
for i in range(5):
    draw_circle(50 + 20*i)
turtle.done()