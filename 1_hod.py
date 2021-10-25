import math
#print(1+2.5)
#print("Hello")
#print("2+2=", 2+2)

x = 479 

pi = 3.16

#ustaleny zapis osetreni vstupu
x =float( input("čtverec má stranu:"))
if x > 0:
    print("Zadej číslo větší než 0!!!!!!")
    quit()

elif x > 10:
    print("Zadej číslo menší než 0!!!!!!")
    quit()


obsah = pi*(x**2)
obvod = 2*math.pi*x
print("obsah čtverce je", obsah)
print("obvod čtverce je", obvod)


#muj kod
while True:
    x =float( input("čtverec má stranu:"))
    if x > 0:
        obsah = pi*(x**2)
        obvod = 2*math.pi*x
        print("obsah čtverce je", obsah)
        print("obvod čtverce je", obvod)
        break
    else: print("Zadej číslo větší než 0!!!!!!")






# //    **  %
#quit()
#type()
#bool => false = prázdný retězec a nulové číslo
# >, <, >=, <=, ==, !=

