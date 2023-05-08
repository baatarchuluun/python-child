# import package
import turtle
  
  
# set direction at 0
# angle using seth
turtle.seth(0)
  
# motion
turtle.forward(80)
turtle.write("East")
  
# back to home
turtle.home()
  
# set direction at 90
# angle using sethading
turtle.setheading(90)
  
# motion
turtle.forward(80)
turtle.write("North")
  
# back to home
turtle.home()
  
# set direction at 180
# angle using seth
turtle.seth(180)
  
# motion
turtle.forward(80)
turtle.write("West",align="right")
  
# back to home
turtle.home()
  
# set direction at 270
# angle using setheading
turtle.setheading(270)
  
# motion
turtle.forward(80)
turtle.write("South")
  
# hide the turtle
turtle.ht()