# if you use W it will overwrite everything in the existing file
# or if you rename txt file it will create a new file for you
employee_file = open("employees.txt", "a")
# \n creates a new line (this is called an escape character
employee_file.write("\nKelly - Customer Service")
employee_file.close()

# summary: you can do the following with external files
# overwrite (w), create new (w), add to a file (a), and read (r)