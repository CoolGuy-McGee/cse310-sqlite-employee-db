import sqlite3

# connect to the database
conn = sqlite3.connect('employee.db')
cursor = conn.cursor()

print("Before hiring new employees:")
print(cursor.execute("SELECT * FROM employees").fetchall())

# insert new employee records
cursor.execute("INSERT INTO employees VALUES ('Ethan', 'Miller', 65000, 'Engineering', '2022-04-15')")
cursor.execute("INSERT INTO employees VALUES ('Isabella', 'Rivera', 71000, 'Marketing', '2021-09-10')")
cursor.execute("INSERT INTO employees VALUES ('Benjamin', 'Clark', 58000, 'Support', '2020-11-01')")
cursor.execute("INSERT INTO employees VALUES ('Zoe', 'Kim', 77000, 'Product', '2019-06-20')")
cursor.execute("INSERT INTO employees VALUES ('Daniel', 'Evans', 69000, 'Finance', '2023-01-05')")
cursor.execute("INSERT INTO employees VALUES ('Chloe', 'Wright', 62000, 'HR', '2020-02-28')")
cursor.execute("INSERT INTO employees VALUES ('Mateo', 'Hernandez', 80000, 'Sales', '2018-08-12')")
cursor.execute("INSERT INTO employees VALUES ('Abigail', 'Turner', 73000, 'Design', '2021-12-03')")
cursor.execute("INSERT INTO employees VALUES ('Samuel', 'Brooks', 84000, 'Operations', '2017-05-18')")
cursor.execute("INSERT INTO employees VALUES ('Victoria', 'Lee', 90000, 'R&D', '2016-10-30')")

print("After hiring new employees:")
print(cursor.execute("SELECT * FROM employees").fetchall())

# commit changes and close the connection
conn.commit()
conn.close()