
import numpy as np

# 1. Convert List to 1D Array
original_list = [12.23, 13.32, 100, 36.32]
array_1d = np.array(original_list)
print("1. One-dimensional NumPy array:")
print(array_1d)

# 2. Create 3x3 Matrix (2–10)
matrix_3x3 = np.arange(2, 11).reshape(3, 3)
print("\n2. 3x3 Matrix from 2 to 10:")
print(matrix_3x3)

# 3. Null Vector (10) & Update Sixth Value
null_vector = np.zeros(10)
null_vector[6] = 11
print("\n3. Null vector with sixth value updated to 11:")
print(null_vector)

# 4. Array from 12 to 38
array_12_38 = np.arange(12, 38)
print("\n4. Array with values from 12 to 38:")
print(array_12_38)

# 5. Convert Array to Float Type
array_int = np.array([1, 2, 3, 4])
array_float = array_int.astype(float)
print("\n5. Array converted to float type:")
print(array_float)

# 6. Celsius to Fahrenheit Conversion
celsius = np.array([-17.78, -11.11, 7.34, 1.11, 37.73, 0.])
fahrenheit = celsius * 9/5 + 32
print("\n6. Celsius to Fahrenheit:")
print("Celsius:", celsius)
print("Fahrenheit:", fahrenheit)

# 7. Append Values to Array
original_array = np.array([10, 20, 30])
appended_array = np.append(original_array, [40, 50, 60, 70, 80, 90])
print("\n7. Appended array:")
print(appended_array)

# 8. Array Statistical Functions
random_array = np.random.rand(10)
mean_val = np.mean(random_array)
median_val = np.median(random_array)
std_dev = np.std(random_array)
print("\n8. Random array statistics:")
print("Array:", random_array)
print("Mean:", mean_val)
print("Median:", median_val)
print("Standard Deviation:", std_dev)

# 9. Find min and max in 10x10 array
array_10x10 = np.random.rand(10, 10)
min_val = np.min(array_10x10)
max_val = np.max(array_10x10)
print("\n9. 10x10 random array:")
print("Minimum value:", min_val)
print("Maximum value:", max_val)

# 10. Create a 3x3x3 array with random values
array_3x3x3 = np.random.rand(3, 3, 3)
print("\n10. 3x3x3 random array:")
print(array_3x3x3)
