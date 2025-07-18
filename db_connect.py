import mysql.connector
from mysql.connector import Error


class db_connect():

    #constructor to initialise all connection variables and details.
    def __init__(self):
        self.host = "earlyaid-groupwork-earlyaid.f.aivencloud.com"  # Aiven MySQL host address
        self.port = "20881"  # Default MySQL port
        self.database = "earlyaid_db"
        self.user = "avnadmin"
        self.password = "AVNS_OpDfbrT75J5ncPh1a5q"

    #function to establish the database connection
    def connect_to_db(self):
        try:
            connection = mysql.connector.connect(
                host = self.host,
                port = self.port,
                database = self.database,
                user = self.user,
                password = self.password
            )
            #print this, if successful
            if connection.is_connected():
                print("Connection to MySQL database successful!")
                return connection

        except Error as e:
            print(f"Error: {e}")
            return None

    # Close database connection
    def close_connection(self, connection):
        if connection.is_connected():
            connection.close()
            print("Connection closed.")

    # the execute select query function for all select statements
    def execute_select_query(self, connection, query):

        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute(query)

            # Fetch and return the result
            result = cursor.fetchall()
            return result

        except Error as e:
            print(f"Error executing SELECT query: {e}")

