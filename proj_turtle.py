import turtle
import time

def get_number_of_racers():
    racers=0
    while True:
        racers=input('enter number of racers(2_10) :')
        if racers.isdigit():
            racers=int(racers)
        else:
            print('input is not numeric enter only numeric values between2-10')
            continue
        if racers>=2 and racers<=10:
            return racers
        else:
            print('number not between 2-10')

def init_turtle():
    width,height=500,500
    screen=turtle.Screen()
    screen.setup(width,height)
racers=get_number_of_racers()
init_turtle()
racer=turtle.Turtle()
racer.forward(100)
racer.left(90)
racer.forward(100)
racer.right(90)
racer.backward(100)
time.sleep(5)

    
