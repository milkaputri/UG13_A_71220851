import turtle
t=turtle.Turtle()
t.penup()

t.goto(-30,50) 
t.pendown()
t.pensize(10)
t.pencolor("red")

t.right(90)
t.forward(150)
 
t.goto(-30,50)
t.goto(20,-20)
t.goto(65,50)
t.goto(65,-100)

#bentuk 8
t.penup()
t.goto(180,-20)
t.pendown()
for i in range (4):
    t.right(90)
    t.forward(60)
t.goto(180,-80)
for i in range (4):
    t.right(90)
    t.forward(60)
t.penup()

#bentuk 5
t.goto (280, 45)
t.pendown()
t.right(90)
t.forward(60)
t.left(90)
t.forward(60)
t.left(90)
t.forward(60)
t.right(90)
t.forward(60)
t.right(90)
t.forward(60)

#bentuk 1
t.penup()
t.goto(300,40)
t.pendown()
t.left(90)
t.forward(120)
t.penup()

#bentuk P
t.goto(320,40)
t.right(90)
t.pendown()
t.left(90)
t.forward(140)
t.penup()
t.goto(320,-20)
t.pendown()
for i in range (3):
    t.left(90)
    t.forward(60)





