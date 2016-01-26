import turtle

def drawStar(N, R):
    turtle.reset()
    a = 360/N
    for i in range(N):
        turtle.fd(R)
        turtle.bk(R)
        turtle.left(a)

def drawSootSprite(N, R):
    # reset direction
    turtle.reset()
    # draw star
    drawStar(N, R)
    # draw body
    turtle.dot(0.8*2*R)
    # draw right eyeball
    turtle.fd(0.2*R)
    turtle.dot(0.3*R, 'white')
    # draw right pupil
    turtle.pu()
    turtle.bk(0.1*R)
    turtle.pd()
    turtle.dot(0.05*R)
    turtle.pu()
    # centre
    turtle.setpos(0, 0)
    # draw left eyeball
    turtle.bk(0.2*R)
    turtle.pd()
    turtle.dot(0.3*R, 'white')
    # draw left pupil
    turtle.pu()
    turtle.fd(0.1*R)
    turtle.pd()
    turtle.dot(0.05*R)

    turtle.hideturtle()

#drawStar(5, 200)
drawSootSprite(50, 200)

turtle.mainloop()

