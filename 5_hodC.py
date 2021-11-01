from math import pi
#priklady funkci
def read_int(prompt):
    astr = input(prompt)
    return int(astr)

def print_float3(num):
    print(f"{num:.3F}")

def square(side):
    return(side*side)

def obsahKruhu (polomer):
    return pi*(polomer*polomer)

def obvodKruhu (polomer):
    return 2*pi*polomer

x = int(input("kolik je poloměr?"))
obsah = obsahKruhu(x)
obvod = obvodKruhu(x)
print(f"Obsah kruhu je {obsah}")
print(f"Obvod kruhu je {obvod}")