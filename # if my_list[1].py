# l = []
# n = int(input("Enter the iterations:"))

# for i in range(n):
#     k = input().split()
#     if k[0] == "append":
#         l.append(int(k[1]))
#     elif k[0] == "sort":
#         l.sort()
#     elif k[0] == "insert":
#         x = int(input("Enter Index position: "))
#         y = k[1]
#         l.insert(x, y)
#     elif k[0] == "extend":
#         if k[1].startswith('[') and k[1].endswith(']'):
#             inner_list = [int(x) for x in k[1][1:-1].split(',')]
#             k[1] = inner_list
#         l.append(k[1])
# print(l)


import numpy as np
l1 = np.array([[1,2,3],[4,5,6],[7,8,9]],ndmin=5)
print(l1.ndim)
