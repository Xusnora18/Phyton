# 1. Create and Access List Elements
fruits = ["apple", "banana", "cherry", "mango", "orange"]
print("1.", fruits[2])

# 2. Concatenate Two Lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print("2.", combined)

# 3. Extract Elements from a List
numbers = [10, 20, 30, 40, 50]
first = numbers[0]
middle = numbers[len(numbers) // 2]
last = numbers[-1]
new_list = [first, middle, last]
print("3.", new_list)

# 4. Convert List to Tuple
movies = ["Inception", "Avatar", "Titanic", "The Matrix", "Gladiator"]
movies_tuple = tuple(movies)
print("4.", movies_tuple)

# 5. Check Element in a List
cities = ["London", "Berlin", "Paris", "Madrid"]
print("5.", "Paris" in cities)

# 6. Duplicate a List Without Using Loops
nums = [1, 2, 3]
duplicated = nums * 2
print("6.", duplicated)

# 7. Swap First and Last Elements of a List
swap_list = [10, 20, 30, 40, 50]
swap_list[0], swap_list[-1] = swap_list[-1], swap_list[0]
print("7.", swap_list)

# 8. Slice a Tuple
numbers_tuple = tuple(range(1, 11))
print("8.", numbers_tuple[3:8])

# 9. Count Occurrences in a List
colors = ["blue", "red", "green", "blue", "yellow", "blue"]
print("9.", colors.count("blue"))

# 10. Find the Index of an Element in a Tuple
animals = ("cat", "dog", "lion", "tiger")
print("10.", animals.index("lion"))

# 11. Merge Two Tuples
t1 = (1, 2, 3)
t2 = (4, 5, 6)
merged = t1 + t2
print("11.", merged)

# 12. Find the Length of a List and Tuple
some_list = [1, 2, 3, 4]
some_tuple = (5, 6, 7)
print("12.", len(some_list), len(some_tuple))

# 13. Convert Tuple to List
num_tuple = (1, 2, 3, 4, 5)
num_list = list(num_tuple)
print("13.", num_list)

# 14. Find Maximum and Minimum in a Tuple
nums_tuple = (3, 7, 1, 9, 5)
print("14.", max(nums_tuple), min(nums_tuple))

# 15. Reverse a Tuple
words = ("apple", "banana", "cherry")
print("15.", words[::-1])
