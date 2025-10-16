import sqlite3

# connect to the database
conn = sqlite3.connect('employee.db')
cursor = conn.cursor()

print("Before deleting all employees:")
print(cursor.execute("SELECT * FROM employees").fetchall())

# delete all employee records for testing purposes
cursor.execute("DELETE FROM employees")

print("After deleting all employees:")
print(cursor.execute("SELECT * FROM employees").fetchall())

# commit changes and close the connection
conn.commit()
conn.close()