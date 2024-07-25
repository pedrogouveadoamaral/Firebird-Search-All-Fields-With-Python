# Firebird Search All Fields

A Python script to search for a specified value across all fields in all tables of a Firebird database.

## Description

This project provides a Python script that connects to a Firebird database and searches for a specified value across all fields in all tables. It retrieves and prints the matching values and the respective table and field names. The script also handles exceptions and keeps track of tables where queries fail.

## Features

- Connects to a Firebird database using user-provided credentials.
- Retrieves all table and field names from the database schema.
- Searches for a specified value in all fields of all tables.
- Prints the results, including table and field names where the value is found.
- Logs tables where queries fail.

## Requirements

- Python 3.x
- `fdb` library for Python

## Installation

1. Install the `fdb` library:
    ```bash
    pip install fdb
    ```

2. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/Firebird-Search-All-Fields.git
    cd Firebird-Search-All-Fields
    ```

## Usage

1. Update the database connection parameters (`database`, `user`, `password`, `search_value`) in the script.

2. Run the script:
    ```bash
    python search_all_fields.py
    ```

3. The script will output the results, including the tables and fields where the value was found, as well as any tables where the queries failed.

## Example

```python
# Database connection parameters
database = r'D:\dbs\DB.GDB'
user = 'SYSDBA'
password = 'masterkey'
search_value = 'TEST'

# Execute the function and print the results
results = search_all_fields(database, user, password, search_value)
print(f"Tables that didn't execute: {results[1]}")
print(f"Values found: {results}")
