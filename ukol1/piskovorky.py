from turtle import *
from math import sqrt

hideturtle()
speed(0)

#funkce pro zakresleni ctverce
def ctverec(x):
    for _ in range(4):
        forward(x)
        left(90)

#funkce pro zakresleni sestiuhleniku
def sestiuhelnik(x):
   for _ in range(6):
       forward(x)
       left(60)

#funkce pro zakresleni krizku
def krizek(x):
    left(45)
    for _ in range(4):
        forward(x/2)
        backward(x/2)
        left(90)
    left(45)

#velikost strany ctverce/sestiuhelniku    
a = 30

#vyber hraci plochy + overeni vstupu
while True:
    typ_site = int(input("Na jaké síťi chcete hrát \n 0 => čtvercová \n 1 => šetiúhelníková \n "))
    if typ_site == 0 or typ_site == 1:
        break
    else: print("neplatný výběr, zadejte 0 nebo 1")

#urceni rozmeru site + overeni vstupu
#sit omezena z praktickych duvodu (3x3 az 10x10)
while True:
    x = int(input("rozměr sítě (3 => 3x3) "))
    if x < 3:
        print("minimální velikost hrací plochy je 3x3")
    elif x > 10:
        print("maximální velikost hrací plochy je 10x10")   
    else:break
    
if typ_site == 0:
    #sit ctverec
    for i in range(x):
        for _ in range(x):
            ctverec(a)
            forward(a)

        penup()
        goto (0,(i+1)*a)
        pendown()
        #backward(x*a)
        #left(90)
        #forward(a)
        #right(90)
else:
    #sit sestiuhlenik
    "zkusit zjednodusit"
    for i in range(x):
        pendown()
        for _ in range(x):
            sestiuhelnik(a)
            left(120)
            forward(a)
            right(60)
            forward(a)
            right(60)
        
        penup()
        forward(a)
        right(60)

        if i%2 == 0:
            for _ in range(x-1):
                forward(a)
                right(60)
                forward(a)
                left(60)
        else:
            for _ in range(x):
                forward(a)
                right(60)
                forward(a)
                left(60)    
        
        forward(a)
        left(60)

#jedno hraci kolo, opakuje se tolikrat kolik je bunek v siti
#pocitani odehranych her
j=0
while True:
    penup()
    #hrac1, krouzek
    #ziskani souradnic a jejich overeni
    while True:
        xy1 = [int(item) for item in input("hráč1: zadejte souřadnice vašeho tahu (x,y) ").split(",")]
        x1 = xy1[0]
        y1 = xy1[1]
        
        if  (x1 < 0) or (x1 > (x-1)):
            print("neplatná souřadnice x")
        if (y1 < 0) or (y1 > (x-1)):
            print("neplatná souřadnice y")
        else:break

    "zkultivovat vypocet souradnic"
    if typ_site == 0:
        #umisteni krouzku ve ctvercove siti
        x1 = a*xy1[0]
        #y1 = xy1[1]
        y1 = a*xy1[1]
        goto(x1+(a/2),y1)
        #goto(x1+(a/2),y1*a)
    else:
        #umisteni krouzku v sestiuhlenikove siti
        vyska = a*sqrt(3)
        x1 = (a +(a/2))*xy1[0]
        #y1 = xy1[1]
        y1 = vyska*xy1[1]
        if x1%2 == 0:
            goto(x1+(a/2),(y1+(0.1*a)))
            #goto(x1+(a/2),(y1*(a*sqrt(3)))+(0.1*a))
        else:
            #goto(x1+(a/2),(y1*(a*sqrt(3)))+(0.1*a)+((a*sqrt(3))/2))
            goto(x1+(a/2),(y1+(vyska)/2)+(0.1*a))
    
    pendown()
    color("blue")

    if typ_site == 0:
        #velikost krouzku ve ctvercove siti
        circle(a/2)
    else:
        #velikost krouzku v sestiuhlenikove siti
        circle((0.9*(a*sqrt(3)))/2)
    
    penup()
    home()
    j += 1

    if j == x**2:
        break
    
    # hrac2, krizek
    #ziskani souradnic a jejich overeni
    while True:
        xy2 = [int(item) for item in input("hráč2: zadejte souřadnice vašeho tahu (x,y) ").split(",")]
        y2 = xy2[1]
        x2 = xy2[0]

        if  (x2 < 0) or (x2 > x-1):
            print("neplatná souřadnice x")
        if (y2 < 0) or (y2 > x-1):
            print("neplatná souřadnice y")
        else:break

    if typ_site == 0:
        #umisteni krizku ve ctvercove siti
        x2 = a*xy2[0]
        y2 = a*xy2[1]
        goto(x2+(a/2),y2+(a/2))
    else:
        #umisteni krizku v sestiuhlenikove siti
        x2 = (a +(a/2))*xy2[0]
        y2 = vyska*xy2[1]
        #y2 = (a*sqrt(3))*xy2[1]
        if x2%2 == 0:
            goto(x2+(a/2),y2+(vyska/2))
            #goto(x2+(a/2),y2+((a*sqrt(3))/2))
        else:
           goto(x2+(a/2),y2+vyska)
           #goto(x2+(a/2),y2+(a*sqrt(3)))
    
    pendown()
    color("red")
    if typ_site == 0:
        #velikost krizku ve ctvercove siti
        krizek(a)
    else:
        #velikost krizku v sestiuhelnikove siti
        krizek(0.8*(2*a))
    
    penup()
    home()
    color("black")
    j += 1

    if j == x^2:
        break
    
    #konec kola

print("hra skončila")
exitonclick()