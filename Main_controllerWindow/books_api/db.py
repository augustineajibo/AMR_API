import sqlite3
conn = sqlite3.connect("books.sqlite")

#create cursor object
cursor = conn.cursor()
#define sql query to create the table
sql_query = """CREATE TABLE book(
    id integer PRIMARY KEY,
    author text Not NULL,
    language text Not NULL,
    title text Not NULL

)"""

cursor.execute(sql_query)