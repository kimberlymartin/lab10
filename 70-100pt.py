##########################################
#                                        #
#             Draw a house!              #
#                                        #
##########################################

# Use create_line(), create_rectangle() and create_oval() to make a 
# drawing of a house using the tKinter Canvas widget.

# 70pt: House outline (roof and the house)
# 80pt: Square windows and a door
# 90pt: A door handle plus a chimney!
# 100pt: Green grass on the ground and a red house!

# Minus 5pts if your code has no comments
# Minus 10pts if you only commit once to github

from Tkinter import *
root = Tk()

# Create the canvas widget
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=1)

# Insert your code here to draw the house!

#The house outline + red
house = drawpad.create_rectangle(200,150,600,550,fill = '#B20000')

#The roof
roof1 = drawpad.create_line(200,150,400,40)
roof2 = drawpad.create_line(400,40,600,150)

#The door
door = drawpad.create_rectangle(350,400,450,550,fill = '#804C33')

#Four windows (1 = top left, 2 = bottom left, 3 = top right, 4 = bottom right) (7x7)
window1 = drawpad.create_rectangle(240,230,310,300,fill = '#CCFFFF')
window2 = drawpad.create_rectangle(240,400,310,470,fill = '#CCFFFF')
window3 = drawpad.create_rectangle(490,230,560,300,fill = '#CCFFFF')
window4 = drawpad.create_rectangle(490,400,560,470,fill = '#CCFFFF')

#The window panes
pane1a = drawpad.create_line(275,230,275,300)
pane1b = drawpad.create_line(240,265,310,265)
pane2a = drawpad.create_line(275,400,275,470)
pane2b = drawpad.create_line(240,435,310,435)
pane3a = drawpad.create_line(525,230,525,300)
pane3b = drawpad.create_line(490,265,560,265)
pane4a = drawpad.create_line(525,400,525,470)
pane4b = drawpad.create_line(490,435,560,435)

#The door handle (2x2)
handle = drawpad.create_oval(420,470,440,490,fill = 'yellow')

#The chimney (1 = left side, 2 = right side, 3 = top)
chimney1 = drawpad.create_line(250,30,250,123)
chimney2 = drawpad.create_line(310,30,310,90)
chimney3 = drawpad.create_line(250,30,310,30)

#The green grass
grass = drawpad.create_rectangle(0,550,800,600,fill = '#2E782E')

#Bricks
layer1 = drawpad.create_line(200,175,600,175)
layer2 = drawpad.create_line(200,200,600,200)
layer3 = drawpad.create_line(200,225,600,225)
layer4a = drawpad.create_line(200,250,240,250)
layer4b = drawpad.create_line(310,250,490,250)
layer4c = drawpad.create_line(560,250,600,250)
layer5a = drawpad.create_line(200,275,240,275)
layer5b = drawpad.create_line(310,275,490,275)
layer5c = drawpad.create_line(560,275,600,275)
layer6 = drawpad.create_line(200,300,600,300)
layer7 = drawpad.create_line(200,325,600,325)
layer8 = drawpad.create_line(200,350,600,350)
layer9 = drawpad.create_line(200,375,600,375)
layer10 = drawpad.create_line(200,400,600,400)
layer11a = drawpad.create_line(200,425,240,425)
layer11b = drawpad.create_line(310,425,350,425)
layer11c = drawpad.create_line(450,425,490,425)
layer11d = drawpad.create_line(560,425,600,425)
layer12a = drawpad.create_line(200,450,240,450)
layer12b = drawpad.create_line(310,450,350,450)
layer12c = drawpad.create_line(450,450,490,450)
layer12d = drawpad.create_line(560,450,600,450)
layer13a = drawpad.create_line(200,475,350,475)
layer13b = drawpad.create_line(450,475,600,475)
layer14a = drawpad.create_line(200,500,350,500)
layer14b = drawpad.create_line(450,500,600,500)
layer15a = drawpad.create_line(200,525,350,525)
layer15b = drawpad.create_line(450,525,600,525)


root.mainloop()
