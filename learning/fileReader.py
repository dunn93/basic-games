# how to read an external file
# need absolute path if not in same directory
# after the comma is the mode you want like read, write, append (add new info), read and write (r+)
# here we are saving the info in txt file into variable
# every time you open a file you need to close a it

employee_file = open("employees.txt", "r")
for employee in employee_file.readlines():
    print(employee)
# .readable tells you if the file is readable or not
# .readline just reads one line at a time starting with the first
# .readlines puts all lines in an array and prints it out for you
# you can then specific specific lines with their index
# print(employee_file.read())

employee_file.close()