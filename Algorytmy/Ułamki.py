#Dodawanie ułamków
a=int(input("Licznik nr 1 "))
b=int(input("Mianownik nr 1 "))
c=int(input("Licznik nr 2 "))
d=int(input("Mianownik nr 2 "))
x, y = b, d
iloczyn=x*y
while x!=y:
    if x>y: x=x-y
    if y>x: y=y-x
nww=iloczyn//x
e=(nww//b)*a
f=(nww//d)*c
g=e+f
print(f"{a}/{b} + {c}/{d} = {e}/{nww} + {f}/{nww} = {g}/{nww}")




