import turtle

wn = turtle.Screen()

crush = turtle.Turtle()

#draw a square
for i in range(3):
    crush.forward(50)
    crush.right(90)


#create a second turtle
#into the variable squirt
#make squirt draw a triangle
squirt = turtle.Turtle()

squirt.up()
squirt.goto(100,100)
squirt.down()
squirt.color("red")
squirt.width(5)
for i in range(3):
    squirt.forward(50)
    squirt.right(120)

wn.exitonclick()
wn.mainloop()
