from tkinter import *

root = Tk()
root.title('Frame exercise')

mainFrame = Frame(root)
mainFrame.pack()

topRow = Frame(mainFrame)
topRow.pack()

yellowFrame = Frame(topRow, width=300,height=150, bg='yellow')
yellowFrame.pack(side=LEFT)
cyanFrame = Frame(topRow, width=300, height=150, bg='cyan')
cyanFrame.pack(side=LEFT)

bottomRow = Frame(mainFrame)
bottomRow.pack()

redFrame = Frame(bottomRow, width=200,height=150, bg='red')
redFrame.pack(side=LEFT)
greenFrame = Frame(bottomRow, width=200,height=150, bg='green', relief='solid', bd=5)
greenFrame.pack(side=LEFT)
blueFrame = Frame(bottomRow, width=200,height=150, bg='blue')
blueFrame.pack(side=LEFT)
root.mainloop()
