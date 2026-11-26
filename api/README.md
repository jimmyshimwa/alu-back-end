# alu-back-end

This project contains Python scripts that gather data from a REST API
(https://jsonplaceholder.typicode.com) and export it.

## Requirements

- Python 3 (tested with python3)
- The `requests` module
- Code follows PEP 8 (checked with pycodestyle)
- All scripts are executable and start with `#!/usr/bin/python3`

## Scripts (directory: api)

### 0-gather_data_from_an_API.py

Takes an employee ID as an argument and prints that employee's TODO list
progress.

Usage:

    ./0-gather_data_from_an_API.py 2

Output format:

    Employee EMPLOYEE_NAME is done with tasks(DONE/TOTAL):
     TASK_TITLE

### 1-export_to_CSV.py

Takes an employee ID as an argument and exports all of that employee's
tasks to a file named USER_ID.csv.

Usage:

    ./1-export_to_CSV.py 2

CSV format:

    "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"

## Author

Jimmy Shimwa
