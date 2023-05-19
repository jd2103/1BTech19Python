  WSTĘP
1. Oblicz sumę liczb 3-cyfrowych
suma=0
for i in range(100,1000):
  suma+=i
  wynik=suma
print(suma)
2. Oblicz sume i ilość dwucyfrowych wielokrotności liczby 6
suma=0
ilosc=0
for i in range(10,100):
  if i%6==0:
    suma+=i
    ilosc+=1
print("Suma to", suma)
print("Ilosc to", ilosc)
3. Znajdź największa liczbę wśród 5 wylosowanych przez program liczb 3-cyfrowych
from random import randint
L = [randint(99,1000) for i in range(5)]
print(L)
print(max(L))
4. Podaj sumę cyfr w dowolnej liczbie
s=int(input())
suma=0
while s>0:
  suma+=s%10
  s//=10
print(suma)
5. Znajdź najmniejszą cyfre we wpisanej przez usera liczbie 3-cyfrowej
s=int(input())
L=list(str(s))
print(min(L))

  ALGORYTMY
1. Sprawdź czy wpisana przez usera liczba jest pierwsza
n = int(input())
for i in range(2,n):
    if n % i == 0:
        print("Liczba nie jest pierwsza")
        exit(0)
print("Liczba jest pierwsza")
2. Sprawdź czy wpisana przez usera liczba jest złożona
n = int(input())
for i in range(2,n):
    if n % i == 0:
        print("Liczba jest złożona")
        exit(0)
print("Liczba jest pierwsza")
3. Sprawdź czy wpisana przez usera liczba jest względnie pierwsza z 24
def nwd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

liczba = int(input("Podaj liczbę: "))

nwd_liczba_24 = nwd(liczba, 24)

if nwd_liczba_24 == 1:
    print("Liczba", liczba, "jest względnie pierwsza z 24.")
else:
    print("Liczba", liczba, "nie jest względnie pierwsza z 24.")

4. Zakoduj szyfrem Cezara i kluczem k słowo s 
def szyfruj_cezarem(slowo, przesuniecie):
    zaszyfrowane = ""
    for litera in slowo:
        if litera.isalpha():
            kod_litery = ord(litera) + przesuniecie
            if litera.isupper():
                zaszyfrowane += chr((kod_litery - ord('A')) % 26 + ord('A'))
            elif litera.islower():
                zaszyfrowane += chr((kod_litery - ord('a')) % 26 + ord('a'))
        else:
            zaszyfrowane += litera
    return zaszyfrowane

slowo = input("Podaj słowo do zaszyfrowania: ")
przesuniecie = int(input("Podaj przesunięcie: "))

zaszyfrowane_slowo = szyfruj_cezarem(slowo, przesuniecie)
print("Zaszyfrowane słowo: ", zaszyfrowane_slowo)

5. Dodaj dwa ułamki a/b + c/d. Zapisz sumę jako ułamek nieskracalny i liczbe mieszaną
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
  
6. Znajdź NWW dwóch wpisanych przez usera liczb
Odejmowanie
a=int(input())
b=int(input())
iloczyn=a*b
while a!=b:
    if a>b: a=a-b
    if b>a: b=b-a
print(iloczyn//a)

Modulo
a=int(input())
b=int(input())
iloczyn=a*b
while b>0:
  a,b=b,a%b
print(iloczyn//a)
  KARTKA
1. Oblicz wartość ONP
2. Znajdź postac ONP dla pisanego wyrażenia
3. Napisz algorytm NWD (obie wersje) i przeprowadź symulacje kroków dla podanych liczb
  NAPISY
1. Znajdź ilość literki C we wpisanym napisie
napis = input("Wpisz napis: ")
lw= 0
for znak in napis:
    if znak == "C":
        lw += 1
print("Ilość wystąpień litery C:", lw)

2. Sprawdź czy literki w napisie sa w porządku nierosnącym np. ZOO, WOK, WODA itp
napis = input("Podaj napis: ")
nierosnace = True
for i in range(len(napis) - 1):
    if napis[i] < napis[i+1]:
        nierosnace = False
        break
if nierosnace:
    print("Litery w napisie są w porządku nierosnącym.")
else:
    print("Litery w napisie nie są w porządku nierosnącym.")

3. Podaj najdłuższy z 3 wpisanych przez usera wyrazów
s1 = input("Podaj pierwszy wyraz: ")
s2 = input("Podaj drugi wyraz: ")
s3 = input("Podaj trzeci wyraz: ")
najdluzszy_wyraz = s1
if len(s2) > len(najdluzszy_wyraz):
    najdluzszy_wyraz = s2
if len(s3) > len(najdluzszy_wyraz):
    najdluzszy_wyraz = s3
print("Najdłuższy wyraz: ", najdluzszy_wyraz)
