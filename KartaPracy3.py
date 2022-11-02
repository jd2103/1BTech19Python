#Zad1
# n = int(input())

# for i in range(n):
#   print(i**3 + 3, end=" ")

#Zad2
# for i in range(105,1000,15):
#   print(i, end=" ")

#Zad3
# n = int(input())
# for i in range(1,n+1):
#   if n % i == 0:
#     print(i, end=" ")

#Zad4
# suma = 0
# for i in range(10,100):
#   suma = suma + i
#   print(suma)

#Zad5
# n = int(input("W ile gramy?"))
# suma = n * (n+1) //2
# for i in range(n-1):
#   k = int(input())
#   suma = suma - k
# print("Brakuje:", suma)

#napisz pętle sumującą liczby dwucyfrowe parzyste
# suma = 0
# for i in range(10,100,2):
#   suma = suma + i
# print(suma)

#Zad6
#Fibo wg literatury 0 1 1 2 3 5 8 13 21 34
#Fibo nasze 1, 2, 3, 5, 8, 13...
# n = int(input())
# a, b = 0,1
# for i in range(n):
#     a, b = b, a + b
#     print(b, end=" ")
