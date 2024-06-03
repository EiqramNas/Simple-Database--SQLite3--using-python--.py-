import sqlite3
import socket

def create_connection(database_name):
    """Create a connection to the SQLite database."""
    conn = None
    try:
        conn = sqlite3.connect(database_name)
        print("Connection to database successful.")
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def create_table(conn):
    """Create a table in the database."""
    try:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS my_table (
                            id INTEGER PRIMARY KEY,
                            text_content TEXT
                        )''')
        print("Table created successfully.")
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")

def insert_data(conn, text_content):
    """Insert data into the table."""
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO my_table (text_content) VALUES (?)", (text_content,))
        print("Data inserted successfully.")
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error inserting data: {e}")

def read_data(conn):
    """Read and print all data from the table."""
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM my_table")
        rows = cursor.fetchall()
        print("Data in the table:")
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(f"Error reading data: {e}")

def update_data(conn, text_id, new_text_content):
    """Update data in the table."""
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE my_table SET text_content = ? WHERE id = ?", (new_text_content, text_id))
        print("Data updated successfully.")
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error updating data: {e}")

def delete_data(conn, text_id):
    """Delete data from the table."""
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM my_table WHERE id = ?", (text_id,))
        print("Data deleted successfully.")
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error deleting data: {e}")

def main():
    database_name = input(r'Location: ')
    conn = create_connection(database_name)
    if conn is not None:
        create_table(conn)

        while True:
            print("\nDatabase Navigation 1(W) 2(R) 3(U) 4(Del) 5(Exit): ")

            choice = input("Enter your choice: ")

            if choice == '1':
                text_content = input("Enter text: ")
                insert_data(conn, text_content)
            elif choice == '2':
                read_data(conn)
            elif choice == '3':
                text_id = int(input("Enter ID of text to update: "))
                new_text_content = input("Enter new text: ")
                update_data(conn, text_id, new_text_content)
            elif choice == '4':
                text_id = int(input("Enter ID of text to delete: "))
                delete_data(conn, text_id)
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

        conn.close()
        print("Connection to database closed.")

if __name__ == "__main__":
    main()
