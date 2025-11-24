'''
  "Treasure hunt" app
  Window title:  treasure hunt
  640 x 480 black frame
  Treasure is located at (100, 450)
  On left click, calculates distance to treasure and outputs a message
    * distance > 250:  "Cold"
    * distance between 50 and 250:  "Warm"
    * distance between 10 and 50:  "Hot"
    * distance <= 10:  "Congratulations!"
  Euclidean distance:  dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
'''
import math
from tkinter import *

def print_distance(event):
  distanceX = event.x
  distanceY = event.y
  distance = math.sqrt((distanceX - locationX)**2 + (distanceY - locationY)**2)
  if distance > 250:
    print('Cold')
  elif distance > 50:
    print('Warm')
  elif distance > 10:
    print('Hot')
  else:
    print('Congratulations!!!')

root = Tk()
root.title('Treasure hunt')
mainFrame = Frame(root, width=640, height=480, bg = 'black')
mainFrame.pack()
mainFrame.bind('<ButtonPress>', print_distance)
locationX = 100
locationY = 450

root.mainloop()
