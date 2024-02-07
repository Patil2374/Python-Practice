#1
l1 =["Areoplane","Bangkok","China","Dubai"]
print("Index ===Values")
for i in range(len(l1)):
    print(i,"===",l1[i])
print()

# #2
# s =[(x+100) if x%2==0 else (x+50) for x in range(1,101)]
# print(s)
# print()

# #3
# sum = 0
# for i in range(101):
#     sum += i
# print(sum)
# print()

# #4
# l1 = [101,102,103,104,105,106,107,108]
# even_odd = [(l1[x]+200) if x%2==1 else(l1[x]+100) for x in range(len(l1))]
# print(even_odd)

#4 by slice operator
# l1 = [101,102,103,104,105,106,107,108]
# even_odd = [(x+200) if x%2==0 else(x+100) for x in l1[0::]]
# print(even_odd)

for i in range(1,11):
    for j in range(1,11):
        result = i * j
        print(f"{i}*{j}={result}",end ="\t")
    print()
