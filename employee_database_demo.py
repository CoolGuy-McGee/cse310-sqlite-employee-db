import runpy
from pathlib import Path
import traceback

base = Path(__file__).resolve().parent

scripts = [
    "employee_database_init.py",
    "add_employees.py",
    "update_employees.py",
    "delete_employees.py",
    "filter_by_hire_date.py",
    "delete_ALL_employees.py"
]

for s in scripts:
    path = base / s
    print(f"\n=== Running: {s} ===")
    if not path.exists():
        print(f"SKIP: {path} not found")
        continue
    try:
        runpy.run_path(str(path), run_name="__main__")
    except Exception:
        print(f"ERROR while running {s}:")
        traceback.print_exc()