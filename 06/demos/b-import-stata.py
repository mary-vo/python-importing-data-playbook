# Read stata files with pandas
# Import stata with pandas
import pandas as pd
# Load data into pandas dataframe
posts_stata = pd.read_stata('samples\\posts-100.dta')
# Confirm the type is pandas dataframe
print(type(posts_stata))
# See all the available functionalities
print(dir(posts_stata))
# Look at our columns
print(posts_stata.columns)
# Check data using head
print(posts_stata.head())
