from turtle import backward, forward,  left, right, exitonclick, speed, penup, pendown

#sit
def ctverec(x):
    for _ in range(4):
        forward(x)
        left(90)

a = 30
x = int(input("roměr sítě (2 => 2x2) "))
for i in range(x):
    for _ in range(x):
        ctverec(a)
        forward(a)
    
    backward(y*a)
    left(90)
    forward(a)
    right(90)

exitonclick()
