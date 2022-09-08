import turtle


#draw a square
def square(t,x,y,w,color,sidlen):
        t.penup()
        t.goto(x,y)
        t.width(w)
        t.color(color)
        t.pendown()
        
        for i in range(4):
            t.forward(sidlen)
            t.right(90)

wn = turtle.Screen()

crush = turtle.Turtle()

square(crush,0,0,1,"green",50)

squirt = turtle.Turtle()
square(squirt, 100,100,5,"red",80)
square(crush, -50,30,3, "yellow",100)
crush.setheading(45)
square(crush,150,30,2,"blue",60)

wn.exitonclick()
wn.mainloop()