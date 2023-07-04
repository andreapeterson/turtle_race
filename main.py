import turtle as t
import random
from tkinter import messagebox

race = False
screen = t.Screen()
screen.bgpic("racetrack.png")
screen.setup(width=850, height=500)
user_bet = screen.textinput("Who Will Win?", "Which turtle do you think will win the race: Pink, Orange, Blue, "
                                             "or Green?").capitalize()

y_positions = [130, 60, -90, -160]
colors = ["Pink", "Orange", "Blue", "Green"]
turtles = []
for turtle_num in range(0, 4):
    turtle = t.Turtle(shape="turtle")
    turtle.penup()
    turtle.speed("fast")
    turtle.goto(x=-415, y=y_positions[turtle_num])
    turtle.color(colors[turtle_num])
    turtles.append(turtle)

if user_bet:
    race = True

leading_position = -414
while race:
    distance = [0, 10, 20, 30, 40, 50]
    for turtle in turtles:

        if turtle.xcor() > 360:
            race = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                messagebox.showinfo("Outcome", f"YAY you won! {winning_color} won the race!! Go {winning_color}")
            else:
                messagebox.showinfo("Outcome",
                                    f"Aw, your turtle lost the race. {winning_color} won the race. Maybe {user_bet} will win next "
                                    f"time.")

        turtle.forward(int(random.choice(distance)))

        if turtle.xcor() > leading_position:
            leading_position = turtle.xcor()
            turtle.shapesize(1.5, 1.5, 1)
        else:
            turtle.shapesize(1, 1, 1)

screen.exitonclick()
