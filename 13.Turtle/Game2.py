import turtle
import random
import time

delay = 0.05
count = 0
count_high = 0

screen = turtle.Screen()
screen.setup(1250,650)
screen.title('Juego 2')
screen.bgcolor('gray')

serpent = turtle.Turtle()
serpent.speed(1)
serpent.shape('square')
serpent.penup()
serpent.goto(0,0)
serpent.direction = 'stop'
serpent.color('green')

food = turtle.Turtle()
food.shape('circle')
food.color('orange')
food.penup()
food.goto(0,100)
food.speed(0)

body = []

text = turtle.Turtle()
text.speed(0)
text.color('black')
text.penup()
text.hideturtle()
text.goto(0, -260)
text.write('Marcador: 0\tMarcador mas alto: 0', align='center', font=('verdana', 24, 'normal'))

def arriba():
    serpent.direction = 'up'

def abajo():
    serpent.direction = 'down'

def izquierda():
    serpent.direction = 'left'

def derecha():
    serpent.direction = 'right'

def movement():
    if serpent.direction == 'up':
        y = serpent.ycor()
        serpent.sety(y + 20)
    if serpent.direction == 'down':
        y = serpent.ycor()
        serpent.sety(y - 20)
    if serpent.direction == 'right':
        x = serpent.xcor()
        serpent.setx(x + 20)
    if serpent.direction == 'left':
        x = serpent.xcor()
        serpent.setx(x - 20)

screen.listen()
screen.onkeypress(arriba, 'Up')
screen.onkeypress(abajo, 'Down')
screen.onkeypress(derecha, 'Right')
screen.onkeypress(izquierda, 'Left')

while True:
    screen.update()

    if serpent.xcor() > 300 or serpent.xcor() < -300 or serpent.ycor() > 300 or serpent.ycor() < -300:
        time.sleep(2)
        for i in body:
            i.clear()
            i.hideturtle()
        serpent.home()
        serpent.direction = 'stop'
        body.clear()

        count = 0
        text.clear()
        text.write('Marcador:{}\tMarcador mas alto:{}'.format(count,count_high), align='center', font=('verdana', 24, 'normal'))
        
    if serpent.distance(food) < 20:
        x = random.randint(-250,250)
        y = random.randint(-250,250)
        food.goto(x,y)

        new_body = turtle.Turtle()
        new_body.shape('square')
        new_body.color('green')
        new_body.penup()
        new_body.goto(0,0)
        new_body.speed(0)
        body.append(new_body)

        count += 10
        if count > count_high:
            count_high = count
            text.clear()
            text.write('Marcador:{}\tMarcador mas alto:{}'.format(count,count_high), align='center', font=('verdana', 24, 'normal'))

    total = len(body)

    for i in range(total-1, 0, -1):
        x = body[i-1].xcor()
        y = body[i-1].ycor()
        body[i].goto(x,y)
    
    if total > 0:
        x = serpent.xcor()
        y = serpent.ycor()
        body[0].goto(x,y)

    movement()

    for i in body:
        if i.distance(serpent) < 20:
            for i in body:
                i.clear()
                i.hideturtle()
            serpent.home()
            body.clear()
            serpent.direction = 'stop'

    time.sleep(delay)

turtle.done()