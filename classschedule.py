
"@author Maevah Miot"

import turtle


t= turtle.Turtle()
t.speed(5)

t.pencolor("blue")
t.pensize("4")
t.penup()
t.goto (0,300)
t.write("Class Schedule")

        #first line
t.penup()
t.goto(-300,250)
t.pendown()
t.forward(600)
 #second line
t.penup()
t.goto(-300,200)
t.pendown()
t.forward(600)
     #third line
t.penup()
t.goto(-300,150)
t.pendown()
t.forward(600)
     #fourth 
t.penup()
t.goto(-300,100)
t.pendown()
t.forward(600)
t.penup()
    #final 
t.penup()
t.goto(-300,50)
t.pendown()
t.forward(600)
t.penup()
     
#vertical
t.goto(0,250)
t.pendown()
t.left(-90)
t.forward(200)
t.penup()

t.hideturtle()
     
  #writing the class name   
t.goto(-300,225)
t.write("Computer Programming 2")
t.penup()
t.goto(-300,175)
t.write("Database Analysis/Logic Design")
t.penup()
t.goto(-300,125)
t.write("Programming for the Web")
t.penup()
t.goto(-300,75)
t.write("Prob and Stats")
t.penup()


   #writing time of class
t.goto(10,225)
t.write(" MWF  12:00-12:50PM")
t.penup()
t.goto(10,175)
t.write("TTH  1:00-2:20PM")
t.penup()
t.goto(10,125) 
t.write("TTH 9:30-10:50AM")
t.penup()
t.goto(10,75)
t.write("MWF 1:00-1:50PM")





    
     
    
     
      
     
         