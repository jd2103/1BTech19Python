#Zad1
# for i in range(1,31):
#   print(i, end=" ")

#Zad2
# for i in range(1,10,2):
#   print(i**2, end=" ")

#Zad3
# for i in range(379,10000,379):
#   if i>1000:
#     print(i, end=" ")

#Zad4
# for i in range(100,1000,5):
#   print("podzielna przez 5")
#   print(i, end=" ")
# for y in range(102,1000,6):
#   print("podzielna przez 6")
#   print(y, end=" ")
# for x in range(110,1000,11):
#   print("podzielna przez 11")
#   print(x, end=" ")

#Zad5
# n = int(input("Ile liczb chcesz wpisać?"))
# suma=0
# for i in range(n):
#   k = int(input())
#   suma=suma+k
# print(suma)

#Zad6
# k = int(input())
# a = 0
# for i in range(0,2 * k,2):
#         a= a+i
# print("Suma początkowych liczb parzystych wynosi:")
# print(a)

#Zad7
# m = int(input())
# a = 0
# for i in range(11,(m*2)+11,+2):
#         a=a+i
# print("Suma początkowych liczb dwucyfrowych nieparzystych wynosi:")
# print(a)

#Zad8
# W0 = int(input("Podaj początkową wartość inwestycji:"))
# L = int(input("Podaj lata inwestycji:"))
# Wk = 0
# suma = Wk
# for i in range(0,L * 12):
#     Wk = suma * 0.06 * (1/12)
#     suma =  suma+Wk
# print("Końcowa wartość inweestycji wynosi:")
# print(suma)

#Zad9
# n = int(input("Podaj ilość liczb:"))
# a = 21
# suma = 0
# for i in range(0,n+1):
#     for j in range(0,i,a):
#         print(a)
#         suma = suma+a
#         a = a+100
# print("Suma tych liczb wynosi:")
# print(suma)

#Zad10
# from cmath import sqrt
# for i in range(1,1000):
#     if i % 10 == sqrt(i):
#         print(i)
#     elif i % 100 == sqrt(i):
#           print(i)


