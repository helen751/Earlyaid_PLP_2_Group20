from datetime import datetime  # Generate a readable timestamp
import mysql.connector
from db_connect import db_connect
import exit_or_restart

# Establish and reuse the connection
connect = db_connect()
connection = connect.connect_to_db()

def store_session_result(user_id, child_id, answer, suggestion, risk_score, parent_email, timestamp=None):
    """
    Store the user session results, the user id and the child id into the earlyaid database
    """

    #If there is no timestamp provided, use the current date and time
    if timestamp is None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        # Create a cursor that execute sql commands
        cursor = connection.cursor()

        sql = '''
        INSERT INTO responses (user_id, child_id, answer, suggestion, risk_score, timestamp)
        VALUES (%s, %s, %s, %s, %s, %s)
        '''

        # Execute sql command with the values provided
        cursor.execute(sql, (user_id, child_id, answer, suggestion, risk_score, timestamp))


        # Save the changes into the database
        connection.commit()

        print("Your information has been saved successfully!")

    except mysql.connector.Error as e:  # Print any database error that occurs
        print("Error saving the session to the database: ", e)

    finally:
        # Close the connection if it was opened
        if 'connection' in locals():
            connection.close()

        #calling the last function to ask user if they want to exit the app or restart
        exit_or_restart.exit_or_restart(user_id, parent_email)
