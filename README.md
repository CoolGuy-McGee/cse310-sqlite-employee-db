# SQLite Employee DB — CSE 310 Sprint 2

Project demonstrating basic CRUD (Create, Read, Update, Delete) operations against a SQLite relational database using Python. This project satisfies the module requirements for working with a SQL relational database and includes a stretch demonstration using a date column.

## Instructions for Build and Use

How to run (Windows)

1. Open a terminal in this folder:
   cd "c:\Users\dalton\Documents\BYU-I\Coursework\Fall 2025\CSE 310 (Applied Programming)\Individual Sprints\Sprint 2\cse310-sqlite-employee-db"

2. Run the demo script that executes all scripts in order:
   python employee_database_demo.py

3. Or run individual scripts:
   python employee_database_init.py
   python add_employees.py
   python update_employees.py
   python delete_employees.py
   python filter_by_hire_date.py

Notes:
- If your system uses `py` instead of `python`, replace `python` with `py`.
- Scripts use Python's standard sqlite3 module. No external dependencies required.
- Back up the database file before running destructive scripts (e.g., `delete_ALL_employees.py`).
- If a script errors because the table doesn't exist, run `employee_database_init.py` first.
- Use the sqlite3 CLI or a DB browser to inspect the .db file if needed.

## Development Environment 

To recreate the development environment, you need the following software and/or libraries with the specified versions:

* sqlite3
* python3

## Useful Websites to Learn More

I found these websites useful in developing this software:

* [W3 Schools](https://www.w3schools.com/sql/)
* [SQLite Tutorial](https://www.sqlitetutorial.net/)
* [Python Docs](https://docs.python.org/3.13/library/sqlite3.html)

## Future Work

The following items I plan to fix, improve, and/or add to this project in the future:

* [ ] Add a CLI interface to interact with the database using a menu system.
* [ ] Have the program accept a custom database path.
* [ ] Support CSV import/export.