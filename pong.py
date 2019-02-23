# Basic Pong Game in Python 3

import turtle

wn = turtle.Screen()
wn.title("Ping Pong by @alblackwelldev")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")

# Paddle B


# Ball



# Main Game Loop
while True: 
    wn.update()
