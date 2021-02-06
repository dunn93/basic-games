# Real life example:
# Im at a restaurant
# if I want meat
#     I order a steak
# otherwise if I want pasta
#     I order spaghetti and meatballs
# otherwise
#     I order a salad

# or is either statments true, and means both have to be correct

is_male = False
is_tall = False

if is_male and is_tall:
    print("you identify as male or you're tall or both")
elif is_male and not(is_tall):
    print("you are a short male")
elif is_tall and not(is_male):
    print("you not male but tall")
else:
    print("you do not identify as male ant you are short")

#if statements and comparisons tutorial

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(3,40,5))