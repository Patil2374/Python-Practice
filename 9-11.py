B =0
for x in range(len(L1)):
    if (L1[x]%2==0):
        B = L1[x] - 50
        L1[x] = B
    else:
        B = L1[x] + 100
        L1[x] = B
print()
print(L1)