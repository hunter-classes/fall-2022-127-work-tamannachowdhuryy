import turtle
wn = turtle.Screen()
sarah = turtle.Turtle()

#Start direction 
sarah.up()
sarah.forward(60)

#Experimental data
sarah.down()
for angle in [160, -43, 270, -97, -43, 200, -940, 17, -86]:

#Secind 100 step turn 
   sarah.left(angle)
   sarah.forward(100)

#Direction going after the turn    
print("The pirate's final heading was", sarah.heading())

wn.exitonclick()