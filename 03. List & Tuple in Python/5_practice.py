# Write a program to ask the user to enter names of their 3 favorite movies & enter them in a list
movies = []

movie = input("Enter 1st movie: ")
movies.append(movie)

movie = input("Enter 2nd movie: ")
movies.append(movie)

movies.append(input("Enter 3rd movie: "))

print(movies)

# Write a program to check if a list contains a palindrome of elements. (Hint: use copy() method)
list = [1, 2, 3, 2, 1]
listCopy = list.copy()
listCopy.reverse()

if(list == listCopy):
    print("Palindrome")
else:
    print("Not Palindrome")

# Write a program to count the number of students with the "A" grade in the following tuple ("C", "D", "A", "A", "B", "B", "A")
grade = ("C", "D", "A", "A", "B", "B", "A")
print(grade.count("A"))

# Write a program to store the above value in a list $ sort them to "A" to "D"
marks = ["C", "D", "A", "A", "B", "B", "A"]
marks.sort()
print(marks)