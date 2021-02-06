
# main python data types = strings, integers, and booleans
# if you want more you can create your own data types with a class by describing their attributes
# class is defining what a student is
# an object is an actual student

class Student:

    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

# function in a class to help the user find/modify info about object
    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False