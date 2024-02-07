# # in while loop
# def chapital_characters():
#     for i in range(65,91):
#         print(chr(i),end =" ")

# def lower_characters():
#     for i in range(97,123):
#         print(chr(i), end = " ")

# if(__name__ == "__main__"):
#     chapital_characters()
#     print()
#     lower_characters()

# # in while loop
# def chapital_characters():
#     a = 65
#     while a<=90:
#         print(chr(a),end =" ")
#         a+=1


# def lower_characters():
#     a = 97
#     while a<=122:
#         print(chr(a), end = " ")
#         a+=1

# if(__name__ == "__main__"):
#     chapital_characters()
#     print()
#     lower_characters()

# def duplicate(l1):
#     l2 =[]
#     for x in l1:
#         if x not in l2:
#             l2.append(x)
#     print(l2)

# if(__name__ == "__main__"):
#     l1 = [121,122,123,124,121,122]
#     duplicate(l1)



def thirdlargest(l):
    digit = []
    print(l[-3])

if __name__ == "__main__":
    l = 7721029878
    thirdlargest(l)

def find_third_largest_digit(number):
    digits = [int(digit) for digit in str(number)]
    unique_digits = sorted(set(digits), reverse=True)

    if len(unique_digits) < 3:
        return "Not enough unique digits in the number."

    third_largest = 0
    count = 0
    for digit in unique_digits:
        count += 1
        if count == 3:
            third_largest = digit
            break

    return third_largest