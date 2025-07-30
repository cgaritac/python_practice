import turtle
import random

screen = turtle.Screen()
screen.title('Juego 1')
screen.bgcolor('gray')

turtle1 = turtle.Turtle()
turtle2 = turtle.Turtle()

turtle1.hideturtle()
turtle1.shape('turtle')
turtle1.color('green', 'green')
turtle1.shapesize(2,2,2)
turtle1.pensize(3)

turtle2.hideturtle()
turtle2.shape('turtle')
turtle2.color('blue', 'blue')
turtle2.shapesize(2,2,2)
turtle2.pensize(3)

turtle1.penup()
turtle1.goto(200,100)
turtle1.pendown()
turtle1.circle(40)

turtle1.penup()
turtle1.goto(-200,137)
turtle1.showturtle()

turtle2.penup()
turtle2.goto(200,-100)
turtle2.pendown()
turtle2.circle(40)

turtle2.penup()
turtle2.goto(-200,-67)
turtle2.showturtle()

dado = [1,2,3,4,5,6]

for i in range(20):
    if turtle1.pos() >= (170,137):
        print('La tortuga verde ha ganado')
        break
    elif turtle2.pos() >= (170,-67):
        print('La tortuga verde ha ganado')
        break
    else:
        turno1 = input('Presiona la letra entre para avanzar la rotuga verde.')
        turno1 = random.choice(dado)
        print('Tu numero es: {}, avanzas: {}'.format(turno1, turno1*20))
        turtle1.pendown()
        turtle1.forward(20*turno1)
        
        turno2 = input('Presiona la letra entre para avanzar la tortuga azul.')
        turno2 = random.choice(dado)
        print('Tu numero es: {}, avanzas: {}'.format(turno2, turno2*20))
        turtle2.pendown()
        turtle2.forward(20*turno2)
turtle.done()