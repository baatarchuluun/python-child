# Imports
import turtle
import time
import random


# Score and delay
score = 0
high_score = 0
delay = 0.1


# Set up the screen
wn = turtle.Screen()
wn.title('Snake Game by Arpit')
wn.bgcolor("green")
wn.setup(width=700, height=700)
wn.tracer(0) # Turns off screen updates

# Outline of the playing field
pencil = turtle.Turtle()
pencil.speed(0)
pencil.shape('circle')
pencil.color('black')
pencil.penup()
pencil.hideturtle()
pencil.goto(310,310)
pencil.pendown()
pencil.goto(-310,310)
pencil.goto(-310,-310)
pencil.goto(310,-310)
pencil.goto(310,310)
pencil.penup()

# Snake head
head = turtle.Turtle()
head.speed(0) # 0 is the maximum animation speed of turtle module
head.shape("circle")
head.color('black')
head.penup()
head.goto(0,0)
head.direction = 'stop'

# Snake Food
food = turtle.Turtle()
food.speed(0) # 0 is the maximum animation speed of turtle module
food.shape("square")
food.color('red')
food.penup()
food.goto(0,100)

# Contains information about snake body
segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape('circle')
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 310)
pen.write('Score: 0 High Score: 0', align = 'center', font = ('Courier', 24, 'normal'))

# Function that helps the snake move
def move():
    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
    # Move segment 0 to the head
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
    # Keep the snake moving in the same direction
    if head.direction == 'up':
        head.sety(head.ycor() + 10)
    if head.direction == 'down':
        head.sety(head.ycor() - 10)
    if head.direction == 'left':
        head.setx(head.xcor() - 10)
    if head.direction == 'right':
        head.setx(head.xcor() + 10)

# Functions that move snake in response to keyboard keys
def go_up():
    if head.direction != 'down':
        head.direction = 'up'
def go_down():
    if head.direction != 'up':
        head.direction = 'down'
def go_left():
    if head.direction != 'right':
        head.direction = 'left'
def go_right():
    if head.direction != 'left':
        head.direction = 'right'

### Keyboard bindings
wn.listen()
wn.onkeypress(go_up, 'Up')
wn.onkeypress(go_down, 'Down')
wn.onkeypress(go_left, 'Left')
wn.onkeypress(go_right, 'Right')

while True:
    # Updates the window repeatedly
    wn.update()

    
    move()

    # Delay so that we can see things move
    time.sleep(delay)