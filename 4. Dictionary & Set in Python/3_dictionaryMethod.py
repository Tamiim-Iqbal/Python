student = {
    "name" : "Saimon",
    "marks" : {
        "phy" : 99,
        "chem" : 89,
        'math' : 95
    }
}

print(len(student))                   #output: 2

#return all keys -> .keys()
print(student.keys())                 #output: dict_keys(['name', 'marks'])

#convert dict to list 
print(list(student.keys()))           #output: ['name', 'marks']

#return all values -> .values
print(student.values())               #output: dict_values(['Saimon', {'phy': 99, 'chem': 89, 'math': 95}])

#return all (key,val) pairs as tuples -> .items
print(student.items())                #output: dict_items([('name', 'Saimon'), ('marks', {'phy': 99, 'chem': 89, 'math': 95})])

pair = list(student.items())
print(pair[0])                        #output: ('name', 'Saimon')

#returns the key according to value -> .get("key")
print(student.get("name"))             #output: Saimon
print(student["name"])                 #output: Saimon
#if key doesn't exist  
print(student.get("name2"))            #output: none
#print(student["name2"])               #error

#insert the specified items to the dictionary -> .update
new_dict = {"city" : "delhi", "age" : 23}
student.update(new_dict)
print(student)                         #output: {'name': 'Saimon', 'marks': {'phy': 99, 'chem': 89, 'math': 95}, 'city': 'delhi', 'age': 23}