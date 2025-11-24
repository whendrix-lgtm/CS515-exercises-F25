'''
  "Treasure hunt" app
  Window title:  treasure hunt
  640 x 480 black frame
  Treasure is located at (100, 450)
  On left click, calculates distance to treasure and outputs a message
    * distance > 250:  blue X
    * distance between 50 and 250:  yellow X
    * distance between 10 and 50:  red X
    * distance <= 10:  red circle ("O")
  Euclidean distance:  dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
'''
import math
from tkinter import *

def draw_x(x, y, color):
  main.create_line(x-5, y-5, x+5, y+5, fill=color)
  main.create_line(x+5, y-5, x-5, y+5, fill=color)

def print_distance(event):
  distanceX = event.x
  distanceY = event.y
  distance = math.sqrt((distanceX - locationX)**2 + (distanceY - locationY)**2)
  if distance > 250:
    draw_x(event.x, event.y, 'blue')
  elif distance > 50:
    draw_x(event.x, event.y, 'yellow')
  elif distance > 10:
    draw_x(event.x, event.y, 'red')
  else:
    main.create_oval(event.x-5, event.y-5, event.x+5, event.y+5, fill='red')

root = Tk()
root.title('Treasure hunt')
main = Canvas(root, width=640, height=480, bg = 'white')
main.pack()
main.bind('<ButtonPress>', print_distance)
locationX = 100
locationY = 450

root.mainloop()
