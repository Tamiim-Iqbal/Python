# Write a program to check if a number entered by the user is odd or even
num = int(input("Enter a number: "))
if(num % 2 == 0):
    print(num, "is even")
elif(num % 2 != 0):
    print(num, "is odd")
else:
    print(num, "is zero")

# Write a program to find the greatest of 3 numbers entered by the user
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))
if(a == b and a == c):
    print("All equal")
elif(a >= b and a >= c):
    print(a, "is largest")
elif(b >= c):
    print(b, "is largest")
else:
    print(c,"is largest")

# Write a program to check if a number is a multiple of 7 or not
num2 = int(input("Enter a number: "))
if(num2 % 7 == 0):
    print(num2, "is a multiple of 7")
else:
    print(num2, "isn't a multiple of 7")