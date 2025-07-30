import turtle

screen = turtle.Screen()
t = turtle.Turtle()

screen.bgcolor('green')
screen.title('Proyecto 1')

t.shapesize(5, 10, 1) #Ancho, largo, borde
t.fillcolor('orange')
t.forward(100)

t.pencolor('white')
t.forward(100)

t.color('red', 'yellow') #Color de la tinta y color de tortuga
t.right(90)
t.forward(100)

t.pensize(5)
t.forward(100)

turtle.done()