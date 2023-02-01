import numpy as np

# Import a list using np.array
sample_array = np.array([0,0,7])
print(type(sample_array))
print(dir(sample_array))

# Import a NumPy text file
# cat badges-five-numpy.txt
badges_saved_np = np.loadtxt('data\\badges-five-numpy.txt')
print(badges_saved_np)

# To check total number of elements
print(badges_saved_np.size)

# To see the dimension of the matrix
print(badges_saved_np.shape)

# Import a comma separated file, required to specify delimiter
# cat badges-five.txt
# badges_comma = np.loadtxt('data\\badges-five.txt') # error

# Above error was caused because the file is delimited
badges_comma = np.loadtxt('data\\badges-five.txt', delimiter=',')
badges_comma_subset = np.loadtxt('data\\badges-five.txt', delimiter=',', usecols=(0,2))
print(badges_comma)
print(badges_comma_subset)

# Import a comma separated file that has a header row
# cat badges-five-header.txt
# badges_header = np.loadtxt('data\\badges-five-header.txt', delimiter=',') # error
# Since file has a header, we will skip it
badges_header = np.loadtxt('data\\badges-five-header.txt', delimiter=',', skiprows=1) 
print(badges_header)

# # Import a comma separated file with header row and convert values to string
badges_str = np.loadtxt('data\\badges-five-header.txt', delimiter=',', skiprows=1, dtype=str) 

# Import and apply a function to one of the values
def Increase(the_id):
    return int(the_id) + 1000
# Converter option: pass in the column and function name
badges_increased = np.loadtxt('data\\badges-five.txt', delimiter=',', dtype=int, converters={0: Increase})
print(badges_increased)

# Import with a missing value, but still with loadtxt which raises an error
# cat badges-five-missing-value.txt
# badges_missing_value = np.loadtxt('data\\badges-five-missing-value.txt', delimiter=',', skiprows=1) #error
# print(badges_missing_value)

# Import with a missing value using genfromtxt
badges_missing_value = np.genfromtxt('data\\badges-five-missing-value.txt', delimiter=',')
print(f"Printing badges_missing_value: {badges_missing_value}")

# We need to skip the header, and then we explore our data with size and shape
badges_missing_value = np.genfromtxt('data\\badges-five-missing-value.txt', delimiter=',', skip_header=1)
print(f"Printing badges_missing_value without header: {badges_missing_value}")

# And you can specify what to do with missing values, i.e. fill with another value
badges_missing_value = np.genfromtxt('data\\badges-five-missing-value.txt', delimiter=',', skip_header=1, filling_values=0)
print(f"Printing badges_missing_value with specified value: {badges_missing_value}")
