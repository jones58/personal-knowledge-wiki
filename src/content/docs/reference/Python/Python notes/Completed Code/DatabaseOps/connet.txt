import sqlite3 as sql # import the sqlite module and assign it an Alias 'sql'

# To use the sqlite module 
"Create a variable called dbCon"
dbCon = sql.connect("Python/Week2/DatabaseOps/dfe3w4.db")

# create cursor object using the cursor method to run sql queries
"dbCursor is a variable"
dbCursor = dbCon.cursor() # cursor() is a method

