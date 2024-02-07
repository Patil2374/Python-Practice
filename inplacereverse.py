# # str = "Software engineer"
# # str = list(str)
# # a = len(str)
# # b = a//2
# # for i in range(b):
# #     temp = str[i]
# #     temp2 = str[a-1]
# #     str[i] = temp2
# #     str[a-1] = temp
# #     a-=1
# # str = ''.join(str)
# # print(str)


# # #palindrome
# # str = input("Enter string to check if it is palindrome or not:- ")
# # str2 = ""
# # for i in range(len(str)):
# #     str2 = str[i] + str2
# # if(str == str2):
# #     print(str, ":Given String is a palindrome")
# # else:
# #     print(str, ":Given String is not a palindrome")

# import time 
# L1=[101,102,103,104,105]
# print("Given string is ",L1)
# print("for loop exicution below\n")
# for x1 in L1:
#     print(x1)
# print()
# time.sleep(2)
# print("End of an application")

travel = input("Do you want to travel? ")
for i in range(1):
    if(travel == "yes"):
        print("Yes i want to go to travel")
    else:
        print("I don't want to travel")