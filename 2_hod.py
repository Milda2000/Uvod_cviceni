print("zadejte sořadnice")
deg = int(input("stupně: "))
if deg >= 360 or deg <= 0:
    print("stupně nejsou v intervalu <-180,180>")
    quit()

min = int(input("minuty: "))
if min >= 60 or min <= 0:
    print("minuty nejsou v intervalu <0,60>")
    quit()

sec = float(input("vteřiny: "))
if sec >= 60 or sec <= 0:
    print("sekundy nejsou v intervalu <0,60>")
    quit()

deg_float = deg + min/60 + sec/3600
print(deg_float)

#kód na jednom řádku/použtí u jaava scriptu(u jazyků, které nelze zakódovat)
print(int(input("zadejte stupně:")) + float(int(input("zadejte minuty: "))/60))

#KEYWORD ARGUMENT(pojmenovaný argument) => int("0xFF",BASE = 16)
#print(sept= (mezi znaky),end=)

