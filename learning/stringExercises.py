print("Hello \n World")

#a variable is just a container to hold data
# different data types = String, number (includes int and floats), boolean, etc
# \n creates a new line in a string
# \" will print a quotation mark in string
# there are functions for strings that can convert strings to all upper/lower or tell you if
# the string is all upper/lower with true/false output

character_name = "Mariah"
character_age = "26"
is_female = True

print("There once was a girl trying to learn python")
print("her name was " + character_name)
print("she was " + character_age + " years old.")

# len() function will tell you length of string
# can grab individual characters by [0]
# you can also pass it a character to find it's index like phrase.index("y") would return 0

phrase = "youtube"
print(len(phrase))
print(phrase[1])
print(phrase.replace("you", "me"))