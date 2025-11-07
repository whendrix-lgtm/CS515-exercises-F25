import turtle
T = turtle.Turtle()

T.pencolor(0, 0.25, 0)
T.fillcolor(0, 0.75, 0)

T.begin_fill()
T.forward(200)
T.left(138)
while abs(T.pos()) > 1:
  T.forward(200)
  T.left(138)
T.end_fill()
