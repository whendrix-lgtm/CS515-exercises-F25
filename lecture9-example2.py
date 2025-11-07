import turtle

def hello():
    print('You just pressed enter!')
screen = turtle.Screen()
screen.onkey(hello, 'Return')
screen.listen()
screen.mainloop()
