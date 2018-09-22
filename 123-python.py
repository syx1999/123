#e2.1Drawpython.py
import turtle
turtle.setup(700,4000,250,250)
turtle.penup()
turtle.fd(-300)
turtle.pendown()
turtle.pensize(30)
turtle.pencolor("red")
turtle.seth(-40)
for i in range(4):
    turtle.circle(60,90)
    turtle.circle(-70,90)
turtle.circle(100,80/2)
turtle.fd(80)
turtle.circle(-100,200)
turtle.fd(70*2/3)

