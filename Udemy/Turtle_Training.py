import turtle

def posit():
    timmy.color("black")
    timmy.left(90)
    timmy.forward(100)
    timmy.left(90)
    timmy.forward(10)
    timmy.right(90)
    timmy.forward(10)
    timmy.right(90)
    timmy.forward(20)

timmy= turtle.Turtle()
timmy.hideturtle()
posit()
timmy.color('green')
turtle.bgcolor('black')
turtle.speed(200)
a=0
while a<200:
    timmy.right(a)
    timmy.forward(a *3)
    a+=1

screen= turtle.Screen()
screen.canvheight
screen.exitonclick()

