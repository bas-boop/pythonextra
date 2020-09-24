import turtle

colors = ["purple","blue","green"]
turtle.speed(500)
my_pen = turtle.Pen()
turtle.bgcolor("black")
for x in range(360):
   my_pen.pencolor(colors[x % 3])
   my_pen.forward(150)
   my_pen.left(120)
   my_pen.forward(150)
   my_pen.left(115)
   
turtle.done()

