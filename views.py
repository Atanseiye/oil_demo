import sqlite3
import pandas as pd

def csv_to_sqlite(csv_file, db_name="data.db", table_name="csv_data"):
    # Step 1: Read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file)

    # Step 2: Connect to SQLite database (it will create the file if it doesn't exist)
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Step 3: Create a table in SQLite (if it doesn't already exist)
    # Dynamically create the table using the columns from the DataFrame
    columns = ', '.join([f"{col} TEXT" for col in df.columns])
    create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
    cursor.execute(create_table_query)

    # Step 4: Insert CSV data into the SQLite table
    for _, row in df.iterrows():
        values = tuple(row)
        insert_query = f"INSERT INTO {table_name} ({', '.join(df.columns)}) VALUES ({', '.join(['?' for _ in df.columns])})"
        cursor.execute(insert_query, values)

    # Commit changes and close the connection
    conn.commit()
    conn.close()

    print(f"CSV data has been successfully inserted into the '{table_name}' table in the '{db_name}' database.")


def load_file_from_db(file_id, db_name="files.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT content FROM files WHERE id = ?", (file_id,))
    content = cursor.fetchone()[0]
    
    with open("output.csv", 'wb') as f:
        f.write(content)
    conn.close()
    return "output.csv"

