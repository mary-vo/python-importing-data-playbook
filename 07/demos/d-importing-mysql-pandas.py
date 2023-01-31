## THIS WHOLE THING DOES NOT WORK?

# Import data from MySQL with pandas
# show databases;
# use importing_mysql
# show tables;
import mysql
from sqlalchemy import create_engine
import pandas as pd
engine = create_engine('mysql+mysqlconnector://root:mysql@localhost:3306/importing_mysql')
posts = pd.read_sql_table('posts', engine, index_col='Id')
print(type(posts))
print(engine.table_names())
print(posts.columns)
print(posts.head())

# Several parameters available
posts = pd.read_sql_table('posts', engine, columns=['Id', 'CreationDate', 'Tags'])
print(posts.head())
# type(posts.iloc(1)[1])
# posts = pd.read_sql_table('posts', engine, columns=['Id', 'CreationDate', 'Tags'], parse_dates={'CreationDate': {'format': '%Y-%m-%dT%H:%M:%S.%f'}})
# type(posts.iloc(1)[1])
