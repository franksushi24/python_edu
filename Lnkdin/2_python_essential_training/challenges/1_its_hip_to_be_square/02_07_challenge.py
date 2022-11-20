# CHALLENGE
# 1. Run Scribe
# 2. Write a function that draws a square
# 3. Pass in the size of the square
# 4. def drawSquare(size):

import os
import time
from termcolor import colored

class Canvas:

# this sets attributes or characteristics to Canvas
    def __init__(self, width, height): 
        self._x = width #this is a variable for width
        self._y = height #this is a variable for height
        self._canvas = [[' ' for y in range(self._y)] for x in range(self._x)] #this sets the boundaries units for x and y? 
        #I belive the brackets indicate a list of y and x length. but now x and y are their own variables
        
#these are all functions NOT ATTRIBUTES
    def hitsWall(self, point): #this function hitsWall is using variables self and point. 
        return point[0] < 0 or point[0] >= self._x or point[1] < 0 or point[1] >= self._y

    def setPos(self, pos, mark):
        self._canvas[pos[0]][pos[1]] = mark

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print(self):
        self.clear()
        for y in range(self._y):
            print(' '.join([col[y] for col in self._canvas]))

class TerminalScribe:
    def __init__(self, canvas):
        self.canvas = canvas
        self.trail = '.'
        self.mark = '*'
        self.framerate = 0.2
        self.pos = [0, 0]

    def up(self):
        pos = [self.pos[0], self.pos[1]-1]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def down(self):
        pos = [self.pos[0], self.pos[1]+1]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def right(self):
        pos = [self.pos[0]+1, self.pos[1]]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def left(self):
        pos = [self.pos[0]-1, self.pos[1]]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)
    
    def drawSquare(self, size):
        i = 0
        while i < size:
            self.right()
            i = i + 1
        i = 0
        while i < size:
            self.down()
            i = i + 1
        i = 0
        while i < size:
            self.left()
            i = i + 1
        i = 0
        while i < size:
            self.up()
            i = i + 1

    def draw(self, pos):
        self.canvas.setPos(self.pos, self.trail)
        self.pos = pos
        self.canvas.setPos(self.pos, colored(self.mark, 'red'))
        self.canvas.print()
        time.sleep(self.framerate)

canvas = Canvas(30, 30)
scribe = TerminalScribe(canvas)

scribe.drawSquare(20)


