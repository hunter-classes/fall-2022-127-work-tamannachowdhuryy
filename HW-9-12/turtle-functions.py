import turtle


#draw a square
def square(t,x,y,w,color,sidelen):
    """
    Draw a square using the turtle passed into t

    Parameters:
        t - a turtle
        x,y - location
        w - width of side
        color - color to draw in
        sidelen - length of each side
    Returns:
      nothing
    """
    t.penup()
    t.goto(x,y)
    t.width(w)
    t.color(color)
    t.pendown()
        
    for i in range(4):
        t.forward(sidelen)
        t.right(90)
            
#def triangle(fill in these):
#code to draw the triangle
def triangle(t,x,y,w,color,sidelen):
    """
    Draw a square using the turtle passed into t

    Parameters:
        t - a turtle
        x,y - location
        w - width of side
        color - color to draw in
        sidelen - length of each side
    Returns:
      nothing
    """
    t.penup()
    t.goto(x,y)
    t.width(w)
    t.color(color)
    t.pendown()
        
    for i in range(3):
        t.forward(sidelen)
        t.right(120)

#def hexagon(fill in these):
#code to draw the hexagon
def hexagon(t,x,y,w,color,sidelen):
    """
    Draw a square using the turtle passed into t

    Parameters:
        t - a turtle
        x,y - location
        w - width of side
        color - color to draw in
        sidelen - length of each side
    Returns:
      nothing
    """
    t.penup()
    t.goto(x,y)
    t.width(w)
    t.color(color)
    t.pendown()
        
    for i in range(6):
        t.forward(sidelen)
        t.left(300)
        
#def ngon(t,numsides,x,y,color,width,sidelen):
#code to draw the ngon
def ngon(t,numsides,x,y,color,w,sidelen):
    """
    Draw a square using the turtle passed into t

    Parameters:
        t - a turtle
        x,y - location
        w - width of side
        color - color to draw in
        sidelen - length of each side
        numsides - the sides of the shape
    Returns:
      nothing
    """
    t.penup()
    t.goto(x,y)
    t.width(w)
    t.color(color)
    t.pendown()
        
    for i in range(9):
        t.forward(sidelen)
        t.left(40)
        
#coding for placement of he shapes 
wn = turtle.Screen()

crush = turtle.Turtle()

square(crush,0,0,1,"green",50)

squirt = turtle.Turtle()
square(squirt, 100,100,5,"red",80)
square(crush, -50,30,3, "yellow",100)
crush.setheading(45)
square(crush,150,30,2,"blue",60)
triangle(crush,150,120,3, "purple",100)
hexagon(crush,70,200,3, "pink",60)
ngon(crush,80,-120,90,"orange",0,80)

wn.exitonclick()
wn.mainloop()
