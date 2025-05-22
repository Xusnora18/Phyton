# 1. Sort a Dictionary by Value
my_dict = {'a': 3, 'b': 1, 'c': 2}
ascending = dict(sorted(my_dict.items(), key=lambda item: item[1]))
descending = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("1. Ascending:", ascending)
print("1. Descending:", descending)

# 2. Add a Key to a Dictionary
d = {0: 10, 1: 20}
d[2] = 30
print("2.", d)

# 3. Concatenate Multiple Dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
new_dict = {}
for d in (dic1, dic2, dic3):
    new_dict.update(d)
print("3.", new_dict)

# 4. Generate a Dictionary with Squares (up to n)
n = 5
squares = {x: x*x for x in range(1, n+1)}
print("4.", squares)

# 5. Dictionary of Squares from 1 to 15
squares_15 = {x: x*x for x in range(1, 16)}
print("5.", squares_15)

# 1. Create a Set
my_set = {1, 2, 3}
print("Set 1:", my_set)

# 2. Iterate Over a Set
print("Set 2:")
for item in my_set:
    print(item)

# 3. Add Member(s) to a Set
my_set.add(4)
my_set.update([5, 6])
print("Set 3:", my_set)

# 4. Remove Item(s) from a Set
my_set.discard(2)
print("Set 4:", my_set)

# 5. Remove an Item if Present in the Set
if 3 in my_set:
    my_set.remove(3)
print("Set 5:", my_set)
