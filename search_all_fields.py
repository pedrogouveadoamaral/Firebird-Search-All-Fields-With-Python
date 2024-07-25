import fdb


def search_all_fields(_database, _user, _password, _search_value):
    # Connect to the Firebird database
    con = fdb.connect(
        dsn=_database,
        user=_user,
        password=_password
    )
    cur = con.cursor()

    try:
        # Execute a query to get all tables and fields from the database
        query_tables_fields = cur.execute(
            "SELECT "
            "TRIM(r.rdb$relation_name) table_name, "  # Table name
            "TRIM(r.rdb$field_name) field_name "      # Field name
            "FROM RDB$RELATION_FIELDS r"
        ).fetchall()

        # Create a dictionary to store the fields for each table
        table_fields = {}
        for table, field in query_tables_fields:
            if table not in table_fields:
                table_fields[table] = []
            table_fields[table].append(field)

        count_table = 1  # Tables counter
        count_field = 1  # Fields counter
        result_list = []  # List to store the results
        tables_not_work = []
        for table, fields in table_fields.items():  # Loop to interate on tables_fields dict
            for field in fields:  # Loop to interate on fields
                # Query to search for the specified value in each field
                try:
                    query = f'''SELECT TRIM({field}) FROM {table} WHERE {field} LIKE '{_search_value}%' '''
                    result = cur.execute(query).fetchall()
                    print(f'Table: ({count_table}) {table} - Field: ({count_field}) {field} - Value(s): {result}')
                    if result:
                        # Append results to the result list if any value is found
                        result_list.append(f'Table: {table} - Field: {field} - Value(s): {result}')
                        print(f'Table: {count_table} {table} - Field: {count_field} {field}')
                    count_field += 1
                except Exception as e:
                    print(f'Query not work on table {table}! Error: {e}')
                    tables_not_work.append(table)
            count_table += 1
        return result_list, tables_not_work
    finally:
        # Close the cursor and connection
        cur.close()
        con.close()


# Database connection parameters
database = r'D:\dbs\DB.GDB'
user = 'SYSDBA'
password = 'masterkey'
search_value = 'TEST'

# Execute the function and print the results
results = search_all_fields(database, user, password, search_value)
print(f"Tables that didn't execute: {results[1]}\n Values found: {results}")
