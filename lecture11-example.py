from tkinter import *
root = Tk()
exit_button = Button(root, text = "Exit", command = root.destroy)
# root.destroy():  close the program
exit_button.pack()
root.mainloop()
