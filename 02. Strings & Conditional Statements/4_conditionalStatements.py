'''
if - elif - else (SYNTAX)

if(condition):
    statement1
elif(condition):
    statement2
else:
    statement3
'''

#if-else
age = 12
if(age >= 18):
    print("Congratulations! You'll get a license")
    print("You can vote")
else:
    print("Sorry try again", 18-age, "years later!")

#if-elif-else
light = "green"
if(light == "red"):
    print("stop")
elif(light == "yellow"):
    print("look!")
elif(light == "green"):
    print("go!")
else:
    print("light is broken")

#nesting
age2 = 65
if(age2 >= 18):
    if(age2 >= 60):
        print("You can't drive")
    else:
        print("You can drive")
else:
    print("You can't drive")