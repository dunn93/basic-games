
# num1 = input("Enter a number: ")
# num2 = input("Enter another number: ")
# result = float(num1) + float(num2)
#
# print(result)

#you do this because input is always created as a String data type and for a calc we want a number data type
#it also means if they don't enter a number nothing will happen
num3 = float(input("Enter first number: "))
op = input("Enter an operator: ")
num4 = float(input("Enter a number: "))

#add message for answer
if op == "+":
    print(num3 +num4)
elif op == "-":
    print(num3 - num4)
elif op == "/":
    print(num3 / num4)
elif op == "*":
    print(num3 * num4)
else:
    print("error: invalid operator")


