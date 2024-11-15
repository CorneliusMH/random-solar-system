#importing the required modules
import randomSystem
import FNGplanetNames
import turtle
import random
import time
from math import *

colors = ['cyan','magenta','yellow','green','red','orange','white','grey']

screen = turtle.Screen()#creating the screen
screen.bgcolor("black")

def amorphous_shape(Turtle):
	amorph  = turtle.Shape("compound")

	turtle.begin_poly()
	turtle.circle(2)
	turtle.end_poly()
	randco = colors[random.randrange(0,8)]
	amorph.addcomponent(turtle.get_poly(),randco,randco)

	turtle.penup()
	turtle.right(4)
	turtle.pendown()
	turtle.begin_poly()
	turtle.circle(2)
	turtle.end_poly()
	randco = colors[random.randrange(0,8)]
	amorph.addcomponent(turtle.get_poly(),randco,randco)

	turtle.penup()
	turtle.forward(2)
	turtle.right(2)
	turtle.pendown()
	turtle.begin_poly()
	turtle.circle(2)
	turtle.end_poly()
	randco = colors[random.randrange(0,8)]
	amorph.addcomponent(turtle.get_poly(),randco,randco)

	turtle.penup()
	turtle.right(4)
	turtle.pendown()
	turtle.begin_poly()
	turtle.circle(2)
	turtle.end_poly()
	randco = colors[random.randrange(0,8)]
	amorph.addcomponent(turtle.get_poly(),randco,randco)

	turtle.penup()
	turtle.forward(2)
	turtle.left(8)
	turtle.pendown()
	turtle.begin_poly()
	turtle.circle(2)
	turtle.end_poly()
	randco = colors[random.randrange(0,8)]
	amorph.addcomponent(turtle.get_poly(),randco,randco)

	turtle.penup()
	turtle.forward(2)
	turtle.right(2)
	turtle.pendown()
	turtle.begin_poly()
	turtle.circle(2)
	turtle.end_poly()
	randco = colors[random.randrange(0,8)]
	amorph.addcomponent(turtle.get_poly(),randco,randco)

	turtle.penup()
	turtle.right(4)
	turtle.pendown()
	turtle.begin_poly()
	turtle.circle(2)
	turtle.end_poly()
	randco = colors[random.randrange(0,8)]
	amorph.addcomponent(turtle.get_poly(),randco,randco)

	turtle.penup()
	turtle.forward(2)
	turtle.left(8)
	turtle.pendown()
	turtle.begin_poly()
	turtle.circle(2)
	turtle.end_poly()
	randco = colors[random.randrange(0,8)]
	amorph.addcomponent(turtle.get_poly(),randco,randco)

	turtle.penup()
	turtle.forward(2)
	turtle.right(6)
	turtle.pendown()
	turtle.begin_poly()
	turtle.circle(2)
	turtle.end_poly()
	randco = colors[random.randrange(0,8)]
	amorph.addcomponent(turtle.get_poly(),randco,randco)

	turtle.penup()
	turtle.right(4)
	turtle.pendown()
	turtle.begin_poly()
	turtle.circle(2)
	turtle.end_poly()
	randco = colors[random.randrange(0,8)]
	amorph.addcomponent(turtle.get_poly(),randco,randco)

	turtle.penup()
	turtle.forward(2)
	turtle.left(8)
	turtle.pendown()
	turtle.begin_poly()
	turtle.circle(2)
	turtle.end_poly()
	randco = colors[random.randrange(0,8)]
	amorph.addcomponent(turtle.get_poly(),randco,randco)

	screen.register_shape("Amorphous",amorph)

	turtle.reset()

# magic_marker = turtle.Turtle()
# amorphous_shape(magic_marker)
# magic_marker.hideturtle()

screen.register_shape('cluster.gif')

sun = turtle.Turtle()#turtle object for sun
sun.shape('circle')#shape of sun
sun.color('yellow')#colour of sun


class Planet(turtle.Turtle):
    def __init__(self,name,radius,color):#initialize function
        super().__init__(shape="cluster.gif")
        self.name = name
        self.radius = radius
        self.c = color
        self.color(self.c)
        self.up()
        self.pd()
        self.angle = 0
    def move(self):
        x = self.radius*cos(self.angle) # Angle in radians
        y = self.radius*sin(self.angle) 

        self.goto(sun.xcor()+x,sun.ycor()+y)

dog = Planet('doggg',100,"red")

i = 0
screen.update()
while i < 100000:#while statement
	screen.update()
	dog.move()
	dog.angle +=    0.050
	i += 1

# system = randomSystem.get_system()

# print(json.dumps(system['planets']))