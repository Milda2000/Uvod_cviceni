volba = int(input("v jakém formátu chcete zadávat souřadnice? \n ve stupních => 0 \n ve formátu DMS => 1 \n"))
if volba == 0:
    souradnice = input("zadejte sořadnice ve formátu N000°00´000.00\" \n")
    pol = souradnice[0]
    deg = int(souradnice[1:4])
    if deg >= 360 or deg <= 0:
        print("stupně nejsou v intervalu <-180,180>")
        quit()

    min = int(souradnice[5:7])
    if min >= 60 or min <= 0:
        print("minuty nejsou v intervalu <0,60>")
        quit()

    sec = float(souradnice[8:-1])
    if sec >= 60 or sec <= 0:
        print("sekundy nejsou v intervalu <0,60>")
        quit()

    deg_float = deg + min/60 + sec/3600
    #jak zachovat 3 pozice + zaokrouhleni?
    print(f"{pol}{deg_float:.5f}")
else:
    souradniceDMS = input("zadejte souřadnice jako desetinné číslo ve formátu N00000000: ")
    polDMS = souradniceDMS[0]
    deg_float = float(souradniceDMS[1:])
    deg = int(deg_float)
    min_float = (deg_float - deg)*60 
    min = int(min_float)
    sec = (min_float - min)*60

    print(f"{polDMS}{deg:03}°{min:02}´{sec:.3f}\" ")