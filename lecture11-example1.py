from tkinter import *

def print_color(event):
  print(event.widget['bg'])

root = Tk()
root.wm_title('tkinter stripe example')
main = Frame(root)
main.pack()

top = Frame(main, height=160, width=640, bg='red')
top.pack()
top.bind('<ButtonPress>', print_color)

mid = Frame(main, height=160, width=640, bg='green')
mid.pack()
mid.bind('<ButtonPress>', print_color)

bot = Frame(main, height=160, width=640, bg='blue')
bot.pack()
bot.bind('<ButtonPress>', print_color)

root.mainloop()
