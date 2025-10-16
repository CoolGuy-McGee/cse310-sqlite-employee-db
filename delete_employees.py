import sqlite3

# connect to the database
conn = sqlite3.connect('employee.db')
cursor = conn.cursor()

print("Before firings:")
print(cursor.execute("SELECT * FROM employees").fetchall())

# delete employee records for 3 employees
cursor.execute("DELETE FROM employees WHERE first=? AND last=?", ('Oliver', 'Brown'))
cursor.execute("DELETE FROM employees WHERE first=? AND last=?", ('Mateo', 'Hernandez'))
cursor.execute("DELETE FROM employees WHERE first=? AND last=?", ('Harper', 'Sinclair'))

print("After firings:")
print(cursor.execute("SELECT * FROM employees").fetchall())

# commit changes and close the connection
conn.commit()
conn.close()