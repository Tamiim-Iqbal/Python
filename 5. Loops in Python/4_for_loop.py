nums = [1, 5, 3, 9, 12, 29, 2]
for num in nums:
    print(num)


vegetables = ("Potatoes", "Tomato", "Onion", "Capsicum")
for veggies in vegetables:
    print(veggies)

# Else
string = "Bangladesh"
for char in string:
    if(char == 'x'):
        print('x is found')
        break
    print(char)
else:
    print("Not Found")