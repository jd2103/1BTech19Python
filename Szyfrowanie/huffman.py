W = "aaaaabbccccdddeeeeeeefggg" #5a2b4c3d7ef3g
W+="."
H=""
ilosc=1
for i in range(len(W)-1):
  if W[i]==W[i+1]:
    ilosc += 1
  else:
    if ilosc>1:
       H+=str(ilosc)
    H+=W[i]
    ilosc=1
print(H)
