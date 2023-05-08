import turtle

def draw_rect(side):
    side1 = side
    for i in range(4): # 0, 1, 2, 3; 0, 1 -> side, 2, 3 -> side + 20
        if i > 1: side1 = side + 20
        turtle.forward(side1)
        turtle.stamp()
        turtle.right(90)
    
turtle.speed(2)
for i in range(5):
    draw_rect(100 + 40 * i)
turtle.done()