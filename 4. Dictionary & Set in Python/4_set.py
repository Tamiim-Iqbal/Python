# Set is the collection of the unordered items
# Each element in the set must be unique & immutable
# list & dict can't be stored in set because they are mutable

collection = {1, 2, 3, 4, "hello", 2}
print(type(collection))                #output: <class 'set'>
print(collection)                      #output: {1, 2, 3, 4, 'hello'}

#empty set
num = set()

# set methods
num.add(1)
num.add(8)
num.add(1)
num.add(3)
print(num)                             #output: {8, 1, 3}

num.remove(8)
print(num)                             #output: {1, 3}

num.add("Hello World")                 #string
num.add((8,4,5))                       #tuple
print(num)                             #output: {1, 3, 'Hello World', (8, 4, 5)}

num.pop()                              #removes a random value
print(num)                             #output: {3, 'Hello World', (8, 4, 5)} 

#num.clear()                           #empties set

num2 = {0, 1, 9, 2, "Bye"}
num3 = {3, 0, 8, 5}

#union -> combines both set values & returns new
print(num3.union(num2))                #output: {0, 1, 2, 3, 5, 8, 9, 'Bye'} 

#intersection -> combines common values & returns new
print(num3.intersection(num2))         #output: {0}