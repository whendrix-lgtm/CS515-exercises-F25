# Script that allows user to "drive" the turtle at 50 px/sec
# Controls:
#  * Left:  turn left 2.5 degrees
#  * Right:  turn right 2.5 degrees
#  * Right click:  reset

import turtle

T = turtle.Turtle()
T.speed(0)
screen = turtle.Screen()

def turn_left():
  T.left(2.5)

def turn_right():
  T.right(2.5)

def reset(x, y):
  T.reset()

def move_forward():
  T.forward(5)
  screen.update()
  screen.ontimer(move_forward, 100)

# Each 100ms:
#  Move forward 5px
#  Prepare to move forward again in 100ms

screen.onkeypress(turn_left, 'Left')
screen.onkeypress(turn_right, 'Right')
screen.onclick(reset, 3)
screen.ontimer(move_forward, 100)

screen.listen()
screen.mainloop()
