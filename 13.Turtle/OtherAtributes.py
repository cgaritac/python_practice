import turtle

screen = turtle.Screen()
t = turtle.Turtle()

'''t.begin_fill()
t.circle(100)
t.end_fill()

t.begin_fill()
t.color('white', 'white')
t.circle(50)
t.end_fill()'''

t.shape('turtle')
t.shape('arrow')
t.shape('circle')
t.shape('square')
t.shape('triangle')
t.shape('classic')

t.penup()
t.forward(100)

t.pendown()
t.forward(100)

t.undo()
t.clear() #Limpia la pantalla pero la tortuga queda en el mismo lugar
t.reset() #Reinicia el programa

t.forward(100)
t.stamp()
t.forward(100)

turtle.done()