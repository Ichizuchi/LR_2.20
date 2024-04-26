import csv
import sqlite3

# Connecting to the cats database
connection = sqlite3.connect('cats.db')

# Creating a cursor object to execute SQL queries on a database table
cursor = connection.cursor()

# Table Definition
create_table = '''CREATE TABLE cats (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Hair_Length REAL NOT NULL,
                Hair_Width REAL NOT NULL,
                Tail_Length REAL NOT NULL,
                Tail_Width REAL NOT NULL,
                Breed TEXT NOT NULL);
                '''

# Creating the table into our database
cursor.execute(create_table)

# Opening the cats.csv file
with open('cats.csv', newline='') as file:
    # Reading the contents of the cats.csv file
    contents = csv.reader(file)
    # Skip the header row
    next(contents)
    # SQL query to insert data into the cats table
    insert_records = "INSERT INTO cats (Hair_Length, Hair_Width, Tail_Length, Tail_Width, Breed) VALUES (?, ?, ?, ?, ?)"
    # Importing the contents of the file into our cats table
    cursor.executemany(insert_records, contents)

# SQL query to retrieve all data from the cats table to verify that the data of the csv file has been successfully inserted into the table
select_all = "SELECT * FROM cats"
rows = cursor.execute(select_all).fetchall()

# Output to the console screen
for r in rows:
    print(r)

# Committing the changes
connection.commit()

# Closing the database connection
connection.close()
