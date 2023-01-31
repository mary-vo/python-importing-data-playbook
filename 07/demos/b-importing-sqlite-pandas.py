# Import data from SQLite using pandas
import pandas as pd 
import sqlite3
stack_connection = sqlite3.connect('samples\\importing_sqlite.db') 
posts_df = pd.read_sql("select * from posts;", stack_connection) 
# This returns a dataframe
print(type(posts_df))
# See the columns
print(posts_df.columns)
# See the data
print(posts_df.head())

