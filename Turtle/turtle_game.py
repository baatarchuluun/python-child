import turtle
import random

t1 = turtle.Turtle()
t1.up()
t1.goto(-300, 100)
t1.down()
t1.shape("turtle")
t1.color("red")

t2 = turtle.Turtle()
t2.up()
t2.goto(-300, -100)
t2.down()
t2.shape("turtle")
t2.color("green")

t1_x = -300
t2_x = -300
while True:
    t1_score = random.randit(1, 6)
    t2_score = random.randit(1, 6)
    t1_x += t1_score * 10
    t2_x += t2_score * 10
    t1.forward(t1_score * 10)
    t2.forward(t2_score * 10)
    if (t1_x > 300):
        t1.write("Player 1 have won")
        break
    if (t2_x > 300):
        t2.write("Player 2 have won")
        break

turtle.done()