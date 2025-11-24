from tkinter import *
def px(event):
  print("You typed x")
def py(event):
  print("You typed Y")
def pz(event):
  print(event.keysym)

root = Tk()
main = Frame(root)
main.pack()
exit_button = Button(main, text = "Exit", command = root.destroy)
exit_button.pack()
exit_button.bind('<x>', px)
exit_button.bind('<Y>', py)
root.bind('<Key>', pz)
root.mainloop()
