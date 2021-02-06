# this means from the student file, import the student class
# classes let you model real world items and we can create our own data types
from Student import Student

# here we are creating a student object
student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Phylis", "Business", 3.8, False)

print(student1.on_honor_roll())

# to inherit a functions and everything from a class in python you'd do class name(inheritance class)

