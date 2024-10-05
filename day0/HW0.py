from turtle import *

#we want to paint a house

#step one draw a square

width(7)
color("red")
begin_fill()
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(70)
end_fill()

#step two make the door

color("yellow")
begin_fill()
left(90)
forward(120)
right(90)
forward(70)
right(90)
forward(120)
right(90)
forward(70)
left(90)
end_fill()

#step four build the roof

penup()
goto(0,0)
goto(200,200)
pendown()
color("brown")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#step five make the windows and then colour them blue

color("red")
goto(0,0)
right(240)
forward(30)
left(90)
forward(50)

color("blue")
begin_fill()
penup()
pendown()
forward(50)
right(90)
forward(30)
right(90)
forward(50)
right(90)
forward(30)
end_fill()

#step six make the second window

color("red")
goto(0,0)
right(180)
forward(150)
left(90)
forward(50)

color("blue")
begin_fill()
penup()
pendown()
forward(50)
right(90)
forward(30)
right(90)
forward(50)
right(90)
forward(30)
end_fill()







exitonclick()