from turtle import *
import turtle

hideturtle()
speed(50)


def ctverec(x):
    for _ in range(4):
        forward(x)
        left(90)

def krizek(x):
    left(45)
    for _ in range(4):
        forward(x/2)
        backward(x/2)
        left(90)
    left(45)

#sit  
a = 30
while True:
    x = int(input("rozměr sítě (2 => 2x2) "))
    if x < 3:
        print("minimální velikost hrací plochy je 3x3")
    elif x > 10:
        print("maximální velikost hrací plochy je 10x10")   
    elif x != int(x):
        print("zadejte celé číslo")
    else:break
    

for i in range(x):
    for _ in range(x):
        ctverec(a)
        forward(a)
    
    backward(x*a)
    left(90)
    forward(a)
    right(90)


for _ in range(9):
    penup()

    #hrac1
    while True:
        xy1 = [item for item in input("hráč1: zadejte souřadnice vašeho tahu (x,y) ").split(",")]
        x1 = xy1[0]
        y1 = xy1[1]

        if  (x1 < 0) or (x1 > x) or (x1 != int(x1)):
            print("neplatná souřadnice x")
        elif (y1 < 0) or (y1 > x) or (y1 != int(y1)):
            print("neplatná souřadnice y")
        else:break
    
    x1 = a*xy1[0]
    y1 = xy1[1]

    goto(x1+(a/2),y1*a)
    pendown()
    circle(a/2)
    penup()
    home()
    

    # hrac2
    while True:
        xy2 = [item for item in input("hráč2: zadejte souřadnice vašeho tahu (0,0) ").split(",")]
        y2 = xy2[1]
        x2 = xy2[0]

        if  (x2 < 0) or (x2 > x) or (x2 != int(x2)):
            print("neplatná souřadnice x")
        elif (y2 < 0) or (y2 > x) or (y2 != int(y2)):
            print("neplatná souřadnice y")
        else:break

    y2 = a*xy2[1]
    x2 = a*xy2[0]
    
    goto(x2+(a/2),y2+(a/2))
    pendown()
    krizek(a)
    penup()
    home()

    
exitonclick()
