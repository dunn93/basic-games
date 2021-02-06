
friends = ["kevin", "karen", "jim"]
lucky_numbers = [4, 8, 15, 16, 23]
# use [] for lists structures
# you can put different kinds of data types in a list
# can use negatives to start at the back of the list, -2 = jim
# 1: will select index 1 and everything after
# 1:2 will only select index 1 and 2

print(friends[0])
friends.extend(lucky_numbers)
print(friends)

# insert function will insert item at a specific index
# append will add to end of list
# pop will remove last item from list
# can sort, count, reverse list, copy, etc.

print(friends.index("kevin"))
