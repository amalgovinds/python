from turtle import Turtle
t=Turtle()
def ploygon(n):
    for count in range(n):
        t.forward(10)
        t.left(360/n)
x=int(input('Enter number of faces of polygo\n')) 
ploygon(x)