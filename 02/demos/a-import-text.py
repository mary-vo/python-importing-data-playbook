# How to read a plain text file
which_file = "Creative Commons Attribution-ShareAlike 3.0 Unported.txt"
license_file = open(which_file, mode='r')
license_name = license_file.readline()
print(license_name)

# Read the entire contents of the file
license = license_file.read()
license_file.close()
print(license)

# Same as above, but using a context manager to avoid having to explicitly close the file
# Using 'with open' will automatically close() files
with open (which_file, 'r') as file:
    print(file.read())

