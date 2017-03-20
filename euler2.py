suma = 0
j=0
i = 1
while i <4000000:
    if (i+j)%2==0:
        suma = suma+i+j
    h=i
    i = i+j
    j=h
print(suma)
