# Write a program to print the length of a list. (list is the parameter)
def lengthOfList(nums):
    length = len(nums)
    return length

nums = [2, 3, 6, 9, 0, 1, 7]

length = lengthOfList(nums)
print(length)
print(nums)





# Write a program to print the elements of a list in a single line. (list is the parameter)
def printList(cities):
    for city in cities:
        print(city, end=" ")
    
cities = ["New York City", "Berlin", "Tokyo", "Dhaka"]

printList(cities)
print()                          # to avoid the % at the end





# Write a program to find the factorial of n. (n is the parameter)
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

factorial(5)





# Write a program to convert USD to BDT. (1 USD = 120 BDT. oct, 24)
def convert(usd):
    taka = usd * 120
    print(taka, "tk")

convert(10)