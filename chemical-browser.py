'''
  Chemical Browser
  Uses ChemDisplay class from chemical.py
'''

from tkinter import *
import chemical

root = Tk()
main = Frame(root)
main.pack()

command_row = Frame(main)
command_row.pack()

display = chemical.ChemDisplay(main)
display.pack()

chemdata = chemical.read_chemicals_from_file('chemicals.csv')
display.set_chemical(chemdata[0])
index = 0

def prev_chemical():
  global index
  index -= 1
  if index < 0:
    index = len(chemdata)-1
  display.set_chemical(chemdata[index])

def next_chemical():
  global index
  index += 1
  if index >= len(chemdata):
    index = 0
  display.set_chemical(chemdata[index])

prev_button = Button(command_row, text='Previous', command=prev_chemical)
prev_button.pack(side=LEFT, padx=10)

next_button = Button(command_row, text='Next', command=next_chemical)
next_button.pack(side=LEFT, padx=10)

root.mainloop()
root.mainloop()
