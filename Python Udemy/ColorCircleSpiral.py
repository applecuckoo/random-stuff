import turtle
t = turtle.Pen()
turtle.bgcolor("black")
t.speed(0)
colors = ["red", "blue", "green", "yellow"]
for x in range(100):
    t.pencolor( colors[ x % 4] )
    t.circle(2*x)
    t.left(95)
