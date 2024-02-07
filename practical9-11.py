#Q1 students marks and percentage
import time 
Name = input("Enter the name of student: ")
eng = eval (input("enter the english marks:"))
print(type(eng))
phy = eval (input("enter the physics marks: "))
soc = eval (input("enter the social marks: "))
mat = eval (input("enter the maths marks: "))
hind = eval (input("enter the hindi marks: "))
che = eval (input("enter the chemistry marks: "))
total = eng+phy+soc+mat+hind+che
percentage = total/600*100
#print("Total marks of student is:",total,"and Precentage is:",percentage,"\n")
if (percentage>95 and percentage<100):
    print(f' Dear {Name}, your marks were {total} and percentage is {percentage} you pass') 
    print(f"Dear {Name}, You are outstanding")
elif (percentage<95 and percentage>90):
    print(f' Dear {Name}, your marks were {total} and percentage is {percentage} you pass')
    print("Dear {Name}, You have secured A+ Grade") 
elif (percentage>80 and percentage<90):
    print(f' Dear {Name}, your marks were {total} and percentage is {percentage} you pass')
    print (f"Dear {Name}, You have secured B Grade")
elif (percentage>70 and percentage<80):
    print(f' Dear {Name}, your marks were {total} and percentage is {percentage} you pass') 
    print(f"Dear {Name}, You have secured C Grade")
else:
    print("You failed")

#Q2 write a code to count the vowels in a given string:
Str = "Divya lives in uppal"
count = 0
for x in range(len(Str)):
    if Str[x] in "AEIOUaeiou":
        count+=1
print(count,"\n")

#Q3
L1 = [10,20,30,40,50,60,70]
#a append 80 to 100
L1.append(80)
L1.append(90)
L1.append(100)
print(L1, "\n")
#b instert "Gangster" before 50
L1.insert(4,"Gangster",)
print(L1, "\n")
#c extend L1 to L2=[80,90,100]
L2 = [80,90,100]
L2.extend(L1)
print(L2, "\n")
#d Remove last element from the list 
L1.pop
print(L1,"\n")
#e Remove 60 from the list
L1.remove(60)
print(L1, "\n")
L1.reverse()
print(L1, "\n")

#4 Given char is vovel or not

char = input("Enter a character: ")
if char in "AEIOUaeiou":
    print("Given char is a vowel\n")
else:
    print("Given char is not a vowel\n")    