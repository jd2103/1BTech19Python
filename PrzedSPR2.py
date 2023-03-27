#1. Wczytaj napis i wypisz z niego pierwszą i ostatnią litere
# s= input()
# print(s[0], s[-1])

#2. Wczytaj napis i wypisz z niego literki poza pierwszą i ostatnią
# s=input()
# for i in range(1, len(s)-1):
#   print(s[i], end="")
# print()

# print(s[1:len(s)-1])

#3. Wypisz 4 ostatnie literki z wpisanego napisu
# s=input()
#1
# for i in range(len(s)-1, len(s)-5, -1):
#   print(s[i], end="")
# print()
#2
# L=list(s)
# L.reverse()
# s= "".join(L)
# for i in range(4):
#   print(L[i], end="")
# print()
#3
# print(s[len(s)-1:len(s)-5:-1])

#4. Waga napisu to suma kodów ascii
c=input()
suma=0
for i in c:
  suma+=ord(i)
print(suma)

