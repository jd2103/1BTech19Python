# Zadanie 1
# a=int(input())
# b=int(input())
# c=int(input())

# if (b-a)==(c-b):
#   print("ciąg arytmetyczny")

# if (b/a)==(c/b):
#   print("ciąg geometryczny")

# if a<b<c:
#   print("ciąg rosnący")

# if c<b<a:
#   print("ciąg malejący")

#Zadanie 2
# suma=0
# for i in range(100,1000):
#     if i%8==0 and i%16!=0:
#         suma+=i
# print(suma)

#Zadanie 4
ilosc=0
for i in range(10,100):
    cd=i//10
    cj=i%10
    if cd>=2*cj:
        ilosc+=1
print(ilosc)