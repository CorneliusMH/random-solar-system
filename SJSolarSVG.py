#importing the required modules
import randomSystem
import FNGplanetNames
import turtle
import random
import time
import svglib
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

