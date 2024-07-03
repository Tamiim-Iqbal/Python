# list method
num = [3, 1, 2]

num.append(4)           #add element in the end
print(num)              #output: [3, 1, 2, 4]

num.sort()              #sort in ascending order
print(num)              #output: [1, 2, 3, 4]

fruits = ["banana", "litchi", "apple", "watermelon"]
fruits.sort()
print(fruits)           #output: ['apple', 'banana', 'litchi', 'watermelon']

num.sort(reverse=True)  #sort in descending order
print(num)              #output: [4, 3, 2, 1]

num.append(6)
num.append(1)
num.append(7)
print(num)              #output: [4, 3, 2, 1, 6, 1, 7]

num.reverse()  
print(num)              #output: [7, 1, 6, 1, 2, 3, 4]

num.insert(0,5)         #insert element at index
print(num)              #output: [5, 7, 1, 6, 1, 2, 3, 4]

num.remove(1)           #remove 1st occurrence of element
print(num)              #output: [5, 7, 6, 1, 2, 3, 4]

num.pop(1)              #remove element at index
print(num)              #output: [5, 6, 1, 2, 3, 4]