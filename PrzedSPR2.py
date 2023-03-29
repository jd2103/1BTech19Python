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
# c=input()
# suma=0
# for i in c:
#   suma+=ord(i)
# print(suma)

# 5. Policz ile we wpisanym napisie jest liter A.
# e=input()
# ilosc=0
# for x in e:
#   if x=="A":
#       ilosc+=1
# print(ilosc)
  
# 6. Podaj dominującą literkę we wpisanym napisie. Niech to będzie tylko jedna literka.
# g=input()
# maks=0
# for x in g:
#   if g.count(x)>maks:
#       maks=g.count(x)
#       literka=x
# print(literka, maks)




# 7. Znajdź literkę-dominantę w napisie (może ich być kilka, a może nie być żadnej)

# 8. Sprawdź czy w napisie występują trzy podciągi "LA"
h=input()
ilosc=0
for i in range(len(h)-1):
  if h[i:i+2]=="LA":
      ilosc+=1
if ilosc ==3:
  print("TAK")
else:
  print("NIE")


# 9. Znajdź "średnią literkę" w napisie. (Przejdź na kody ASCII i jeśli wynik będzie
# ułamkowy to zaokrąglij średnią w dół)

# 10. Wypisz literki, których nie ma w napisie

# 11. Znajdź ilość trzyznakowych palindromów w napisie (trzy literki koło siebie)