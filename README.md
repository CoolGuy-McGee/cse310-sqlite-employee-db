# SQLite Employee DB — CSE 310 Sprint 2

Project demonstrating basic CRUD (Create, Read, Update, Delete) operations against a SQLite relational database using Python. This project satisfies the module requirements for working with a SQL relational database and includes a stretch demonstration using a date column.

## Module objectives
The project implements the following requirements:
1. Create a SQL database and table (scripts create/open a local SQLite DB).
2. Query data from the database.
3. Add new data to the database.
4. Update data in the database.
5. Delete data from the database.

Stretch challenge implemented:
- A hire_date column is used and `filter_by_hire_date.py` demonstrates filtering employees by a date range.

## Files and purpose
- `employee_database_demo.py` — runs the other scripts in order (convenience / demo harness).
- `employee_database_init.py` — creates the employees table and inserts initial records (seed).
- `add_employees.py` — inserts additional unique employees.
- `update_employees.py` — updates employee fields (last names and raises).
- `delete_employees.py` — deletes a few employees.
- `filter_by_hire_date.py` — demonstrates querying by hire_date (stretch).
- `delete_ALL_employees.py` — utility to remove all rows from the employees table (use with caution).
- `README.md`, `LICENSE` — repo documentation and license.

## How to run (Windows)
1. Open a terminal in this folder:
   cd "c:\Users\dalton\Documents\BYU-I\Coursework\Fall 2025\CSE 310 (Applied Programming)\Individual Sprints\Sprint 2\cse310-sqlite-employee-db"

2. Run the demo script that executes all of the scripts in order:
   python employee_database_demo.py
   

3. Or run the other scripts individually or run the demo harness:
   python employee_database_init.py
   python add_employees.py
   python update_employees.py
   python delete_employees.py
   python filter_by_hire_date.py
   

Notes:
- If your system uses `py` instead of `python`, replace `python` with `py`.
- Scripts use Python's standard sqlite3 module. No external dependencies required.

## Expected behavior
- The init script creates the SQLite database file (if not present) and an `employees` table with a `hire_date` column.
- Add/update/delete scripts modify the table and commit changes.
- `employee_database_demo.py` runs the scripts in a defined order and prints progress/errors to the console.
- `filter_by_hire_date.py` shows how to filter rows using a date range (stretch).

## Safety / troubleshooting
- Back up the database file before running destructive scripts (e.g., `delete_ALL_employees.py`).
- If a script errors because the table doesn't exist, run `employee_database_init.py` first.
- Use `sqlite3` CLI or a DB browser to inspect the .db file if needed.

## License
See LICENSE file in this folder.