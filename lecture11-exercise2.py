'''
  Application that selects its own window color

  3 Entries:  Red, Green, then Blue
  "Change" button:  reads 3 Entry values and sets the background color
    * Pack all with padx=10 and pady=10

  Entries should be ints in range 0-255
'''


from tkinter import *

root = Tk()
red_frame = Frame(root)
red_frame.pack()
green_frame = Frame(root)
green_frame.pack()
blue_frame = Frame(root)
blue_frame.pack()

Label(red_frame, text='Red:').pack(side=LEFT,padx=10, pady=10)
Label(green_frame, text='Green:').pack(side=LEFT,padx=10, pady=10)
Label(blue_frame, text='Blue:').pack(side=LEFT,padx=10, pady=10)

red_entry = Entry(red_frame)
red_entry.pack(side=LEFT, padx=10, pady=10)
green_entry = Entry(green_frame)
green_entry.pack(side=LEFT, padx=10, pady=10)
blue_entry = Entry(blue_frame)
blue_entry.pack(side=LEFT, padx=10, pady=10)

def read_entries():
  try:
    red = int(red_entry.get())
    green = int(green_entry.get())
    blue = int(blue_entry.get())
    if red in range(256) and green in range(256) and blue in range(256):
      # Convert 3 ints of 0-255 into a color:
      root.configure(f'#{red:02x}{green:02x}{blue:02x}')
  except:
    pass

change_button = Button(root, text='Change', command=read_entries)
change_button.pack(padx=10, pady=10)

root.mainloop()
