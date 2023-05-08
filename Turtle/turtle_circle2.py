import turtle
def draw_circle(rad, i):
    turtle.up()
    turtle.goto(0, -50 + (-20 * (i - 1)))
    turtle.down()

    turtle.circle(rad)
    
for i in range(1, 6):
    draw_circle(50 + 20*(i - 1), i)

turtle.done()