import turtle
import math

T = turtle.Turtle()
T.radians()

def move_toward(x, y):
  tx, ty = T.pos()
  angle = math.atan2(y-ty, x-tx)
  T.setheading(angle)
  T.forward(50)

screen = turtle.Screen()
screen.onclick(move_toward)

screen.listen()
screen.mainloop()
