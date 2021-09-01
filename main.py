from turtle import Turtle, Screen, color
import turtle
import random

background = 'racetrack.gif'
turtle.bgpic(background)

# is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color : ")

# colors = ["red", "blue", "green", "orange", "purple", "yellow"]


# y_positions = [-175, -107, -38, 30, 103, 175 ]

# all_turtles= []

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

# if user_bet:
#     is_race_on = True

# while is_race_on:
    
    for turtle in all_turtles:
        if turtle.xcor() > 220:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"Your have won. {winning_color} is the winner!")
            else:
                print(f"You have lost. {winning_color} is the winner!")
        
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()
