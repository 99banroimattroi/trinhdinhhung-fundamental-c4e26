from turtle import *

speed(0)

color('blue')
left(60)
for i in range(2):
    forward(100)
    right(120)
forward(100)

color('red')
right(90)
for i in range(4):
    forward(100)
    right(90)

color('blue')
left(18)
for i in range(4):
    forward(100)
    right(72)

color('red')
right(120)
for i in range(5):
    forward(100)
    left(60)

mainloop()