#smajlik
print("\U0001F60A")

pattern = "Toto je {}. iterace cyklu"
for i in range(10):
    print(pattern.format(i))

pattern = "Toto je {poradi}. iterace cyklu. {poradi}!"
for i in range(10):
    print(pattern.format(poradi = i))

#formatovani retezcu
#indexovani
a = "Ahoj"
#slice index
a[1:]
a[0:2] #horni mez se nevypise