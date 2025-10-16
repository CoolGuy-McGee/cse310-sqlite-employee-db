import sqlite3

# connect to the database
conn = sqlite3.connect('employee.db')
cursor = conn.cursor()

# filter employees hired before 2020-01-01
print("Employees hired before 2020-01-01:")
cursor.execute("SELECT * FROM employees WHERE hire_date < '2020-01-01'")
print(cursor.fetchall())

# commit changes and close the connection
conn.commit()
conn.close()