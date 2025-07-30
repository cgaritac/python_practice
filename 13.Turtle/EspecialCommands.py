import turtle

screen = turtle.Screen()
t = turtle.Turtle()

t.speed(10) #El valor de la velocidad va de uno a diez
t.circle(10)
t.speed(10)
t.circle(50)
t.dot(30)

t.hideturtle()
t.circle(40)

t.setx(100) #Hace que se mueva sobre el eje x
t.sety(-500)

turtle.done()