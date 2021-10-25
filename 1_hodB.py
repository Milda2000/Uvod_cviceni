import math

print("ax^2+b+c")
a = float(input("zadejte a: "))
b = float(input("zadejte b: "))
c = float(input("zadejte c: "))

dis = b**2 - (4*a*c)

if dis > 0:
    x1 = (-b + math.sqrt(dis))/ (2*a)
    x2 = (-b - math.sqrt(dis))/ (2*a)
    print("x1 = ",x1, "x2 = ",x2)
elif dis == 0:
    x = -b / 2*a
    print("x1,2 = ", x)
else: print("x1,2 nejsou v množině reálných čísel")
