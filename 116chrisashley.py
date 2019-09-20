#   a116_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic", "arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold", "red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  new_colors=turtle_colors.pop()
  t.fillcolor(new_colors)
  t.pencolor(new_colors)
  my_turtles.append(t)
#  
startx = 0
starty = 0
direction=90
#
for t in my_turtles:
    t.setheading(direction)
    direction=t.heading() + 30
    t.penup()
    t.goto(startx, starty)
    t.pendown()
    t.right(45)     
    t.forward(50)
    startx = t.xcor()  
    starty = t.ycor() 
    


wn = trtl.Screen()
wn.mainloop()