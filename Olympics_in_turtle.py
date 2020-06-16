
import turtle
''' 
turtle.showturtle()
turtle.color("red")
turtle.forward(120)
turtle.write("1", font=('adobe garamond', 20, 'normal'))


turtle.right(90)
turtle.color("yellow")
turtle.forward(50)
turtle.write("  2", font=('adobe garamond', 20, 'normal'))

turtle.right(90)
turtle.color("green")
turtle.forward(120)
turtle.write("3", font=('adobe garamond', 20, 'normal'))

turtle.right(90)
turtle.color("blue")
turtle.forward(50)
turtle.write("4", font=('adobe garamond', 20, 'normal'))  '''

radius=int(input("Enter the desired radius: "))
halfRadius=radius/2
diameter=2*radius
y_startCord1=0
y_move1=-radius

cubeDiamter=diameter*3
x_start=-(cubeDiamter/2)           #+(halfRadius))
x_move1=diameter+(halfRadius)
x_move2=radius+(radius/4)

blue=x_start
black=blue+x_move1
red=black+x_move1


yellow=blue+x_move2
green=black+x_move2

fontSize=radius

'''
circles=[blue, black, red, yellow, green]
colours={blue:"blue", black:"black", red:"red", yellow:"yellow", green:"green"}

for i in range(5):
    if i <= 3:
        turtle.color(colours[circles[i]])
        turtle.goto(circles[i], y_startCord1)
        turtle.pendown()
        turtle.circle(radius)
        turtle.penup()
    elif i > 3:
        turtle.color(colours[circles[i]])
        turtle.goto(circles[i], y_move1)
        turtle.pendown()
        turtle.circle(radius)
        turtle.penup()

'''
ts=turtle.getscreen()
ts.bgcolor("pink")     
turtle.pensize(5)

turtle.color("blue")
turtle.penup()
turtle.goto(blue, y_startCord1)   #turtle.goto(x, y)
turtle.pendown()
turtle.circle(radius)


turtle.color("black")
turtle.penup()
turtle.goto(black, y_startCord1)
turtle.pendown()
turtle.circle(radius)

turtle.color("red")
turtle.penup()
turtle.goto(red, y_startCord1)
turtle.pendown()
turtle.circle(radius)

turtle.color("yellow")
turtle.penup()
turtle.goto(yellow, y_move1)
turtle.pendown()
turtle.circle(radius)


turtle.color("green")
turtle.penup()
turtle.goto(green, y_move1)
turtle.pendown()
turtle.circle(radius)


turtle.color("maroon")
turtle.penup()
turtle.goto(0, -(diameter+halfRadius))
turtle.pendown()
turtle.write("Olympics", align='center', font=('Calibri', fontSize, 'normal'))
'''turtle.color("yellow")
turtle.write("Olympics", align='center', font=('Calibri', fontSize, 'normal'))
turtle.write("Olympics", align='center', font=('Calibri', fontSize, 'normal'))
turtle.write("Olympics", align='center', font=('Calibri', fontSize, 'normal'))
turtle.write("Olympics", align='center', font=('Calibri', fontSize, 'normal'))
'''
'''
turtle.penup()
turtle.goto(0, 100)
turtle.pendown()
turtle.write("\u6B22\u8FCE \u03b1 \u03b2 \u03b3", font=('adobe garamond', 40, 'bold'))
turtle.write("\u0000\uFFFF")

'''
input("")
