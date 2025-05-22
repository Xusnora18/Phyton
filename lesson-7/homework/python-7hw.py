# MAP and FILTER examples with lambda
nums = [1, 2, 3, 4, 5]

# map example: square each number
squares = list(map(lambda x: x ** 2, nums))
print("map example:", squares)

# filter example: keep even numbers
evens = list(filter(lambda x: x % 2 == 0, nums))
print("filter example:", evens)


# 1. is_prime(n)
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print("is_prime(4):", is_prime(4))  # False
print("is_prime(7):", is_prime(7))  # True


# 2. digit_sum(k)
def digit_sum(k):
    return sum(int(i) for i in str(k))

print("digit_sum(24):", digit_sum(24))  # 6
print("digit_sum(502):", digit_sum(502))  # 7


# 3. 2 powers <= N
def powers_of_two(N):
    k = 1
    while (2 ** k) <= N:
        print(2 ** k, end=' ')
        k += 1

print("\npowers_of_two(10):")
powers_of_two(10)  # 2 4 8
