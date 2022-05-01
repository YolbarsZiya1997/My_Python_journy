import turtle

ziya_turtle = turtle.Turtle()
ziya_turtle.speed(500)
jesur_turtle = turtle.Turtle()
jesur_turtle.speed(500)
alim_turtle = turtle.Turtle()
alim_turtle.speed(500)


def square():
    ziya_turtle.forward(100)
    ziya_turtle.right(60)
    ziya_turtle.forward(100)
    ziya_turtle.right(60)
    ziya_turtle.forward(100)
    ziya_turtle.right(60)
    ziya_turtle.forward(100)
    ziya_turtle.right(60)
    ziya_turtle.forward(100)
    ziya_turtle.right(60)
    ziya_turtle.forward(100)
    ziya_turtle.right(5)


def cube():
    jesur_turtle.forward(150)
    jesur_turtle.left(90)
    jesur_turtle.forward(150)
    jesur_turtle.left(90)
    jesur_turtle.forward(150)
    jesur_turtle.left(90)
    jesur_turtle.forward(150)
    jesur_turtle.left(15)


def matrix():
    alim_turtle.right(60)
    alim_turtle.forward(200)
    alim_turtle.right(120)
    alim_turtle.forward(200)
    alim_turtle.right(120)
    alim_turtle.forward(200)
    alim_turtle.right(30)


for i in range(100):
    square()
    cube()
    matrix()
