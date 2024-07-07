student = {
    "name" : "Saimon",
    "marks" : {
        "phy" : 99,
        "chem" : 89,
        'math' : 95
    }
}

print(student)  #{'name': 'Saimon', 'marks': {'phy': 99, 'chem': 89, 'math': 95}}
print(student["marks"])  #{'phy': 99, 'chem': 89, 'math': 95}
print(student["marks"]["phy"])  #99