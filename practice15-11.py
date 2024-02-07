# n = int(input("Enter the number of table"))
# a = 1
# while(a<=10):
#     print(n,"*",a,"==",n*a)
#     a+=1

# str = input("enter the string")
# a=0
# while(a<len(str)):
#     print("Index",a,"==  Value",str[a])
#     a+=1

# str = input("enter the string")
# a = 0
# count = 0
# while(a<len(str)):
#     if(str[a] not in "AEIOUaeiou"):
#         count+=1
#         print(str[a])
#     a+=1

#2
l1 = [101,102,103,104,102,102,103,104,105]
a = 0
l2 = [] 
while(a<len(l1)):
    if(l1[a] not in l2):
        l2.append(l1[a])
    a+=1
print(l2)

#3
l = [111,12,102,105,106]
a=0
max = 0 
sec_max = 0
while(a<len(l)):
    if(max<l[a]):
        max = l[a]
    elif(max>l[a] and sec_max<l[a]):
        sec_max = l[a]
    a+=1
print(sec_max)

#4
v1 = "silent"
v2 = "listen"
a = 0
if(len(v1) == len(v2)):
    while(a<len(v1)):
        if(v2[a] not in v1):
            print("Given data is not anagram\n")
            
        else:
            print("Given data is anagram\n")
        a+=1
else:
    print("not anagram")

#1
l1 =[1,2,3,4,5,6,7,8,9,10,11,12]
print(l1,"\n")
length = len(l1)
if length % 3 != 0:
    print("List is not divisible in 3 equal parts\n")
else:
    part_size = length // 3
    print("Divided list\n")
    for i in range(0, length, part_size):
        print(l1[i:i+part_size],end = " ")

##4
# v1=input("Enter the string1:")
# v2=input("Enter the string2:")
# if sorted(v1)==sorted(v2):
#     print("It is an anagram")
# else:
#     print("It is not an anagram")

