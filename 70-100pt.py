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
column1a = drawpad.create_line(250,150,250,175)
column1b = drawpad.create_line(250,200,250,225)
column1c = drawpad.create_line(250,300,250,325)
column1d = drawpad.create_line(250,350,250,375)
column1e = drawpad.create_line(250,470,250,475)
column1f = drawpad.create_line(250,500,250,525)
column2a = drawpad.create_line(300,150,300,175)
column2b = drawpad.create_line(300,200,300,225)
column2c = drawpad.create_line(300,300,300,325)
column2d = drawpad.create_line(300,350,300,375)
column2e = drawpad.create_line(300,470,300,475)
column2f = drawpad.create_line(300,500,300,525)
column3a = drawpad.create_line(350,150,350,175)
column3b = drawpad.create_line(350,200,350,225)
column3c = drawpad.create_line(350,250,350,275)
column3d = drawpad.create_line(350,300,350,325)
column3e = drawpad.create_line(350,350,350,375)
column4a = drawpad.create_line(400,150,400,175)
column4b = drawpad.create_line(400,200,400,225)
column4c = drawpad.create_line(400,250,400,275)
column4d = drawpad.create_line(400,300,400,325)
column4e = drawpad.create_line(400,350,400,375)
column5a = drawpad.create_line(450,150,450,175)
column5b = drawpad.create_line(450,200,450,225)
column5c = drawpad.create_line(450,250,450,275)
column5d = drawpad.create_line(450,300,450,325)
column5e = drawpad.create_line(450,350,450,375)
column6a = drawpad.create_line(500,150,500,175)
column6b = drawpad.create_line(500,200,500,225)
column6c = drawpad.create_line(500,300,500,325)
column6d = drawpad.create_line(500,350,500,375)
column6e = drawpad.create_line(500,470,500,475)
column6f = drawpad.create_line(500,500,500,525)
column7a = drawpad.create_line(550,150,550,175)
column7b = drawpad.create_line(550,200,550,225)
column7c = drawpad.create_line(550,300,550,325)
column7d = drawpad.create_line(550,350,550,375)
column7e = drawpad.create_line(550,470,550,475)
column7f = drawpad.create_line(550,500,550,525)
shifted1a = drawpad.create_line(225,175,225,200)
shifted1b = drawpad.create_line(225,225,225,250)
shifted1c = drawpad.create_line(225,275,225,300)
shifted1d = drawpad.create_line(225,325,225,350)
shifted1e = drawpad.create_line(225,375,225,400)
shifted1f = drawpad.create_line(225,425,225,450)
shifted1g = drawpad.create_line(225,475,225,500)
shifted1h = drawpad.create_line(225,525,225,550)
shifted2a = drawpad.create_line(275,175,275,200)
shifted2b = drawpad.create_line(275,225,275,250)
shifted2c = drawpad.create_line(275,275,275,300)
shifted2d = drawpad.create_line(275,325,275,350)
shifted2e = drawpad.create_line(275,375,275,400)
shifted2f = drawpad.create_line(275,425,275,450)
shifted2g = drawpad.create_line(275,475,275,500)
shifted2h = drawpad.create_line(275,525,275,550)
shifted3a = drawpad.create_line(325,175,325,200)
shifted3b = drawpad.create_line(325,225,325,250)
shifted3c = drawpad.create_line(325,275,325,300)
shifted3d = drawpad.create_line(325,325,325,350)
shifted3e = drawpad.create_line(325,375,325,400)
shifted3f = drawpad.create_line(325,425,325,450)
shifted3g = drawpad.create_line(325,475,325,500)
shifted3h = drawpad.create_line(325,525,325,550)
shifted4a = drawpad.create_line(375,175,375,200)
shifted4b = drawpad.create_line(375,225,375,250)
shifted4c = drawpad.create_line(375,275,375,300)
shifted4d = drawpad.create_line(375,325,375,350)
shifted4e = drawpad.create_line(375,375,375,400)
shifted5a = drawpad.create_line(425,175,425,200)
shifted5b = drawpad.create_line(425,225,425,250)
shifted5c = drawpad.create_line(425,275,425,300)
shifted5d = drawpad.create_line(425,325,425,350)
shifted5e = drawpad.create_line(425,375,425,400)
shifted6a = drawpad.create_line(475,175,475,200)
shifted6b = drawpad.create_line(475,225,475,250)
shifted6c = drawpad.create_line(475,275,475,300)
shifted6d = drawpad.create_line(475,325,475,350)
shifted6e = drawpad.create_line(475,375,475,400)
shifted6f = drawpad.create_line(475,425,475,450)
shifted6g = drawpad.create_line(475,475,475,500)
shifted6h = drawpad.create_line(475,525,475,550)
shifted7a = drawpad.create_line(525,175,525,200)
shifted7b = drawpad.create_line(525,225,525,250)
shifted7c = drawpad.create_line(525,275,525,300)
shifted7d = drawpad.create_line(525,325,525,350)
shifted7e = drawpad.create_line(525,375,525,400)
shifted7f = drawpad.create_line(525,425,525,450)
shifted7g = drawpad.create_line(525,475,525,500)
shifted7h = drawpad.create_line(525,525,525,550)
shifted8a = drawpad.create_line(575,175,575,200)
shifted8b = drawpad.create_line(575,225,575,250)
shifted8c = drawpad.create_line(575,275,575,300)
shifted8d = drawpad.create_line(575,325,575,350)
shifted8e = drawpad.create_line(575,375,575,400)
shifted8f = drawpad.create_line(575,425,575,450)
shifted8g = drawpad.create_line(575,475,575,500)
shifted8h = drawpad.create_line(575,525,575,550)


root.mainloop()
