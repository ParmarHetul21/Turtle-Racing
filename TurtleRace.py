# A Turtle Race Game
import turtle
import time
import random

HEIGHT, WIDTH = 500, 500
COLORS = ['red', 'yellow', 'blue', 'brown', 'orange', 'green', 'violet', 'black', 'pink', 'yellow']

def get_racer_number():
    racer = 0
    while True:   
        racer = input("Enter the number of racer (2 - 10): ")
        if racer.isdigit():
            racers = int(racer)
        else:
            print("enter the numeric values!.. Try again")
            continue
    
        if 2 <= racers <= 10:
            return racers
        else:
            print("Try again numvber is not in range....")

def init_turtle():
    # Setting up a string
    screen = turtle.Screen()
    screen.setup(HEIGHT, WIDTH)
    screen.title("Turtle racing")

def create_turtle(colors):
    turtles = []
    spacingX = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH // 2 + (i + 1) * spacingX, -HEIGHT // 2+ 20)
        racer.pendown()
        turtles.append(racer)
    return turtles


def racing(colors):
    turtles = create_turtle(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]

racers = get_racer_number()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers] 

winner = racing(colors)
print("the winner of the race is",winner)
time.sleep(10)