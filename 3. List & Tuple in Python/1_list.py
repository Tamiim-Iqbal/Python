# string → immutable
# list → mutable
marks = [94.2, 98.7, 90.1, 85.3, 99.6]
print(marks)              #output: [94.2, 98.7, 90.1, 85.3, 99.6]
print(type(marks))        #output: <class 'list'>
print(len(marks))         #output: 5
print(marks[0])           #output: 94.2

# list can store element of different types
student = ["Arjun", 94.5, 22, "Dhaka"]
print(student)            #output: ['Arjun', 94.5, 22, 'Dhaka']
student[0] = "Akash"      #change value akash from arjun
print(student)            #output: ['Akash', 94.5, 22, 'Dhaka']
#print(student[4])        #error : list index out of range

#list slicing (similar to string)
price = [34, 76, 83, 94, 64, 32]
print(price[1 : 4])      #output: [76, 83, 94]
print(price[  : 4])      #output: [34, 76, 83, 94]
print(price[1 : ])       #output: [76, 83, 94, 64, 32]
print(price[-3 : -1])    #output: [94, 64]