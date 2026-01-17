# NumPy is a fundamental package for scientific computing in Python[cite: 495].
import numpy as np # [cite: 496]

# --- 1. CREATING ARRAYS ---
# The easiest way to create an array is to use the array() function.
# It accepts sequence-like objects (like lists) and produces a NumPy array[cite: 513, 514].
p = np.array([48.858598, 2.294495]) # [cite: 496]

# empty() creates a new array of a given shape without initializing elements[cite: 517].
empty_array = np.empty([3, 2], dtype=np.float64) # [cite: 518]

# ones() creates an array filled with 1s[cite: 524].
ones_array = np.ones(5) # [cite: 525]

# arange() creates an array with evenly spaced values in a given interval[cite: 531].
range_array = np.arange(2, 5) # [cite: 532]

# fromstring() creates a 1-D array from a text string[cite: 538].
string_array = np.fromstring('3.14 2.17', dtype=float, sep=' ') # [cite: 539]

# --- 2. ARRAY ATTRIBUTES ---
# You can inspect the properties of an array object.
print(p.ndim)   # Gets the dimension of the array [cite: 502]
print(p.shape)  # Gets the size of each array dimension [cite: 504]
print(len(p))   # Gets the dimension length [cite: 506]
print(p.dtype)  # Gets the data type (e.g., float64) [cite: 508]

# --- 3. NUMERICAL OPERATIONS ---
# NumPy allows mathematical operations on entire arrays without using for loops[cite: 540].
a = np.ones(4)
print(a * 2) # Multiplies every element by 2 [cite: 541]
print(a + 3) # Adds 3 to every element [cite: 541]

# --- 4. RESHAPING AND TRANSPOSING ---
# Transposing and reshaping return views of the data without copying it[cite: 544].
matrix = np.array([[0, 5, 10], [20, 25, 30]])
print(matrix.reshape(3, 2)) # Changes the shape to 3 rows, 2 columns [cite: 545]
print(matrix.T)             # Transposes the matrix (swaps rows and columns) [cite: 545]

# --- 5. MATHEMATICAL & STATISTICAL FUNCTIONS ---
# NumPy includes functions for trigonometry, rounding, and statistics[cite: 546, 547, 552].
angles = np.array([0., 30., 45.])
print(np.sin(angles * np.pi / 180)) # Sine function [cite: 546]

stats_array = np.array([[2, 4], [3, 5]])
print(np.sum(stats_array, axis=0))  # Sum of elements along an axis [cite: 554]
print(np.prod(stats_array, axis=1)) # Product of elements over an axis [cite: 556]
print(np.std(stats_array))          # Standard deviation [cite: 558]
print(np.var(stats_array))          # Variance [cite: 558]

# --- 6. SAVING AND LOADING DATA ---
# Arrays are saved by default in .npy binary format[cite: 559].
np.save('test1.npy', stats_array) # [cite: 559]

# Use savez() to store multiple arrays in a single .npz file[cite: 560].
np.savez('test2.npz', arr0=range_array, arr1=ones_array) # [cite: 561]

# Use load() or loadtxt() to bring data back into Python[cite: 562].
loaded_data = np.load('test1.npy') # [cite: 562]