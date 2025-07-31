for i in range(-1, 0, -1):
        x = body[i-1].xcor()
        y = body[i-1].ycor()
        body[i].goto(x,y)
    
    if total > 0:
        x = serpent.xcor()
        y = serpent.ycor()
        body[0].goto(x,y)