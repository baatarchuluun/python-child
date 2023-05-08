import turtle
t = turtle.Turtle()
t.fillcolor("red")
t.begin_fill()
for i in range(4):
  t.forward(200)
  t.right(90)  
t.end_fill()

t.up()
t.goto(-200, 100)
t.down()
t.fillcolor("green")
t.begin_fill()
t.circle(100)
t.end_fill()
turtle.done()