# corona
from turtle import *

color('green')
bgcolor('black')
speed(11)
hideturtle()
penup()
goto(0, 150)
pendown()
b = 0
while b < 220:
    right(b)
    forward(b * 3)
    b += 1

mainloop()
