def modify_string(txt):
    result = []
    i = 0
    while i < len(txt):
        result.append(txt[i])
        if (i + 1) % 3 == 0 and i + 1 < len(txt):
            if txt[i] not in "aeiouAEIOU" and (i + 1 == len(txt) - 1 or txt[i+1] != '_'):
                result.append('_')
        i += 1
    return ''.join(result)

print("1.", modify_string("abcabcabcdeabcdefabcdefg"))


n = 5
print("2.")
for i in range(n):
    print(i * i)

# 3.1 Print first 10 natural numbers
print("3.1")
i = 1
while i <= 10:
    print(i)
    i += 1

# 3.2 Pattern
print("3.2")
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=' ')
    print()

# 3.3 Sum from 1 to given number
print("3.3")
num = 10
total = sum(range(1, num + 1))
print("Sum is:", total)

# 3.4 Multiplication table
print("3.4")
n = 2
for i in range(1, 11):
    print(n * i)

# 3.5 Display numbers from list
print("3.5")
numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if 75 <= num <= 150:
        print(num)

# 3.6 Count digits
print("3.6")
num = 75869
print("Output:", len(str(num)))

# 3.7 Reverse number pattern
print("3.7")
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print()

# 3.8 Reverse list
print("3.8")
list1 = [10, 20, 30, 40, 50]
for item in reversed(list1):
    print(item)

# 3.9 Numbers from -10 to -1
print("3.9")
for i in range(-10, 0):
    print(i)

# 3.10 Done message
print("3.10")
for i in range(5):
    print(i)
print("Done!")

# 3.11 Prime numbers in range
print("3.11")
for num in range(25, 51):
    if num > 1:
        for i in range(2, int(num ** 0.5)+1):
            if num % i == 0:
                break
        else:
            print(num)

# 3.12 Fibonacci series
print("3.12")
a, b = 0, 1
for _ in range(10):
    print(a, end=' ')
    a, b = b, a + b
print()

# 3.13 Factorial
print("3.13")
n = 5
fact = 1
for i in range(1, n+1):
    fact *= i
print(f"{n}! = {fact}")


print("4.")
list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]

from collections import Counter

c1 = Counter(list1)
c2 = Counter(list2)
result = list((c1 - c2).elements()) + list((c2 - c1).elements())
print(result)










