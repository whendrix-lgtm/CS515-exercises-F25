from tkinter import *

root = Tk()
root.wm_title('tkinter stripe example')
main = Frame(root)
main.pack()

top = Frame(main, height=160, width=640, bg='red')
top.pack()

mid = Frame(main, height=160, width=640, bg='green')
mid.pack()

bot = Frame(main, height=160, width=640, bg='blue')
bot.pack()

root.mainloop()
