
try:
    answer = 10/0
    number = int(input("Enter a number: "))
    print(number)
# below is the catch
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid input")
