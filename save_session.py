import sqlite3  # Module for SQLite database operations
from datetime import datetime  # Generate a readable timestamp

def store_session_result(response_id, user_id, child_id, answer, suggestion, risk_score, timestamp):
    """
    Store the user session results, the user id and the child id into the earlyaid database
    """
    try:
        # Get the current date and time
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Connect to the database
        conn = sqlite3.connect('earlyaid_database_db.db')
        cursor = conn.cursor()

        # Insert the session result into the 'responses' table
        cursor.execute('''
        INSERT INTO responses (response_id, user_id, child_id, answer, suggestion, risk_score, timestamp)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (response_id, user_id, child_id, answer, suggestion, risk_score, timestamp))

        # Save the changes into the database
        conn.commit()

        print("The information has been saved successfully!")

    except sqlite3.Error as e:  # Print any database error that occurs
        print("Error saving the session to the database: ", e)

    finally:
        # Close the connection if it was opened
        if 'conn' in locals():
            conn.close()
