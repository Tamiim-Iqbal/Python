# Store following word meanings in python dictionary
'''
    table : "a piece of furniture", "list of facts & figures"
    cat : "a small animal"
'''
dict = {
    "table": ("a piece of furniture", "list of facts & figures"),
    "cat" : "a small animal",
}
print(dict)

# You are given a list of subjects for students. Assume one classroom is required for 1 subjects. How many classrooms are needed by all students.
'''
    "python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"
'''
subjects = {"python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"}
print(len(subjects))

# Write a program to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value
marks = {}

x = int(input("Enter Physics number: "))
marks.update({"Physics": x})

x = int(input("Enter Chemistry number: "))
marks.update({"Chemistry": x})

x = int(input("Enter Math number: "))
marks.update({"Math": x})

print(marks)

# Figure out a way to store 9 & 9.0 as separate values in the set.
values = {9, 9.0}
print(values)                              #ops!

value = {
    ("float", 9.0),
    ("int", 9)
}
print(value)