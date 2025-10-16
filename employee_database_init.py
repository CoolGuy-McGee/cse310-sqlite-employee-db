import sqlite3

# connect to the database
conn = sqlite3.connect('employee.db')
cursor = conn.cursor()

# create the employees table
cursor.execute("""CREATE TABLE IF NOT EXISTS employees (
               first text,
               last text,
               pay real,
               department text,
               hire_date text)
               """)

# insert 10 sample employee records
cursor.execute("INSERT INTO employees VALUES ('Jane', 'Smith', 72000, 'Marketing', '2022-06-01')")
cursor.execute("INSERT INTO employees VALUES ('Carlos', 'Lopez', 55000, 'Support', '2021-11-20')")
cursor.execute("INSERT INTO employees VALUES ('Aisha', 'Khan', 82000, 'Engineering', '2020-08-05')")
cursor.execute("INSERT INTO employees VALUES ('Maya', 'Patel', 67000, 'HR', '2019-03-12')")
cursor.execute("INSERT INTO employees VALUES ('Liam', 'OConnor', 95000, 'Engineering', '2018-07-23')")
cursor.execute("INSERT INTO employees VALUES ('Oliver', 'Brown', 48000, 'Sales', '2024-02-14')")
cursor.execute("INSERT INTO employees VALUES ('Sofia', 'Garcia', 76000, 'Product', '2021-05-30')")
cursor.execute("INSERT INTO employees VALUES ('Noah', 'Wilson', 61000, 'Finance', '2023-09-01')")
cursor.execute("INSERT INTO employees VALUES ('Emma', 'Nguyen', 70000, 'Design', '2020-12-10')")
cursor.execute("INSERT INTO employees VALUES ('Harper', 'Sinclair', 88000, 'Operations', '2020-10-20')")

print(cursor.execute("SELECT * FROM employees").fetchall())

# commit changes and close the connection
conn.commit()
conn.close()