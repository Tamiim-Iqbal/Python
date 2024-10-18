# Print number from 1 to 100
i = 1
while i <= 100:
    print(i)
    i += 1

# Print number from 100 to 1
i = 100
while i >= 1:
    print(i)
    i -= 1

# Print a Multiplication table of a number n
i = 1
n = int(input("Enter a number : "))
print("Multiplication table of", n)

while (i <= 10):
    print(n, "X", i ,"=",n*i)
    i += 1

# Print the elements of the following list using a loop - [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
i = 0
while i < len(num):
    print(num[i])
    i += 1

# Search for a number x in the tuple using loop - (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
num2 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
i = 0
x = int(input("Enter a number to search : "))
while i < len(num2):
    if(num2[i] == x):
        print("Found at index :", i)
        break
    i += 1
