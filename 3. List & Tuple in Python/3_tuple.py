# tuple -> create immutable sequences of values
num = (3, 1, 2)
print(num[0])           #output: 3
print(num[1])           #output: 1
print(type(num))        #output: <class 'tuple'>
#num[1] = 4             #error: tuple object doesn't support item assignment

#single element tuple
num2 = (3,)  
print(num2)             #output: (3,)
print(type(num2))       #output: <class 'tuple'>

num3 = (2)
print(num3)             #output: 2
print(type(num3))       #output: <class 'int'>

#tuple slicing (same as string & list)
roll = (3, 1, 4, 2, 7)
print(roll[1 : 3])      #output: (1, 4)