student = {
    "name" : "Saimon",
    "marks" : {
        "phy" : 99,
        "chem" : 89,
        'math' : 95
    }
}

print(student)                              #output: {'name': 'Saimon', 'marks': {'phy': 99, 'chem': 89, 'math': 95}}
print(student["marks"])                     #output: {'phy': 99, 'chem': 89, 'math': 95}
print(student["marks"]["phy"])              #output: 99