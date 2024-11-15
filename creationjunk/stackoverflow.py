from turtle import Turtle, Screen, Shape, tracer, update

#### Monkey patch Turtle object to allow compound shapes to be dragged. ####
####### Based on patch by Ingrid: https://bugs.python.org/issue16428 #######

def onclick(self, fun, btn=1, add=None):
    if (self.turtle._type == 'compound'):
        for i in self.turtle._item:
            self.screen._onclick(i, fun, btn, add)
    else:
        self.screen._onclick(self.turtle._item, fun, btn, add)
    self._update()

Turtle.onclick = onclick

def onrelease(self, fun, btn=1, add=None):
    if (self.turtle._type == 'compound'):
        for i in self.turtle._item:
            self.screen._onrelease(i, fun, btn, add)
    else:
        self.screen._onrelease(self.turtle._item, fun, btn, add)
    self._update()

Turtle.onrelease = onrelease

def ondrag(self, fun, btn=1, add=None):
    if (self.turtle._type == 'compound'):
        for i in self.turtle._item:
            self.screen._ondrag(i, fun, btn, add)
    else:
        self.screen._ondrag(self.turtle._item, fun, btn, add)

Turtle.ondrag = ondrag

############################ End Monkey patch. #############################

def simple_polygon(turtle):

    turtle.begin_poly()
    turtle.circle(50)
    turtle.end_poly()
    screen.register_shape("simple_polygon", turtle.get_poly())

    turtle.reset()

def compound_single(turtle):

    shape = Shape("compound")

    turtle.begin_poly()
    turtle.circle(50)
    turtle.end_poly()
    shape.addcomponent(turtle.get_poly(), "blue", "blue")  # component #1
    screen.register_shape("compound_single", shape)

    turtle.reset()

def compound_double(turtle):

    shape = Shape("compound")

    turtle.begin_poly()
    turtle.circle(50)
    turtle.end_poly()
    shape.addcomponent(turtle.get_poly(), "green", "green")  # component #1

    turtle.penup()
    turtle.left(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.pendown()

    turtle.begin_poly()
    turtle.circle(25)
    turtle.end_poly()
    shape.addcomponent(turtle.get_poly(), "yellow", "yellow")  # component #2
    screen.register_shape("compound_double", shape)

    turtle.reset()

def drag_handler(turtle, x, y):
    turtle.ondrag(None)  # disable ondrag event inside drag_handler
    turtle.goto(x, y)
    update()
    turtle.ondrag(lambda x, y, turtle=turtle: drag_handler(turtle, x, y))

screen = Screen()
tracer(0)

magic_marker = Turtle()
simple_polygon(magic_marker)
compound_single(magic_marker)
compound_double(magic_marker)
magic_marker.hideturtle()

red = Turtle(shape="simple_polygon")
red.color("red")
red.penup()
red.goto(150, 150)
red.ondrag(lambda x, y: drag_handler(red, x, y))

blue = Turtle(shape="compound_single")
blue.penup()
blue.goto(-150, -150)
blue.ondrag(lambda x, y: drag_handler(blue, x, y))

mostly_green = Turtle(shape="compound_double")
mostly_green.penup()
mostly_green.goto(150, -150)
mostly_green.ondrag(lambda x, y: drag_handler(mostly_green, x, y))
update()
screen.mainloop()