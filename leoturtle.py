
from ipycanvas import MultiCanvas
import math
from ipywidgets import Color
from sidecar import Sidecar


class TurtleScreen():
    def __init__(self, width=400, height=400):
        self.multicanvas = MultiCanvas(4, width=width, height=height)
        self.turtleCanvas = self.multicanvas[3]
        self.sc = Sidecar(title="Turtle Screen")
        with self.sc:
            display(self.multicanvas)
        self.turtles = []

    def draw(self):
        self.turtleCanvas.clear()
        for turtle in self.turtles:
            turtle.draw_turtle()


class Turtle():
    def __init__(self, screen=TurtleScreen()):
        self.screen = screen
        self.multicanvas = screen.multicanvas
        self.background = self.multicanvas[0]
        self.canvas = self.multicanvas[1]
        self.fillCanvas = self.multicanvas[2]
        self.turtleCanvas = self.multicanvas[3]
        self.fill = False
        self.center = (self.canvas.width/2, self.canvas.height/2)
        self.position = list(self.center)
        self.heading = 180
        self.pen = True
        self.turtleVisible = True
        self.turtleSize = 5
        self.turtleCanvas.fill_style = 'red'
        self.turtleSpeed = 5  # speed in pixels per refresh cycle
        # self.canvas.fill_style = 'red'
        # self.fillCanvas.fill_style = 'red'
        self.screen.turtles.append(self)
        self.screen.draw()

    def draw_turtle(self):
        self.turtleCanvas.move_to(*self.position)
        if self.turtleVisible:
            self.turtleCanvas.fill_arc(
                self.position[0], self.position[1], self.turtleSize, 0, 2*math.pi)

    def forward(self, distance):
        step = self.turtleSpeed
        if distance < 0:
            step = - self.turtleSpeed
        stepsum = 0
        while abs(stepsum+step) <= abs(distance):
            self.forward_step(step)
            stepsum += step
        if abs(stepsum) < abs(distance):
            self.forward(distance-stepsum)

    def fd(self, distance):
        self.forward(distance)

    def forward_step(self, distance):
        self.canvas.begin_path()
        self.canvas.move_to(*self.position)
        delta_x = distance*math.sin(math.radians(self.heading))
        delta_y = distance*math.cos(math.radians(self.heading))
        self.position[0] += delta_x
        self.position[1] += delta_y
        if self.pen:
            self.canvas.line_to(*self.position)
        if self.fill:
            self.fillCanvas.line_to(*self.position)
        self.canvas.stroke()
        self.screen.draw()

    def back(self, distance):
        self.forward(-distance)

    def bk(self, distance):
        self.back(distance)

    def left(self, angle):
        self.heading = (self.heading + angle) % 360
        self.screen.draw()

    def lt(self, angle):
        self.left(angle)

    def right(self, angle):
        self.left(-angle)

    def rt(self, angle):
        self.right(angle)

    def circle(self, radius, angle=360, direction=1):
        step = int(self.turtleSpeed*180/(math.pi*radius))
        if step == 0:
            step = 1
        if angle < 0:
            step = - step
        stepsum = 0
        while abs(stepsum+step) <= abs(angle):
            self.circle_step(radius, step, direction)
            stepsum += step
        if abs(stepsum) < abs(angle):
            self.circle_step(radius, angle-stepsum, direction)

    def circle_step(self, radius, angle=360, direction=1):
        angle = int(angle)
        distance = 2*radius*math.tan(math.radians(0.5))
        self.canvas.begin_path()
        for _ in range(angle):
            delta_x = distance*math.sin(math.radians(self.heading))
            delta_y = distance*math.cos(math.radians(self.heading))
            self.position[0] += delta_x
            self.position[1] += delta_y
            self.left(direction)
            self.canvas.line_to(*self.position)
            if self.fill:
                self.fillCanvas.line_to(*self.position)
        self.canvas.stroke()
        self.screen.draw()

    def leftArc(self, radius, angle):
        self.circle(radius, angle=angle)

    def rightArc(self, radius, angle):
        self.circle(radius, angle=angle, direction=-1)

    def goto(self, x, y):
        self.canvas.move_to(x, y)
        self.screen.draw()

    def setx(self, x):
        self.canvas.move_to(x, self.position[1])
        self.screen.draw()

    def sety(self, y):
        self.goto(self.position[0], y)
        self.screen.draw()

    def setheading(self, angle):
        self.angle = angle
        self.screen.draw()

    def home(self):
        self.position = list(self.center)
        self.heading = 180
        self.screen.draw()

    def begin_fill(self):
        self.fill = True
        self.fillCanvas.begin_path()
        self.fillCanvas.move_to(*self.position)

    def end_fill(self):
        self.fill = False
        self.fillCanvas.fill()
        self.canvas.draw_image(self.fillCanvas, 0, 0)
        self.fillCanvas.clear()

    def dot(self, radius):
        self.canvas.fill_arc(
            self.position[0], self.position[1], radius, 0, 2*math.pi)

    def pendown(self):
        self.pen = True

    def penup(self):
        self.pen = False

    def pencolor(self, color):
        self.canvas.stroke_style = color
        self.fillCanvas.stroke_style = color

    def fillcolor(self, color):
        self.fillCanvas.fill_style = color
        self.canvas.fill_style = color

    def showturtle(self):
        self.turtleVisible = True
        self.screen.draw()

    def hideturtle(self):
        self.turtleVisible = False
        self.screen.draw()

    def speed(self, speed):
        self.turtleSpeed = 5*speed

    def clearScreen(self):
        self.canvas.clear()
        self.fillCanvas.clear()
        self.position = list(self.center)
        self.heading = 180
        self.screen.draw()

    def cs(self):
        self.clearScreen()
