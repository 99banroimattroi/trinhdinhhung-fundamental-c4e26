from turtle import *

colors = ['red', 'blue', 'brown', 'yellow', 'grey']

n=3

for i in range(len(colors)):

    for j in range(n):

        pencolor(colors[n-3])
        forward(100)
        left(180-((n-2)*180)/n)

    n+=1

done()