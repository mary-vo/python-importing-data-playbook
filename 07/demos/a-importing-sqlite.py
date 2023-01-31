# Import data from SQLite using sqlite3
import sqlite3
# ls
stack_connection = sqlite3.connect('samples\\importing_sqlite.db')
print(type(stack_connection))
# Use a cursor to iterate over the rows returned as results
stack_cursor = stack_connection.cursor()
stack_cursor.execute("select name from sqlite_master where type = 'table';")
print(stack_cursor.fetchone())
print(stack_cursor.fetchall())

# Careful on names
# ls -l 
# When you try to open a new db with the wrong name, a new database gets created. WHAT?!!!
# stack_connection_bad = sqlite3.connect('bad_name_sqlite.db')
# stack_connection_bad.cursor().execute("select name from sqlite_master where type = 'table';").fetchall()
# # ls -l

# Query your data
rows = stack_cursor.execute('select * from posts').fetchall()
print(type(rows))
print(rows[0])
print(type(rows[0]))
# Limit the number of results
stack_cursor.execute('select * from posts limit 1').fetchall()
# Selecting just a few columns
stack_cursor.execute('select Id, Score, Tags from posts limit 3').fetchall()