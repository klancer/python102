
#!/usr/bin/env python
from turtle import *
import random


def drawSquare():
    color('blue', 'yellow')
    begin_fill()
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    end_fill()
    done()

def drawCircle():
    color('blue', 'yellow')
    begin_fill()
    circle(100)
    end_fill()
    done()

def drawTriangle():
    color('blue', 'red')
    begin_fill()
    forward(100)
    left(120)
    forward(100)
    left(120)
    forward(100)
    end_fill()
    done()

def drawStar():
    color('blue', 'red')
    begin_fill()
    side = 0
    while side < 5:
        forward(100)
        left(144)
        side += 1
    end_fill()
    done()


def draw8Star():
    color('blue', 'red')
    begin_fill()
    side = 0
    while side < 8:
        forward(100)
        left(135)
        side += 1
    end_fill()
    done()


def draw12Star():
    color('blue', 'red')
    begin_fill()
    side = 0
    while side < 12:
        forward(100)
        left(150)
        side += 1
    end_fill()
    done()

if __name__ == "__main__":
    drawSquare()
    drawCircle()
    drawTriangle()
    drawStar()
    draw8Star()
    draw12Star()



