import turtle
import math

t = turtle.Turtle()

def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def circle(t, r):
    circ = 2 * math.pi * r
    n = 50
    length = circ / n
    polygon(t, n, length)


circle(t, 100)