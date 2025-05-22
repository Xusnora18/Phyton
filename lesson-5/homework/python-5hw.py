# 1. Leap Year Checker
def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

print("1.", is_leap(2024))  # Example: True


# 2. Conditional Statements Exercise
n = 3  # Example input

if n % 2 != 0:
    print("2. Weird")
elif n in range(2, 6):
    print("2. Not Weird")
elif n in range(6, 21):
    print("2. Weird")
else:
    print("2. Not Weird")


# 3. Find even numbers between a and b (inclusive)

a = 2
b = 10

# Solution 1: Using if-else (indirectly with list comprehension and condition inside)
evens_1 = [x for x in range(a, b+1) if x % 2 == 0]
print("3.1", evens_1)

# Solution 2: Without if-else (using step in range)
start = a if a % 2 == 0 else a + 1
evens_2 = list(range(start, b+1, 2))
print("3.2", evens_2)
