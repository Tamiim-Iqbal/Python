# conversion -> automatically
a = 2
b = 3.25
c = "2"
sum = a + b
print(sum)  # Output: 5.25
# print(a+c)  # error: unsupported operand type for +: 'int' and 'str'

# casting -> manually
c = int(c)
print(a+c) # Output: 4