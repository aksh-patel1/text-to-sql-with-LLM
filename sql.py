import sqlite3

# connect to database
connection = sqlite3.connect('student.db')

# create a cursor object to insert record, delete table, retrieve information
cursor = connection.cursor()

# create the table
table_info = """
CREATE TABLE STUDENT(
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT);
"""

cursor.execute(table_info)

# Insert Some more records

cursor.execute('''INSERT INTO STUDENT values('Aksh', 'Data Engineering', 'A', 93)''')
cursor.execute('''INSERT INTO STUDENT values('Vipasha', 'Data Engineering', 'A', 97)''')
cursor.execute('''INSERT INTO STUDENT values('Parv', 'Data Science', 'B', 83)''')
cursor.execute('''INSERT INTO STUDENT values('Purvi', 'Machine Learning', 'C', 73)''')

# Display all the records
print("The inserted records are:")

data = cursor.execute('SELECT * FROM STUDENT')

for row in data:
    print(row)

# Close the connection
connection.commit()
connection.close()