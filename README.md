EarlyAid – PLP Group 20

EarlyAid is a terminal-based Python tool designed to guide users through structured questions, collect their answers, save session data, and optionally send the results via email. It connects to a cloud-based MySQL database hosted on Aiven.io.

A brief Description of the Project Files:

.idea - IDE settings (optional)
pycache - Python cache files (auto-generated)
earlyaid_schema.sql - SQL file with the database schema
README.md - Project overview and usage instructions
colored_message.py - Displays colored output for better UX
db_connect.py - Connects to the Aiven-hosted MySQL database
email_sender.py - Sends session results via email
exit_or_restart.py - Asks whether to exit or restart
main.py - Main entry point of the app
populate_questions.py - Adds default questions to the database
questions.py - Handles fetching and managing questions
save_session.py - Saves answers to the database
user_class.py - Defines the User class
README.db - Explanation of database structure

How to Run the Program:

Clone the repository

git clone git@github.com:helen751/Earlyaid_PLP_2_Group20.git
cd Earlyaid_PLP_2_Group20

Install dependencies

Install the MySQL connector for Python:

pip install mysql-connector-python

Configure your database connection

Open the file db_connect.py and edit the connection details to match your Aiven.io MySQL setup:

host = "your-aiven-host"
user = "your-username"
password = "your-password"
database = "your-database-name"
port = your-port
ssl_ca = "path/to/ca.pem" (if your Aiven setup uses SSL)

Note: In production, use environment variables or a secure config file instead of hardcoding passwords.

(Optional) Set up the schema and add sample questions

Use any MySQL client or Python to run earlyaid_schema.sql to create the tables.
To add sample questions to the database, run:

python populate_questions.py

Run the program

python main.py

Main Features:

Welcomes the user and collects their info

Loads questions from the MySQL database

Saves user responses to the database

Option to email the results to the user

Allows the user to restart or exit

Terminal interface with colored messages

Requirements:

Python 3.6 or newer

Internet connection to access Aiven.io database

MySQL connector for Python: install with pip install mysql-connector-python

File Descriptions:

main.py - Starts and runs the full application
user_class.py - Manages user details
questions.py - Retrieves questions from the database
colored_message.py - Adds colored formatting to terminal output
db_connect.py - Handles connection to the cloud database
earlyaid_schema.sql - Defines the database tables
populate_questions.py - Adds default questions to the DB
save_session.py - Stores session results in the database
email_sender.py - Sends results to email if user agrees
exit_or_restart.py - Gives restart or exit choice
README.db - Description of the database design

Security Tips:

Do not hardcode sensitive credentials.
Use .env files or environment variables to keep passwords and hostnames secure.

Contributors:

Developed by Group 20 – ALU PLP Program
Maintained by: helen751 on GitHub
