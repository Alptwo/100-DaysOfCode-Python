from turtle import Turtle, Screen
import random

myturtle = Turtle()

#makes a square

# for i in range(0, 3):
#     myturtle.forward(25)
#     myturtle.left(90)

#makes a dashed line
# for i in range(15):
#     myturtle.forward(10)
#     myturtle.penup()
#     myturtle.forward(10)
#     myturtle.pendown()


#random line lul
# colors = ["blue", "red", "yellow", "green", "black", "wheat"]
# directions = [0, 90, 180, 270]
# myturtle.pensize(5)
# for i in range(100):
#     myturtle.color(random.choice(colors))
#     myturtle.forward(25)
#     myturtle.setheading(random.choice(directions))


def moveforward():
    myturtle.forward(10)




screen = Screen()

screen.listen()

screen.onkey(key="space", fun=moveforward())



screen.exitonclick()