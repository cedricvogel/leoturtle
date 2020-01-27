
from ipycanvas import MultiCanvas
import math
from ipywidgets import Color


class Turtle():
    def __init__(self):
        self.multicanvas = MultiCanvas(4, width=400, height=400)
        self.background = self.multicanvas[0]
        self.canvas = self.multicanvas[1]
        self.fillCanvas = self.multicanvas[2]
        self.turtleCanvas = self.multicanvas[3]
        self.fill = False
        self.center = [200, 200]
        self.position = [200, 200]
        self.heading = 0
        self.pen = True
        self.turtleVisible = True
        self.turtleSize = 5
        self.turtleCanvas.fill_style = 'red'
        self.turtleSpeed = 5  # speed in pixels per refresh cycle
        # self.canvas.fill_style = 'red'
        # self.fillCanvas.fill_style = 'red'

    def turtle_draw(self):
        self.turtleCanvas.clear()
        self.turtleCanvas.move_to(*self.position)
        if self.turtleVisible:
            self.turtleCanvas.fill_arc(
                self.position[0], self.position[1], self.turtleSize, 0, 2*math.pi)

    def draw(self):
        self.turtle_draw()
        return self.multicanvas

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

    def forward_step(self, distance):
        self.canvas.begin_path()
        self.canvas.move_to(*self.position)
        delta_x = round(distance*math.sin(math.radians(self.heading)))
        delta_y = round(distance*math.cos(math.radians(self.heading)))
        self.position[0] += delta_x
        self.position[1] += delta_y
        if self.pen:
            self.canvas.line_to(*self.position)
        if self.fill:
            self.fillCanvas.line_to(*self.position)
        self.canvas.stroke()
        self.turtle_draw()

    def back(self, distance):
        self.forward(-distance)

    def left(self, angle):
        self.heading = (self.heading + angle) % 360
        self.turtle_draw()

    def right(self, angle):
        self.left(-angle)
        self.turtle_draw()

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
        self.turtle_draw()

    def leftArc(self, radius, angle):
        self.circle(radius, angle=angle)

    def rightArc(self, radius, angle):
        self.circle(radius, angle=angle, direction=-1)

    def goto(self, x, y):
        self.canvas.move_to(x, y)
        self.turtle_draw()

    def setx(self, x):
        self.canvas.move_to(x, self.position[1])
        self.turtle_draw()

    def sety(self, y):
        self.goto(self.position[0], y)
        self.turtle_draw()

    def setheading(self, angle):
        self.angle = angle
        self.turtle_draw()

    def home(self):
        self.goto(self.center[0], self.center[1])

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
        self.turtle_draw()

    def hideturtle(self):
        self.turtleVisible = False
        self.turtle_draw()

    def speed(self, speed):
        self.turtleSpeed = 5*speed

    def clear(self):
        self.canvas.clear()
        self.fillCanvas.clear()
