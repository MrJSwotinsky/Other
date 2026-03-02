# Underwater Bacground:
app.red_1 = 135
app.green_1 = 206
app.blue_1 = 250
app.red_2 = 0
app.green_2 = 0
app.blue_2 = 255
ocean = Rect(0,0,400,400, fill = gradient(rgb(app.red_1,app.green_1,app.blue_1), rgb(app.red_2,app.green_2,app.blue_2), start = 'top'))

# Fish
Fish = Polygon(400,100,420,80,440,80,455,95,470,80,470,120,455,105,440,120,420,120, fill = rgb(5, 250, 210))
Fish_Eye = Circle(416,96,4)

# Face (No eyes - Eyes included w/mask):
Circle(200, 200,100, fill = 'yellow')
Circle(200, 190, 15)
Oval(200, 230, 100, 30)
Rect(150, 215, 100, 15, fill = 'yellow')

# Mask & Eyes:
Line(112, 150, 150, 162, fill = 'darkBlue', lineWidth = 20)
Line(288, 150, 250, 162, fill = 'darkBlue', lineWidth = 20)  
Rect(140, 130, 120, 60, fill = 'lightYellow', border = 'blue')
Left_Eye = Circle(175, 160, 15)
Right_Eye = Circle(225, 160, 15)

# Regulator:
Oval(130, 220, 150, 50, border = 'darkBlue', borderWidth = 8, fill = None, rotateAngle = 20)
Rect(110, 190, 75,40, fill = 'yellow')
Circle(120, 192, 20, fill = 'yellow')
Star(200, 240, 25, 10, fill = 'darkBlue', roundness = 90)
Label('SCUBA', 200, 232, font = 'montserrat', size = 10, fill = 'white', bold = True)
Label('Gear', 200, 245, font = 'caveat', size = 20, fill = 'white', italic = True)

# Bubbles
Bubble_1 = Circle(240, 220, 8, fill = 'lightBlue', border = 'blue', borderWidth = 1, opacity = 50)
Bubble_2 = Circle(235, 200, 3, fill = 'lightBlue', border = 'blue', borderWidth = 1, opacity = 50)
Bubble_3 = Circle(260, 190, 15, fill = 'lightBlue', border = 'blue', borderWidth = 1, opacity = 50)
Bubble_4 = Circle(280, 150, 12, fill = 'lightBlue', border = 'blue', borderWidth = 1, opacity = 50)
Bubble_5 = Circle(237, 125, 18, fill = 'lightBlue', border = 'blue', borderWidth = 1, opacity = 50)
Bubble_6 = Circle(260, 110, 6, fill = 'lightBlue', border = 'blue', borderWidth = 1, opacity = 50)
Bubble_7 = Circle(265, 80, 10, fill = 'lightBlue', border = 'blue', borderWidth = 1, opacity = 50)
Bubble_8 = Circle(290, 13, 12, fill = 'lightBlue', border = 'blue', borderWidth = 1, opacity = 50)
Bubble_9 = Circle(240, 40, 20, fill = 'lightBlue', border = 'blue', borderWidth = 1, opacity = 50)
bubbles = Group(Bubble_1, Bubble_2, Bubble_3, Bubble_4, Bubble_5, Bubble_6, Bubble_7, Bubble_8, Bubble_9)

#def onKeyPress(space):
def onMousePress(mouseX, MouseY):
    Fish.centerX -= 10
    Fish_Eye.centerX -=10
    for bubble in bubbles:
        bubble.radius += .15
    app.red_1 -= 2
    app.green_1 -= 3
    app.blue_1 -= 3
    app.blue_2 -= 3
    ocean.fill = gradient(rgb(app.red_1,app.green_1,app.blue_1), rgb(app.red_2,app.green_2,app.blue_2), start = 'top')
