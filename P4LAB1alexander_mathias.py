# Alexander Mathias
# 3/20/2025
# P4Lab1
# Learning turtle graphics and loops

import turtle
# Create drawing window
win = turtle.Screen()
# Creat turtle object
timmy = turtle.Turtle()

# Get some attributes
timmy.pensize(7)
timmy.pencolor('red')
timmy.shape('turtle')
win.bgcolor('black')




#Traingle
for i in range(3):
    timmy.forward(150)
    timmy.left(120)


# Square
side_num = 0

while side_num <= 3:
    timmy.forward(150)
    timmy.right(90)
    side_num += 1




# Keeps the window open when drawing (keep at the bottom of code)
win.mainloop()