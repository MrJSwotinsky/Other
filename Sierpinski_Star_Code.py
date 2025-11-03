# Import turtle module, generate turtle, set its pen size to 1, and set its tracer to 0:
import turtle
my_turtle = turtle.Turtle()
my_turtle.pensize(.75)
my_turtle.tracer(0)

# Set background color to black:
screen = turtle.Screen()
screen.bgcolor('black')

# Set triangle sidelength and corner points.
# x1, y1 for lower left corner.
# x2, y2 for lower right corner.
# x3, y3 for top corner:
side_length = 240
x1 = -120
y1 = -60
x2 = x1 + side_length
y2 = y1
x3 = x1 + side_length / 2
y3 = y2 + side_length / 2 * 3 ** (1/2)

# Accept turtle, depth, and coordinates of corner points, and generate Sierpinski triangle of depth levels of depth:
def Sierpinski(t, depth, x_1, y_1, x_2, y_2, x_3, y_3):
  
  # Determine midpoints of each side:
  left_midpoint_x = (x_1 + x_3) / 2
  left_midpoint_y = (y_1 + y_3) / 2
  right_midpoint_x = (x_2 + x_3) / 2
  right_midpoint_y = (y_2 + y_3) / 2
  lower_midpoint_x = (x_1 + x_2) / 2
  lower_midpoint_y = (y_1 + y_2) / 2
  
  # Base case:
  if depth == 0:
    pass
  
  # Recursion:
  else:
    # Construct inner triangle:
    t.pu()
    t.setx(left_midpoint_x)
    t.sety(left_midpoint_y)
    t.pd()
    t.goto(right_midpoint_x, right_midpoint_y)
    t.goto(lower_midpoint_x, lower_midpoint_y)
    t.goto(left_midpoint_x, left_midpoint_y)
  
    # Complete upper triangle:
    Sierpinski(t, depth - 1, left_midpoint_x, left_midpoint_y, right_midpoint_x, right_midpoint_y, x_3, y_3)
 
    # Complete lower left triangle:
    Sierpinski(t, depth - 1, x_1, y_1, lower_midpoint_x, lower_midpoint_y, left_midpoint_x, left_midpoint_y)
    
    # Complete lower right triangle:
    Sierpinski(t, depth - 1, lower_midpoint_x, lower_midpoint_y, x_2, y_2, right_midpoint_x,right_midpoint_y)
  
  
# Extend the Sierpinski triangle to a star.
# Accept, turtle, triangle depth, star depth, and coordinates of new triangle to be constructed, 
# and construct a new Sierpinski triangle:
def star(t, triangle_depth, star_depth, x_1, y_1, x_2, y_2, x_3, y_3):
  
  # Set color of star to a gradient transitioning from a purple interior to a yellow exterior:
  t.pencolor(255 - star_depth * 15, 255 - star_depth * 30, 10 + star_depth * 35)  
  
  # Construct triangle border:
  t.pu()
  t.setx(x_1)
  t.sety(y_1)
  t.pd()
  t.goto(x_2, y_2)
  t.goto(x_3, y_3)
  t.goto(x_1, y_1)
  
  # Complete Sierpinski triangle:
  Sierpinski(t, triangle_depth, x_1, y_1, x_2, y_2, x_3, y_3)
  
  # Base case:
  if star_depth == 0:
    pass
  
  # Recurison:
  else:
    # Determine midpoints of each side:
    left_midpoint_x = (x_1 + x_3) / 2
    left_midpoint_y = (y_1 + y_3) / 2
    right_midpoint_x = (x_2 + x_3) / 2
    right_midpoint_y = (y_2 + y_3) / 2
    lower_midpoint_x = (x_1 + x_2) / 2
    lower_midpoint_y = (y_1 + y_2) / 2
    
    # Set new coordniates for triangle to be built on right side of current triangle:
    new_x_1_right = (x_3 + right_midpoint_x) / 2
    new_y_1_right = (y_3 + right_midpoint_y) / 2
    
    new_x_2_right = (x_2 + right_midpoint_x) / 2
    new_y_2_right = (y_2 + right_midpoint_y) / 2
    
    new_x_3_right = (new_x_1_right + new_x_2_right)/2 + (3 ** (1/2)) / 2 * (new_y_1_right - new_y_2_right) 
    new_y_3_right = (new_y_1_right + new_y_2_right)/2 - (3 ** (1/2)) / 2 * (new_x_1_right - new_x_2_right) 

    # Build new triangle on right side of current triangle:
    star(t, triangle_depth, star_depth - 1, new_x_1_right, new_y_1_right, new_x_2_right, new_y_2_right, new_x_3_right, new_y_3_right)
   
    # Set new coordinates for triangle to be built on left side of current triangle:
    new_x_1_left = (x_1 + left_midpoint_x) / 2
    new_y_1_left = (y_1 + left_midpoint_y) / 2
    
    new_x_2_left = (x_3 + left_midpoint_x) / 2
    new_y_2_left = (y_3 + left_midpoint_y) / 2
    
    new_x_3_left = (new_x_1_left + new_x_2_left)/2 + (3 ** (1/2)) / 2 * (new_y_1_left - new_y_2_left) 
    new_y_3_left = (new_y_1_left + new_y_2_left)/2 - (3 ** (1/2)) / 2 * (new_x_1_left - new_x_2_left) 

    # Build new triangle on left side of current triangle:
    star(t, triangle_depth, star_depth - 1, new_x_1_left, new_y_1_left, new_x_2_left, new_y_2_left, new_x_3_left, new_y_3_left)

    # Build the lower triangle in the outermost layer only:
    if star_depth == d:
      # Set new coordinates for triangle to be built on lower side of current triangle:
      new_x_1_lower = (x_2 + lower_midpoint_x) / 2
      new_y_1_lower = (y_2 + lower_midpoint_y) / 2
    
      new_x_2_lower = (x_1 + lower_midpoint_x) / 2
      new_y_2_lower = (y_1 + lower_midpoint_y) / 2
    
      new_x_3_lower = (new_x_1_lower + new_x_2_lower) / 2 + (3 ** (1/2)) / 2 * (new_y_1_lower - new_y_2_lower) 
      new_y_3_lower = (new_y_1_lower + new_y_2_lower) / 2 - (3 ** (1/2)) / 2 * (new_x_1_lower - new_x_2_lower) 

      # Build new triangle on lower side of current triangle:
      star(t, triangle_depth, star_depth - 1, new_x_1_lower, new_y_1_lower, new_x_2_lower, new_y_2_lower, new_x_3_lower, new_y_3_lower)
      
      
# Set star depth:
d = 7

# Generate a "Sierpinski Star" in the center of the canvas with a triangle depth of 5 and a star depth of star_depth:
star(my_turtle, 5, d, x1, y1, x2, y2, x3, y3)

# Send the turtle to top right corner of canvas:
my_turtle.pu()
my_turtle.goto(200,200)

# Display "Sierpinski Star":
turtle.update()
