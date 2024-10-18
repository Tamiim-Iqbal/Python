# Dictionaries are used to store data values in key:value pairs
# Properties : unordered, mutable, don't allow duplicate keys
info = {
    "name" : "Tamim",                      #string
    "age" : 22,                            #int
    "marks" : [94.4, 89.7],                #list
    "subjects" : ("python", "c"),          #tuple
}

print(type(info))                          #output: <class 'dict'>
print(info)                                #output: {'name': 'Tamim', 'age': 22, 'marks': [94.4, 89.7], 'subjects': ('python', 'c')}
print(info["name"])                        #output: Tamim
print(info["marks"])                       #output: [94.4, 89.7]

#change value
info["name"] = "Iqbal"
print(info["name"])                        #output: Iqbal

#add new value
info["country"] = "Bangladesh"
print(info["country"])                     #output: Bangladesh

#empty dictionary
hello = {}
print(hello)                              #output: {}
hello["text"] = "World"
print(hello)                              #output:  {'text': 'World'}