import pandas as pd

# Create ExcelFile
excel_file = pd.ExcelFile('sample\\stackoverflow.xlsx')
print(type(excel_file))
print(excel_file.sheet_names)

# Parse into DataFrame
# Load worksheet into a pandas DataFrame
excel_df = excel_file.parse()
print(excel_df.head(3))
print(type(excel_df))


# Or use pandas directly to load worksheet, with read_excel
posts_excel = pd.read_excel('sample\\stackoverflow-one.xlsx')
# type(posts_excel)
# Check all the options available for this dataframe
# print(dir(posts_excel))
print(posts_excel.columns)
print(posts_excel.head())
# Indicate the columns to return
print(pd.read_excel('sample\\stackoverflow-one.xlsx', usecols=[0, 3]).columns)
# Indicate a range of columns to return
print(pd.read_excel('sample\\stackoverflow-one.xlsx', usecols='A:C').columns)
# Indicate specific columns to return from the sheet
print(pd.read_excel('sample\\stackoverflow-one.xlsx', usecols='A,C').columns)

# Get a dict of worksheets
print(excel_file.sheet_names)
posts_dict = pd.read_excel('sample\\stackoverflow.xlsx',sheet_name=None)
print(posts_dict)
print(type(posts_dict))
print(posts_dict.keys())
print(posts_dict['Posts'].head())

# # Different ways of getting the data you need
# To return a specific sheet / key from the dictionary of sheets
print(posts_dict['Users'].head())
# To call a specific sheet
print(pd.read_excel('sample\\stackoverflow.xlsx',sheet_name='Users').head())
# You can specific specific columns in the sheet
print(pd.read_excel('sample\\stackoverflow.xlsx',sheet_name='Users', usecols=range(1,9)).head())
# Passing an integer in sheet_name will return the indexed number of the sheet
print(pd.read_excel('sample\\stackoverflow.xlsx',sheet_name=2).head())
# Skip rows, telling pandas how many rows to ignore/skip
print(pd.read_excel('sample\\stackoverflow.xlsx',sheet_name=2, usecols=range(1,9),skiprows=4).head())
# Specificy nrows meaning how many row syou want to return
print(pd.read_excel('sample\\stackoverflow.xlsx',sheet_name=2, usecols=range(1,9),nrows=2).head())
# See type of your data
print(pd.read_excel('sample\\stackoverflow.xlsx',sheet_name='Users', skiprows=1).dtypes)
# Control the type of your data with parameter dtype
print(pd.read_excel('sample\\stackoverflow.xlsx',sheet_name='Users', skiprows=1, dtype={'PostTypeId': str}).dtypes)
# Converters or pass a function to all values
print(pd.read_excel('sample\\stackoverflow.xlsx',sheet_name='Users', skiprows=1, converters={'Id': lambda x: x + 1000}).head())
# This returns NaN (not a number)
print(pd.read_excel('sample\\stackoverflow.xlsx',sheet_name='Posts', usecols=[0,7,8]).head())
# If you don't want NaN set keep_default_na and you won't get NaN it will just be empty
print(pd.read_excel('sample\\stackoverflow.xlsx',sheet_name='Posts', usecols=[0,7,8], keep_default_na=False).head())

