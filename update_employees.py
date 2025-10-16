import sqlite3

# connect to the database
conn = sqlite3.connect('employee.db')
cursor = conn.cursor()

print("Before update:")
print(cursor.execute("SELECT * FROM employees").fetchall())

# update some employee records
# change last names for 4 female employees
cursor.execute("UPDATE employees SET last=? WHERE first=? AND last=?", ('Johnson', 'Jane', 'Smith'))
cursor.execute("UPDATE employees SET last=? WHERE first=? AND last=?", ('Ahmed', 'Aisha', 'Khan'))
cursor.execute("UPDATE employees SET last=? WHERE first=? AND last=?", ('Singh', 'Maya', 'Patel'))
cursor.execute("UPDATE employees SET last=? WHERE first=? AND last=?", ('Carter', 'Isabella', 'Rivera'))

# give raises to 6 employees (round numbers between 2000 and 7000)
cursor.execute("UPDATE employees SET pay = pay + ? WHERE first=? AND last=?", (5000, 'Liam', "OConnor"))
cursor.execute("UPDATE employees SET pay = pay + ? WHERE first=? AND last=?", (2000, 'Oliver', 'Brown'))
cursor.execute("UPDATE employees SET pay = pay + ? WHERE first=? AND last=?", (7000, 'Samuel', 'Brooks'))
cursor.execute("UPDATE employees SET pay = pay + ? WHERE first=? AND last=?", (3000, 'Victoria', 'Lee'))
cursor.execute("UPDATE employees SET pay = pay + ? WHERE first=? AND last=?", (6000, 'Mateo', 'Hernandez'))
cursor.execute("UPDATE employees SET pay = pay + ? WHERE first=? AND last=?", (4000, 'Benjamin', 'Clark'))

print("After update:")
print(cursor.execute("SELECT * FROM employees").fetchall())

# commit changes and close the connection
conn.commit()
conn.close()