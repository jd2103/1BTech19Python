#Funkcja ord()- zwraca kod ASCII znaku
# print(ord("A"))
# print(ord("Z"))
# w Python kod ASCII wielkich liter A-Z są od 65-90

#Funkcja chr()- zwraca znak dla danego kodu
# print(chr(66))
# print(chr(75))

#Zadanie testowe: wypisz alfabet liter wielkich
# for i in range(65,91):
#     print(chr(i), end=" ")

#String w python- "lista", len- zwraca długość stringa
# napis="ARGENTYNA"
# print(napis[0], napis[1], napis[2])
# print(len(napis))

# for i in range(len(napis)):
#     print(napis[i])

# napis=input()
# szyfr=""
# print(napis[0], napis[1], napis[2])
# print(len(napis))

# napis=input()
# szyfr=""
# for i in range(len(napis)):
#     szyfr = szyfr + chr(65+((ord(napis[i])-65+3)%26))
# print(szyfr)
