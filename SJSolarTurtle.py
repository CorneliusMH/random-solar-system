#importing the required modules
import randomSystem
import FNGplanetNames
import turtle
import random
import time
from math import *

system = randomSystem.get_system()

print(system)

print(FNGplanetNames.build_name_table())

sunSource = system['system']["primaryBody"]

size_class_translate = {
    "A":10,
    "B":20,
    "C":30,
    "D":40,
    "E":50,
    "F":60,
    "G":70,
    "H":80,
    "I":90,
    "J":100
}

color_translate = {
    "Earth":'green',
    "Fire":"orange",
    "Air":"cyan",
    "Water":"blue",
    "Liveworld":"purple"
}

screen = turtle.Screen()#creating the screen
screen.bgcolor("pink")
screen.tracer(20)

sun = turtle.Turtle()#turtle object for sun
sun.shape('circle')#shape of sun
sun.color('yellow')#colour of sun


class Planet(turtle.Turtle):
    def __init__(self,name,radius,color,shape='circle'):#initialize function
        super().__init__(shape)
        self.name = name
        self.radius = radius
        self.c = color
        self.color(self.c)
        self.up()
        self.pd()
        self.angle = 0
        self.shape = shape
    def move(self):
        x = self.radius*cos(self.angle) # Angle in radians
        y = self.radius*sin(self.angle) 
        self.goto(sun.xcor()+x,sun.ycor()+y)

# making planets

planets = system["planets"]

print (planets)


#adding planets to a list

myList = []
myAngle = []

distance = 1

for i in range(planets['number']):
    print ("Planet",i,planets[i])
    thisPlanet = planets[i].copy()
    planetStats = thisPlanet['bodyStats']
    name = i #thisPlanet['name']
    size = size_class_translate[planetStats['size class']]
    color = color_translate[thisPlanet['type']]
    distance += thisPlanet['distance']
    radius = distance*10
    shape = planetStats['shape']
    outPlanet = Planet(name,radius,color,shape)
    print(outPlanet)

    # Angle fun!
    if thisPlanet['motion'] == 'Clockwise orbit':
        angle = -1*random.randrange(5,40)/500
    elif thisPlanet['motion'] == 'Counter-clockwise orbit':
        angle = random.randrange(5,40)/500
    elif thisPlanet['motion'] == 'No movement, planets are fixed in place.':
        angle = 0
        outPlanet.angle = random.randrange(0,360)
    elif thisPlanet['motion'] == 'Random movement within the system, no predefined orbits.':
        angle = 0
        outPlanet.angle = random.randrange(0,360)

    myAngle.append(angle)
    myList.append(outPlanet)

print(myList)
print(myAngle)

while True:#while statement
    screen.update()#updating the screen
    for i in myList:
        i.move()#moving the elements of the list
        i.angle += myAngle[i.name]

    # Increase the angle by 0.0x radians
    
    # mercury.angle +=    0.050
    # venus.angle +=      0.030
    # earth.angle +=      0.010
    # mars.angle +=       0.007

    # jupiter.angle +=    0.020
    # saturn.angle +=     0.018
    # uranus.angle +=     0.016
    # neptune.angle +=    0.005
    
    