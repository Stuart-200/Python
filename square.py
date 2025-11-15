import turtle

turtle.Screen().bgcolor("Green")

screen = turtle.Screen()
screen.setup(400,300)

turtle.title("Welcome to Turtle Window")

pen = turtle.Turtle()

for i in range(4):
    
    pen.forward(100)
    pen.left(90)
    i = i+1
    
turtle.done()