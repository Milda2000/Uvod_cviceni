import random as rnd

cislo = rnd.randint(1,100)

#moje verze
# cislo_uzivatel = int(input("jaké číslo si myslím? "))
# while cislo_uzivatel != cislo:
#     if cislo_uzivatel > cislo:
#         print("hádej menší")
#     else: 
#         print("hádej větší")
#     cislo_uzivatel = int(input("jaké číslo si myslím? "))
#print("uhádl jsi! je to číslo", cislo)

#verze xtompok
while True:
    cislo_uzivatel = int(input("jaké číslo si myslím? "))
    if cislo_uzivatel > cislo:
        print("hádej menší")
    elif cislo_uzivatel < cislo: 
        print("hádej větší")
    else: break

print("uhádl jsi! je to číslo", cislo)


