deg_float = float(input("zadejte souřadnice jako desetinné číslo: "))
deg = int(deg_float)
min_float = (deg_float - deg)*60 
min = int(min_float)
sec = (min_float - min)*60

print(f"{deg} stupňů {min} minut {round(sec)} sekund")

