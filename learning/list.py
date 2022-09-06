
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

# lists
# if you want last item in list you ca do [-1] this is good because you don't need to know the length of list
# slicing
# appending- will add entire list into a single index of list
# extend- adds individual indexed items into list
# pop- deletes last index and returns it
# sorted- doesn't alter the OG list
# join- turning list into strings
# split- will let you define ' , ' and will parse out those and create a list