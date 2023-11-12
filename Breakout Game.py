import turtle

import time

import random

"""# Set up the screen"""
screen = turtle.Screen()
screen.title("Breakout")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)
"""#Paddle"""
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)
"""# Ball"""
ball = turtle.Turtle()
ball.speed(40)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

"""# Bricks"""
bricks = []

def create_bricks():
    colors = ["red", "orange", "yellow", "green", "blue"]
    for y in range(150, 250, 50):
        for x in range(-240, 260, 80):
            brick = turtle.Turtle()
            brick.speed(0)
            brick.shape("square")
            brick.color(random.choice(colors))
            brick.shapesize(stretch_wid=1, stretch_len=4)
            brick.penup()
            brick.goto(x, y)
            bricks.append(brick)


create_bricks()
"""# Paddle movement"""
def paddle_right():
    x = paddle.xcor()
    if x < 245:
        x += 20
    paddle.setx(x)

def paddle_left():
    x = paddle.xcor()
    if x > -245:
        x -= 20
    paddle.setx(x)


"""# Keyboard bindings"""
screen.listen()
screen.onkey(paddle_right, "Right")
screen.onkey(paddle_left, "Left")
"""# Main game loop"""
while True:
    screen.update()
    """# Move the ball"""
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    """# Border checking"""
    if ball.xcor() > 290 or ball.xcor() < -290:
        ball.dx *= -1
    if ball.ycor() > 290:
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.goto(0, 0)
        ball.dy *= -1
    """# Paddle and ball collisions"""
    if (ball.ycor() < -240 and ball.ycor() > -250) and (ball.xcor() > paddle.xcor() - 50 and
                                                        ball.xcor() < paddle.xcor() + 50):
        ball.sety(-240)
        ball.dy *= -1
    """# Brick and ball collisions"""
    for brick in bricks:
        if ball.distance(brick) < 30:
            brick.goto(1000, 1000)  # Move the brick off the screen
            bricks.remove(brick)
            ball.dy *= -1
    """# Check for win"""
    if not bricks:
        turtle.goto(0, 0)
        turtle.write("You Win!", align="center", font=("Courier", 24, "normal"))
        time.sleep(2)
        turtle.clear()
        break
    """# Check for game over"""
    if ball.ycor() < -290:
        turtle.goto(0, 0)
        turtle.write("Game Over", align="center", font=("Courier", 24, "normal"))
        time.sleep(2)
        turtle.clear()
        break