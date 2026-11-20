import turtle, math, colorsys

screen = turtle.Screen()
screen.bgcolor("black")
screen.colormode(1.0)
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.pensize(2)
N, S = 1400, 60

for i in range(N):
    a = i/N * 12 * math.pi
    r = (math.exp(math.cos(a))
         - 2 * math.cos(4 * a)
         - math.sin ( a / 12 ) ** 5)
    x = S * r * math.sin(a)
    y = S * r * math.cos(a)

    t.color(colorsys.hsv_to_rgb(i/N, 1, 1))
    t.goto(x, y)
    if i % 7 == 0:
        t.goto(0, 0)
        t.dot(5)
    if i % 20 == 0:
        screen.update()
turle.done()