from turtle import backward, forward,  left, right, exitonclick, speed, penup, pendown
#import turtle

speed(0)

def ctverec(x):
    for _ in range(4):
        forward(x)
        left(90)

def sestiuhelnik(x):
   for _ in range(6):
       forward(x)
       left(60)

def sestiuhelnik_sit(x):
    right(30)
    for _ in range(6):
       forward(x)
       left(60)


#ctverec
a = float(input("jak velký má být čtverec? "))
for _ in range(4):
    forward(a)
    left(90)

exitonclick()

#sestiuhelnik
a = float(input("jak velká má být strana šestiúhelníku? "))
for _ in range(6):
    forward(a)
    left(60)
exitonclick()

#kytycka
a = float(input("jak velká má být strana šestiúhelníku? "))

for _ in range(6):
    sestiuhelnik(a)
    forward(a)
    right(60)

exitonclick()

#ctvercova sit
a = float(input("jak velký má být čtverec? "))
x = int(input("počet sloupců sítě: "))
y = int(input("počet řádků sítě: "))
for i in range(y):
    for _ in range(x):
        ctverec(a)
        forward(a)
    
    backward(y*a)
    left(90)
    forward(a)
    right(90)

exitonclick()

#sestiuhelnikova sit
a = float(input("jak velká má být strana šestiúhelníku? "))
x = int(input("počet sloupců sítě: "))
y = int(input("počet řádků sítě: "))

for i in range(y):
    for _ in range(x):
        sestiuhelnik_sit(a)
        forward(a)
        left(60)
        forward(a)
        right(30)

    left(90)
    forward(a)
    left(60)

    if i%2 == 0:
        for _ in range(x):
            forward(a)
            left(60)
            forward(a)
            right(60)
    else:
        for _ in range(x-1):
            forward(a)
            left(60)
            forward(a)
            right(60)    
    
    forward(a)
    right(150)


    

exitonclick()