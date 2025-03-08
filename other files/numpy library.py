import numpy as np

a = np.arange(1, 10).reshape((3,3)) # makes a random array [basically a matrix]
b = np.arange(1, 10).reshape((3,3))
# a[:] = 2 # fills the array with 2 elements
# a.fill (8) # fills the array with that number
a+= 3 # adds the number to the array
array_sum = a.sum()
array_sum = a.sum(0) # adds the coulmns of the array
array_sum = a.sum(1) # adds the rows of the array
array_prodcut = a.prod() # calculates the product of the array
array_average = a.mean() # calculates the average of the array
array_max = a.max() # calculates the maximum of the array
array_min = a.min() # calculates the minimum of the array
array_flat = a.flatten() # flattens the array
array_flat2 = a.ravel() # flattens the array
array_repeat = np.repeat(a, 3) # repeats the array
array_repeat_rows = np.repeat(a, 3, axis= 1) # repeats the array in rows
array_repeat_columns = np.repeat(a, 3, axis= 0) # repeats the array in columns
array_unique = np.unique(array_repeat , 3) # removes duplicates in  the array
array_diagonal = np.diagonal(a) # returns the diagonal of the array
array_diagonal_above = np.diagonal(a, offset= 1) # returns the diagonal above the first element of the array
array_diagonal_below = np.diagonal(a, offset= -1) # returns the diagonal below the first element of the array
my_list = a.tolist() # converts the array to a list
a.tofile("my_array.txt", sep = ",") # creates a new file
array_swapped = np.swapaxes(a, 0, 1) # creates a transpose (swapping rows and columns)
array_swapped_2 = a.transpose(0,1) # creates a transpose (swapping rows and columns)
array_swapped_3 = a.T # creates a transpose (swapping rows and columns)
simple_opps = a + b # adding two matrix
simple_opps_2 = a - b # subtract two matrix
simple_opps_3 = a * b # multiply two matrix (elemants)
modulo = a % b # gives the remainder of 2 matrix
floor_division = a // b #it ignores floating point division in integers
floor_division_1 = np.floor(a/b) # it ignores floating point division in floats
matrix_multiplication = np.matmul(a, b) # multiplies two matrix
matrix_multiplication_dot = a.dot(b) # dot product of two matrix
matrix_multiplication_at = a @ b # matrix multiplication
matrix_lcm = np.lcm(a, b)  # finds the lcm of the matrix
matrix_gcd = np.gcd(a, b) # finds the gcd of the matrix
matrix_log_a = np.log(a) # finds the log of the matrix
matrix_log_b = np.log(b) # finds the log of the matrix

print("Original matrix a:", a)
print("Sum of all elements:", array_sum)
print("Product of all elements:", array_prodcut)
print("Average value:", array_average)
print("Maximum value:", array_max)
print("Minimum value:", array_min)
print("Flattened array (flatten):", array_flat)
print("Flattened array (ravel):", array_flat2)
print("Repeated array elements:", array_repeat)
print("Row-wise repeated array:", array_repeat_rows)
print("Column-wise repeated array:", array_repeat_columns)
print("Unique elements:", array_unique)
print("Main diagonal:", array_diagonal)
print("Diagonal above main:", array_diagonal_above)
print("Diagonal below main:", array_diagonal_below)
print("Array converted to list:", my_list)
print("Type of a:", type(a))
print("Type of my_list:", type(my_list))
print("Swapped axes (transpose):", array_swapped)
print("Transposed array (method 1):", array_swapped_2)
print("Transposed array (method 2):", array_swapped_3)
print("Element-wise addition:", simple_opps)
print("Element-wise subtraction:", simple_opps_2)
print("Element-wise multiplication:", simple_opps_3)
print("Element-wise modulo:", modulo)
print("Floor division:", floor_division)
print("Floor division (float):", floor_division_1)
print("Matrix multiplication:", matrix_multiplication)
print("Dot product:", matrix_multiplication_dot)
print("Matrix multiplication (@):", matrix_multiplication_at)
print("LCM matrix:", matrix_lcm)
print("GCD matrix:", matrix_gcd)
print("Natural log of a:", matrix_log_a)
print("Natural log of b:", matrix_log_b)