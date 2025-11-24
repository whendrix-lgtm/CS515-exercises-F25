'''
Code for reading and displaying information about various chemicals

Chemical:  class that represents one chemical
  Stores cID, name, formula, mass, InChI, and synonyms
read_chemicals_from_file:  function to read chemicals
  Returns a list of Chemical objects from a CSV file
ChemDisplay:  class that displays information about a chemical
  Inherits from tkinter.Frame
  Main method is .set_chemical(chem)
'''

from tkinter import *
import csv

# Display constants
SMALL_PAD    = 5
BIG_PAD      = 20
NUM_SYNONYMS = 10
LABEL_SIZE   = (9, 18, 40, 68)
GRID_WIDTH   = (75, 150, 50)

class Chemical:
  '''
   Class for representing information about an element or compound
  '''
  def __init__(self, split):
    '''
    Constructs the chemical from one row in a CSV file
    Called by read_chemicals_from_file
    '''
    self.cid = int(split[0])
    self.name = split[1]
    self.synonyms = [str.strip() for str in split[2].split('|')]
    self.mw = float(split[3])
    self.formula = split[4]
    self.inchi = split[5]
    self.mass = float(split[6])
  def __str__(self):
    return self.name
  def __eq__(self, rhs):
    return type(rhs) == Chemical and self.cid == rhs.cid

class Field (Frame):
  '''
  Helper class that displays one piece of information
  Includes a label for the type of information
  Text beyond a maximum length will be shorted
  Clicking on data value will print the full string to the console
  '''
  def __init__(self, parent, name, text = '', maxlen = LABEL_SIZE[-1]):
    '''
    Class constructor

    parent:  parent widget (tkinter)
    name:    label for data value
    text:    data value
    maxlen:  maximum number of characters
    '''
    Frame.__init__(self, parent, padx=SMALL_PAD, pady=SMALL_PAD)
    if maxlen < 3:
      self.maxlength = 3
    else:
      self.maxlength = maxlen
    key = Label(self, text=name)
    self.value = Label(self, relief='sunken', bd = 3)
    self.set_text(text)
    self.value.bind('<ButtonPress>', self.print_text)
    key.pack(side = LEFT)
    self.value.pack(side = LEFT)
  def set_text(self, text):
    '''
    Changes the data value
    '''
    if type(text) != str:
      text = str(text)
    self.text = text
    if len(text) > self.maxlength:
      self.value['text'] = text[:self.maxlength - 3] + '...'
    else:
      self.value['text'] = text
  def print_text(self, event):
    '''
    Function for printing data value to console on click
    '''
    if self.text != '':
      print(self.text)

class ChemDisplay (Frame):
  '''
  Frame for displaying information about a Chemical
  '''
  def __init__(self, parent, chem = None):
    '''
    Constructor

    parent:  parent frame (from tkinter)
    chem:    chemical to display (default None)
    '''
    Frame.__init__(self, parent)
    self.chemical = chem

    self.cid = Field(self, 'CID', maxlen = LABEL_SIZE[0])
    self.name = Field(self, 'Name', maxlen = LABEL_SIZE[1])
    self.formula = Field(self, 'Formula', maxlen = LABEL_SIZE[1])
    self.mw = Field(self, 'Mol wt', maxlen = LABEL_SIZE[0])
    self.mass = Field(self, 'Mass', maxlen = LABEL_SIZE[0])
    self.inchi = Field(self, 'InChI', maxlen = LABEL_SIZE[3])
    synframe = Frame(self)
    synlab = Label(synframe, text='Synonyms')
    self.syntext = Text(synframe, height = NUM_SYNONYMS, width = LABEL_SIZE[2])
    self.set_chemical(chem)
    synlab.pack(side = LEFT, padx=BIG_PAD, pady=BIG_PAD)
    self.syntext.pack(side=LEFT, padx=BIG_PAD, pady=BIG_PAD)

    self.cid.grid(row=0, column=0, padx=BIG_PAD)
    self.name.grid(row=0, column=1, padx=BIG_PAD)
    self.formula.grid(row=1, column=1, padx=BIG_PAD)
    self.mw.grid(row=0, column=2, padx=BIG_PAD)
    self.mass.grid(row=1, column=2, padx=BIG_PAD)
    self.inchi.grid(row=3, column=0, columnspan=3)
    synframe.grid(row=4, column=0, columnspan=3)

    for i in range(3):
      self.columnconfigure(i, minsize=GRID_WIDTH[i])

  def set_chemical(self, chem):
    '''
    Changes the frame to display information about the given chemical
    Pass None to clear
    '''
    if chem != None:
      self.chemical = chem
      self.cid.set_text(str(chem.cid))
      self.name.set_text(chem.name)
      self.mw.set_text(chem.mw)
      self.mass.set_text(chem.mass)
      self.formula.set_text(chem.formula)
      self.inchi.set_text(chem.inchi)
      self.syntext.delete('1.0', 'end')
      self.syntext.insert('1.0', '\n'.join(chem.synonyms))
    else:
      self.cid.set_text('')
      self.name.set_text('')
      self.mw.set_text('')
      self.mass.set_text('')
      self.formula.set_text('')
      self.inchi.set_text('')
      self.syntext.delete('1.0', 'end')

def read_chemicals_from_file(filename):
  '''
  Returns a list of Chemicals constructed using the lines of a CSV file
  Expected rows:  CID, name, synonyms, molecular weight, formula, InChI, mass
  '''
  with open(filename) as file:
    file.readline()
    reader = csv.reader(file)
    ret = []
    for line in reader:
      try:
        temp = Chemical(line)
        ret.append(temp)
      except Exception as ex:
        print(f'Error reading line {line}: {ex}')

  return ret
