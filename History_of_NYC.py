# Mode
app.mode = 'Main'

# Background:
Rect(0, 0, 400, 400, fill = gradient('lightBlue', 'royalBlue', 'darkBlue', start = 'top'))
Rect(5,60,390,330, border = 'black', fill = 'white')

# Buttons:
history_ny_button = Rect(5, 5, 130, 50, border = 'black', fill = 'white')
Label('History of NYC',70, 30)

history_boros_button = Rect(135, 5, 130, 50, border = 'black', fill = 'white')
Label('History of Boros',205, 30)

main_screen_button = Rect(265, 5, 130, 50, border = 'black', fill = 'white')
Label('Main Screen',340, 30)

# Main:
Main_Label = Label("Click a Button Above to Explore", 200, 200)

# NY History:
NY_History = Label("History of NYC Data Goes Here", 200, 200, visible = False)

# Boros:
Manhattan = Image('cmu://669630/45464774/Manhattan.jpg', 7, 62,  width = 193, height = 125)
Bronx = Image('cmu://669630/45464927/Bronx.jpg', 200, 62, width = 193, height = 125)
Staten_Island = Image('cmu://669630/45486111/Staten_Island.png',7, 187, width = 128, height = 125)
Brooklyn = Image('cmu://669630/45485890/Brooklyn.png', 135, 187, width = 130, height = 125)
Queens = Image('cmu://669630/45465015/Queens.png', 265, 187, width = 128, height = 125)

Manhattan_Label = Label('Manhattan', 102, 80, size = 20)
Bronx_Label = Label('Bronx', 302, 80, size = 20)
Staten_Island_Label = Label('Staten Island', 71, 205, size = 20)
Brooklyn_Label = Label('Brooklyn', 200, 205, size = 20)
Queens_Label = Label('Queens', 329, 205, size = 20)

# Boro and label groups:
boros = Group(Manhattan,Bronx, Queens, Staten_Island, Brooklyn)
boro_labels = Group(Manhattan_Label, Bronx_Label, Staten_Island_Label, Brooklyn_Label, Queens_Label)

# Initialize boros visibility to False and opacity to 10:
boros.visible = False
boro_labels.visible = False
boros.opacity = 50
 
# Data Display:       
data = Label('', 200, 350, size = 10)

# Boro Data
Manhattan.data = 'History of Manhattan Data Goes Here'
Bronx.data = 'History of the Bronx Data Goes Here'
Queens.data = 'History of Queens Data Goes Here'
Staten_Island.data = 'History of Staten Island Data Goes Here'
Brooklyn.data = 'History of Brooklyn Data Goes Here'

def history(location, x, y):
    if location == 'NY':
        app.mode = 'NY'
        Main_Label.visible = False
        boros.visible = False
        boro_labels.visible = False
        data.visible = False
        NY_History.visible = True
    
    elif location == 'Boros':
        app.mode = 'Boros'
        NY_History.visible = False
        Main_Label.visible = False
        boros.visible = True
        boro_labels.visible = True
        data.visible = True
        boros.opacity = 50
        for boro in boros:
            if boro.hits(x, y):
                boro.opacity = 100
                data.value = boro.data
                
    if location == 'Main':
        app.mode = 'Main'
        boros.visible = False
        boro_labels.visible = False
        data.visible = False
        NY_History.visible = False
        Main_Label.visible = True
        
def onMousePress(mouseX, mouseY):
    if history_ny_button.hits(mouseX, mouseY):
        history('NY', mouseX, mouseY)
    elif main_screen_button.hits(mouseX, mouseY):
        history('Main', mouseX, mouseY)
    elif history_boros_button.hits(mouseX, mouseY) or app.mode == 'Boros':
        history('Boros', mouseX, mouseY)
    
  
