# Pandas works well for tabular data: relations or labeled data, columsn of different types
# Can perform operations on your data like data manipulation ahd analysis, numerical and time series date

import pandas as pd

# Import data using pandas with read_csv
posts_csv = pd.read_csv('data\\posts-100.csv')
print(type(posts_csv))
print(posts_csv)
print(posts_csv.head()) # defaults to 5 rows
print(posts_csv.head(3))

# You can get the numpy array from the DataFrame 
print(posts_csv.values)
print(type(posts_csv.values))

## Import from a URL
## This URL is not working
# remote_file = 'https://raw.githubusercontent.com/xmorera/sample-data/master/csv/posts-100.csv'
# posts_url = pd.read_csv(remote_file, header=None)
# posts_url.head()

# # You can read a small number of lines too
posts_small = pd.read_csv('data\\posts-100.csv', nrows=3)
print(posts_small)
posts_small = pd.read_csv('data\\posts-100.csv', nrows=3, skiprows=3)
print(posts_small)

# Use a lambda to specify which rows to skip
# Specify which rows to load using a function
# Referred to as a callable, use a named function or anonymous funtion
# Evaluate against row indices and determine which rows to skip
posts_odd = pd.read_csv('data\\posts-100.csv', skiprows=lambda x: x % 2 != 0) # this is an anonymous function
posts_odd.head()

# You can also specify that you want to load only certain columns
posts_columns = pd.read_csv('data\\posts-100.csv', usecols=[0,6,7,8])
posts_columns.head(5)

# The DataFrame gives a name to columns, but this does not look right
print(posts_columns.columns)

# # So we specify that the file does not have a header, and now labels are added automatically
posts_no_header = pd.read_csv('data\\posts-100.csv', header=None)
print(posts_no_header.columns)

# And you can add a prefix for column names when no header info exists
# This will literally insert 'Col' prefix in front of the indexed column number
posts_prefix = pd.read_csv('data\\posts-100.csv', header=None, prefix='Col')
print(posts_prefix.columns)

# And you can add column names
header_fields = ['New_Id', 'New_PostTypeId', 'New_CreationDate', 'New_Score', 'New_ViewCount', 'New_LastActivityDate', 'New_Title', 'New_Tags', 'New_AnswerCount', 'New_CommentCount', 'New_FavoriteCount', 'New_ClosedDate']
posts_add_header = pd.read_csv('data\\posts-100.csv', names=header_fields)
print(posts_add_header)

# Even easier if headers are included in the file
posts_header = pd.read_csv('data\\posts-100-header.csv') 
print(posts_header.columns)

# Headers are important because you can use them to refer to columns
print(posts_header[['AnswerCount']].head())
print(posts_header[['Id','PostTypeId']].head())

# You can also use infer and read_csv will automatically determine if the file contains a header
infer_header = pd.read_csv('data\\posts-100-header.csv', header='infer').columns
print(infer_header)
infer_header = pd.read_csv('data\\posts-100-header.csv', header=None).columns # If header=None, Returns indecies only

# Although you might want to actually remove the headers
pd.read_csv('data\\posts-100-header.csv', skiprows=1).head()

# Specify types
print(pd.read_csv('data\\posts-100-header.csv', usecols=[0, 1, 2, 7]).head())
print(pd.read_csv('data\\posts-100-header.csv', usecols=[0, 1, 2, 7]).columns)
print(pd.read_csv('data\\posts-100-header.csv', usecols=[0, 1, 2, 7]).dtypes)
print(pd.read_csv('data\\posts-100-header.csv', usecols=[0, 1, 2, 7], dtype={'PostTypeId': str}).dtypes)
print(pd.read_csv('data\\posts-100-header.csv', usecols=[0, 1, 2, 7], dtype={'PostTypeId': float}).dtypes)


# Apply a function with a regular expression
post_tags = pd.read_csv('data\\posts-100-header.csv', usecols=[0, 1, 2, 7])
print(post_tags.iloc[1]) # To return a row by integer location
print(post_tags.iloc[1]['Tags']) # This returns a string that contains a list
# How to convert the string to an actual list? Use converter
import re
# In the converter tell it which column you want to apply the function to (i.e. 'Tags')
posts_tags_convert = pd.read_csv('data\\posts-100-header.csv', usecols=[0, 1, 2, 7], converters={'Tags': lambda x: re.findall('<[A-Za-z0-9_-]*>',x)})
print(posts_tags_convert.head(3))
print(type(posts_tags_convert.iloc[1]['Tags']))
print(posts_tags_convert.iloc[1]['Tags'])

# Work with dates too
posts_date = pd.read_csv('data\\posts-100-header.csv', usecols=[0, 1, 2, 7])
print(posts_date.dtypes) # Type is object
print(type(posts_date['CreationDate'][0]))
posts_date = pd.read_csv('data\\posts-100-header.csv', usecols=[0, 1, 2, 7], parse_dates=['CreationDate'])
print(posts_date.dtypes)
print(type(posts_date['CreationDate'][0]))

# Let's see some missing values
posts_missing = pd.read_csv('data\\posts-100-header.csv', usecols=[0, 3, 4, 8, 9, 10]).head(5)
print(posts_missing)

# Work with missing values
print(pd.read_csv('data\\posts-100-header.csv', usecols=[0, 3, 4, 8, 9, 10], na_filter=False).head())
print(pd.read_csv('data\\posts-100-header.csv', usecols=[0, 3, 4, 8, 9, 10], na_filter=True).head())
print(pd.read_csv('data\\posts-100-header.csv', usecols=[0, 3, 4, 8, 9, 10], dtype={'ViewCount': float}, na_filter=True).head())

# Now with a tsv file, there is an error unless you set sep or delimiter
# This fails because the file is tab delimited, but pandas tried to load separating by commas instead
## posts_tsv = pd.read_csv('data\\posts-100.tsv') # Error
## print(posts_tsv)
posts_tsv = pd.read_csv('data\\posts-100.tsv', sep='\t')
print(posts_tsv.head())
posts_tsv = pd.read_csv('data\\posts-100.tsv', delimiter='\t')
print(posts_tsv.head())
# You can also use read_table for tab delimited file
posts_tsv =  pd.read_table('data\\posts-100.tsv')
posts_tsv.head()