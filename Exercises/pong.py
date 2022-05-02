import turtle

wn = turtle.Screen()
wn.title("Pong by @YolbarsZiya")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
palaq_a = turtle.Turtle()
palaq_a.speed(0)
palaq_a.shape("square")
palaq_a.color("white")
palaq_a.shapesize(stretch_wid=5, stretch_len=1)
palaq_a.penup()
palaq_a.goto(-350, 0)

# Paddle B
palaq_b = turtle.Turtle()
palaq_b.speed(0)
palaq_b.shape("square")
palaq_b.color("white")
palaq_b.shapesize(stretch_wid=5, stretch_len=1)
palaq_b.penup()
palaq_b.goto(350, 0)

# Ball
top = turtle.Turtle()
top.speed(0)
top.shape("circle")
top.color("white")
top.penup()
top.goto(0, 0)
top.dx = 0.1
top.dy = -0.11

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A : 0  Player B :", align="center", font=("Courier", 20, "normal"))


# Functions
def palaq_a_up():
    y = palaq_a.ycor()
    y += 20
    palaq_a.sety(y)


def palaq_a_down():
    y = palaq_a.ycor()
    y -= 20
    palaq_a.sety(y)


def palaq_b_up():
    y = palaq_b.ycor()
    y += 20
    palaq_b.sety(y)


def palaq_b_down():
    y = palaq_b.ycor()
    y -= 20
    palaq_b.sety(y)


# Keyboard binding
wn.listen()
wn.onkeypress(palaq_a_up, "w")
wn.onkeypress(palaq_a_down, "s")
wn.onkeypress(palaq_b_up, "Up")
wn.onkeypress(palaq_b_down, "Down")

# Main game loop
while True:
    wn.update()

    # Move the top
    top.setx(top.xcor() + top.dx)
    top.sety(top.ycor() + top.dy)

    # Boarder checking
    if top.ycor() > 290:
        top.sety(290)
        top.dy *= -1

    if top.ycor() < -290:
        top.sety(-290)
        top.dy *= -1

    if top.xcor() > 390:
        top.goto(0, 0)
        top.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A : {}  Player B : {}".format(score_a, score_b), align="center", font=("Courier", 30, "bold"))

    if top.xcor() < -390:
        top.goto(0, 0)
        top.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A : {}  Player B : {}".format(score_a, score_b), align="center", font=("Courier", 30, "bold"))

    # Paddle and ball collisions
    for i in range(0, 390):

        if (340 < top.xcor() < 350) and (
                palaq_b.ycor() + 50 > top.ycor() > palaq_b.ycor() - 50):
            top.setx(340)
            top.dx *= -1

        if (-340 > top.xcor() > -350) and (
                palaq_a.ycor() + 50 > top.ycor() > palaq_a.ycor() - 50):
            top.setx(-340)
            top.dx *= -1
