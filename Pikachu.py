from turtle import *

# Function for position
def my_goto(x, y):
    penup()
    goto(x, y)
    pendown()

# to draw the left eye
def leftEye(x, y):
    my_goto(x, y)
    seth(0)
    fillcolor('#333333')
    begin_fill()
    circle(22)
    end_fill()

    my_goto(x, y + 10)
    fillcolor('#000000')
    begin_fill()
    circle(10)
    end_fill()

    my_goto(x + 6, y + 22)
    fillcolor('#ffffff')
    begin_fill()
    circle(10)
    end_fill()

# To draw the right eye
def rightEye(x, y):
    my_goto(x, y)
    seth(0)
    fillcolor('#333333')
    begin_fill()
    circle(22)
    end_fill()

    my_goto(x, y + 10)
    fillcolor('#000000')
    begin_fill()
    circle(10)
    end_fill()

    my_goto(x - 6, y + 22)
    fillcolor('#ffffff')
    begin_fill()
    circle(10)
    end_fill()

# To draw the mouth
def mouth(x, y):
    my_goto(x, y)
    fillcolor('#88141D')
    begin_fill()

    # Lower Lip
    l1 = []
    l2 = []
    seth(190)
    a = 0.7
    for i in range(28):
        a += 0.1
        right(3)
        fd(a)
        l1.append(position())

    my_goto(x, y)

    seth(10)
    a = 0.7
    for i in range(28):
        a += 0.1
        left(3)
        fd(a)
        l2.append(position())

    # Upper Lip
    seth(10)
    circle(50, 15)
    left(180)
    circle(-50, 15)

    circle(-50, 40)
    seth(233)
    circle(-50, 55)
    left(180)
    circle(50, 12.1)
    end_fill()

    # Tongue
    my_goto(17, 54)
    fillcolor('#DD716F')
    begin_fill()
    seth(145)
    circle(40, 86)
    penup()
    for pos in reversed(l1[:20]):
        goto(pos[0], pos[1] + 1.5)
    for pos in l2[:20]:
        goto(pos[0], pos[1] + 1.5)
    pendown()
    end_fill()

    # Nose
    my_goto(-17, 94)
    seth(8)
    fd(4)
    back(8)

# to draw the left red cheek
def leftCheek(x, y):
    tracer(False)
    my_goto(x, y)
    seth(300)
    fillcolor('#DD4D28')
    begin_fill()
    a = 2.3
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a -= 0.05
            lt(3)
            fd(a)
        else:
            a += 0.05
            lt(3)
            fd(a)
    end_fill()
    tracer(True)

# To draw the right red cheek
def rightCheek(x, y):
    tracer(False)
    my_goto(x, y)
    seth(60)
    fillcolor('#DD4D28')
    begin_fill()
    a = 2.3
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a -= 0.05
            lt(3)
            fd(a)
        else:
            a += 0.05
            lt(3)
            fd(a)
    end_fill()
    tracer(True)

# To draw the left ear
def LeftEar(x, y):
    my_goto(x, y)
    fillcolor('#000000')
    begin_fill()
    seth(330)
    circle(100, 35)
    seth(219)
    circle(-300, 19)
    seth(110)
    circle(-30, 50)
    circle(-300, 10)
    end_fill()

# To draw the right ear
def RightEar(x, y):
    my_goto(x, y)
    fillcolor('#000000')
    begin_fill()
    seth(300)
    circle(-100, 30)
    seth(35)
    circle(300, 15)
    circle(30, 50)
    seth(190)
    circle(300, 17)
    end_fill()

# Body
def body():
    fillcolor('#F6D02F')
    begin_fill()
    penup()
    circle(130, 40)
    pendown()
    circle(100, 105)
    left(180)
    circle(-100, 5)

    # ... The full body drawing code continues here unchanged ...

    # Calling other functions
    cap(-134.07, 147.81)
    mouth(-5, 25)
    leftCheek(-126, 32)
    rightCheek(107, 63)
    LeftEar(-250, 100)
    RightEar(140, 270)
    leftEye(-85, 90)
    rightEye(50, 110)

# Cap
def cap(x, y):
    my_goto(x, y)
    fillcolor('#CD0000')
    begin_fill()
    seth(200)
    circle(400, 7)
    left(180)
    circle(-400, 30)
    circle(30, 60)
    fd(50)
    circle(30, 45)
    fd(60)
    left(5)
    circle(30, 70)
    right(20)
    circle(200, 70)
    circle(30, 60)
    fd(70)
    right(35)
    fd(50)
    circle(8, 100)
    end_fill()

    my_goto(-168.47, 185.52)
    seth(36)
    circle(-270, 54)
    left(180)
    circle(270, 27)
    circle(-80, 98)
    fillcolor('#444444')
    begin_fill()
    left(180)
    circle(80, 197)
    left(58)
    circle(200, 45)
    end_fill()

    my_goto(-58, 270)
    pencolor('#228B22')
    dot(35)

    my_goto(-30, 280)
    fillcolor('#228B22')
    begin_fill()
    seth(100)
    circle(30, 180)
    seth(190)
    fd(15)
    seth(100)
    circle(-45, 180)
    right(90)
    fd(15)
    end_fill()
    pencolor('#000000')

# Main
if __name__ == '__main__':
    screensize(800, 700, "#f0f0f0")
    screen = Screen()
    screen.setup(width=1.0, height=1.0)
    pensize(3)
    speed(10)
    body()
    my_goto(250, -230)
    write("by Ukasha Programmer", font=("Arial", 15))
    mainloop()
