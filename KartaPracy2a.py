#Zad 1
# a = int(input())
# b = int(input())
# if (a + b) % 2 == 0:
#   print("TAK, suma tych liczb jest parzysta")
# else:
#   print("NIE, suma tych liczb nie jest ")

#Zad 2
# a = int(input())
# g = int(input())
# if (a+g)/2 > (a**g)/(1/2):
#   print("TAK")
# else:
#   print("NIE")

#Zad 3
# k = int(input())
# l = int(input())
# m = int(input())
# if k==l:
#   print("Tak")
#   print(k,l)
# else:
#   print("Nie")
# if m==l:
#   print("Tak")
#   print(m,l)
# else:
#   print("Nie")
# if k==m:
#   print("Tak")
#   print(k,m)
# else:
#   print("Nie")

#Zad 4
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# print("najmniejsza jest liczba")
# print(min(a,b,c,d))

#Zad 5
# a = int(input())
# b = int(input())
# c = int(input())
# if a<(b+c) and a>(b-c) and b<(a+c) and b>(a-c) and c<(a+b) and c>(a-b) :
#   print("Tak, te liczby spełniają nierówność trójkąta")
# else:
#   print("Nie, te liczby nie spełniają nierówności trójkąta")

#Zad 6
a = int(input())
b = int(input())
c = int(input())
if a<(b+c) and a>(b-c) and b<(a+c) and b>(a-c) and c<(a+b) and c>(a-b):
 elif c**2 == a**2 + b**2:
  print ("Trójkąt prostokątny")
 elif c**2 > a**2 + b**2:
    print("Trójkąt rozwartokątny")
 elif c**2 < a**2 + b**2:
  print("Trójkąt ostrokątny")
 else:
  print("nie da się stworzyć żadnego trójkąta")