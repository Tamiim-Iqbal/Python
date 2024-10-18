# string writing
str1 = "This is a string.\n"               #next line -> \n
str2 = 'String in single quote.\t'         #tab -> \t
str3 = """This is also a string.\n"""
print(str1, str2, str3)

# string concatenation
str_1 = "Hello "
str_2 = "World"
finalString = str_1 + str_2
print(finalString)                         #output : Hello World

# length of string -> len()
len1 = "Tamim"
print(len(len1))                           #output : 5

# indexing (position) -> start from 0 
idx = "Bangladesh"
print(idx[0])                              #output : B
#idx[1] = "A"                              #can't be modified

# slicing -> str[starting_idx : ending_idx] (ending idx is not included)
str = "Bangladesh"
print(str[6 : 10])                         #output : desh
print(str[ : 6])                           #[0:6]
print(str[6 : len(str)])                   #[6:last idx]

# slicing : Negative index
str2 = "Apple"
print(str2[-4 : -1])                       #output: ppl