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
house = drawpad.create_rectangle(200,150,600,550,fill = 'red')

#The roof
roof1 = drawpad.create_line(200,150,400,40)
roof2 = drawpad.create_line(400,40,600,150)

#The door
door = drawpad.create_rectangle(350,400,450,550,fill = 'white')

#Four windows (1 = top left, 2 = bottom left, 3 = top right, 4 = bottom right) (7x7)
window1 = drawpad.create_rectangle(240,230,310,300,fill = 'white')
window2 = drawpad.create_rectangle(240,400,310,470,fill = 'white')
window3 = drawpad.create_rectangle(490,230,560,300,fill = 'white')
window4 = drawpad.create_rectangle(490,400,560,470,fill = 'white')

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
grass = drawpad.create_rectangle(0,550,800,600,fill = 'green')

root.mainloop()
