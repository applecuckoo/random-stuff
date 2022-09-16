# RosetteGoneWild.py
import turtle
t = turtle.Pen()
t.speed(0)
number_of_circles = int(turtle.numinput("Number of circles",
                                        "How many circles in your rosette?", 6))
for x in range(number_of_circles):
    t.circle(100)
    t.left(360/number_of_circles)
