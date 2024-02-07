# a = "i am a good student"
# b = a.split()
# for c in reversed(b):
#     b.append(c)
# d = ' '.join(b) 
# print(d)
# index = 0
# print(" ".join(b),)
# while index < len(b):
#     print(" ".join(b[4:index+1]),)
#     index += 1


a = "i am a good student"
for x in a: 
    x = a.split()
    a2 = " ".join(reversed(x))
print(a2)