import turtle
T = turtle.Turtle()
T.speed(10)

'''
  Draws a regular polygon with the given turtle

  Args:
  T:  turtle
  n:  # of sides
  s:  side length
'''
def polygon(T, n, s):
  for i in range(n):
    T.forward(s)
    T.left(360/n)

# Test polygon() by drawing polygons with 3-12 sides and perimeter 500
for n in range(3, 13):
  polygon(T, n, 500/n)
