# Task 2: Custom Modules

# math_operations module
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

# string_utils module
def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    return sum(1 for char in s.lower() if char in 'aeiou')

# Task 3: Custom Packages

# geometry/circle.py
def calculate_area(radius):
    return 3.141592653589793 * radius * radius

def calculate_circumference(radius):
    return 2 * 3.141592653589793 * radius

# file_operations/file_reader.py
def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()

# file_operations/file_writer.py
def write_file(file_path, content):
    with open(file_path, 'w') as f:
        f.write(content)
