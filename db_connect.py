import mysql.connector
from mysql.connector import Error


class db_connect():

    def __init__(self):
        self.host = "earlyaid-groupwork-earlyaid.f.aivencloud.com"  # Aiven MySQL host address
        self.port = "20881"  # Default MySQL port
        self.database = "earlyaid_db"
        self.user = "avnadmin"
        self.password = "AVNS_OpDfbrT75J5ncPh1a5q"


    def connect_to_db(self):
        try:
            connection = mysql.connector.connect(
                host = self.host,
                port = self.port,
                database = self.database,
                user = self.user,
                password = self.password
            )

            if connection.is_connected():
                print("Connection to MySQL database successful!")
                return connection

        except Error as e:
            print(f"Error: {e}")
            return None

    # Close connection
    def close_connection(self, connection):
        if connection.is_connected():
            connection.close()
            print("Connection closed.")

    # Example of running a query
    def execute_select_query(self, connection, query):

        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute(query)

            # Fetch and print the result
            result = cursor.fetchall()
            return result

        except Error as e:
            print(f"Error executing SELECT query: {e}")

