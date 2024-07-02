str = "i am a coder"

print(str.endswith("er"))  #returns true if strings ends with substr 

print((str.capitalize()))  #capitalize 1st char
print(str)  #original variable remain unchanged

print(str.replace("o", "a"))  #replaces all occurrence of old
print(str)  #original variable remain unchanged

print(str.find("am"))  #returns 1st index of 1st occurrence
print(str.find("b"))  # -1, means b doesn't exist

print(str.count("a"))  #counts the occurrence of substr 