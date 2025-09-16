import sqlite3
import pandas as pd

# Connect to SQLite database (creates company.db if not exists)
conn = sqlite3.connect("company.db")
cursor = conn.cursor()

# Drop tables if already exist (to avoid duplicate errors when re-running)
cursor.execute("DROP TABLE IF EXISTS employees;")
cursor.execute("DROP TABLE IF EXISTS departments;")

# Create employees table
cursor.execute("""
CREATE TABLE employees (
    employee_id INTEGER PRIMARY KEY,
    department_id INTEGER,
    salary INTEGER
)
""")

# Insert employees data
cursor.executemany("""
INSERT INTO employees (employee_id, department_id, salary) VALUES (?, ?, ?)
""", [
    (1, 101, 65000),
    (2, 102, 80000),
    (3, 101, 70000),
    (4, 103, 95000),
    (5, 102, 75000),
    (6, 101, 60000),
    (7, 104, 55000),
    (8, 103, 110000)
])

# Create departments table
cursor.execute("""
CREATE TABLE departments (
    department_id INTEGER PRIMARY KEY,
    department_name TEXT
)
""")

# Insert departments data
cursor.executemany("""
INSERT INTO departments (department_id, department_name) VALUES (?, ?)
""", [
    (101, "Marketing"),
    (102, "Engineering"),
    (103, "Data Science"),
    (104, "Sales")
])

# Run the SQL query
query = """
SELECT d.department_name, 
       AVG(e.salary) AS average_salary
FROM employees e
JOIN departments d ON e.department_id = d.department_id
GROUP BY d.department_name
ORDER BY average_salary DESC;
"""

df = pd.read_sql_query(query, conn)

# Show results
print(df)

# Close connection
conn.close()
