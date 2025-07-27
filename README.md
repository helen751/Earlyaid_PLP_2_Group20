EarlyAid – PLP Group 20

EarlyAid is a terminal-based Python tool designed to guide users through structured questions, collect their answers, save session data, and optionally send the results via email. It connects to a cloud-based MySQL database hosted on Aiven.io.

A brief Description of the Project Files:

.idea - IDE settings (This is an optional file)
pycache - Python cache files (the file is also auto-generated)
earlyaid_schema.sql - This is an SQL file with the database schema
README.md - Project overview and usage instructions
colored_message.py - This  file Displays colored output for better User experience
db_connect.py - This file Connects to the Aiven-hosted MySQL database
email_sender.py - This file is incharge for Sending session results via email
exit_or_restart.py - This file Asks the user whether to exit or restart
main.py - This file is the Main entry point of the app
populate_questions.py - This file Adds default questions to the database
questions.py - This file Handles fetching and managing questions
save_session.py - This file Saves answers to the database
user_class.py - This file Defines the User class


How can one Run the Program:

1st Step: Clone the repository

git clone git@github.com:helen751/Earlyaid_PLP_2_Group20.git
cd Earlyaid_PLP_2_Group20

2nd Step: Install relevant dependencies

Install the MySQL connector for Python:

pip install mysql-connector-python

3rd Step : Configure your database connection

Open the file db_connect.py and edit the connection details to match your Aiven.io MySQL setup:

host = "earlyaid-groupwork-earlyaid.f.aivencloud.com"
user = "avnadmin"
password = "AVNS_OpDfbrT75J5ncPh1a5q"
database = "defaultdb"
port = 20881
ssl = REQUIRED


4th Step : Use any MySQL client or Python to run earlyaid_schema.sql to create the tables.
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

**************** The Requirements For this application:

Python 3.9 or newer

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


Contributors:

Developed by Group 20 – ALU PLP Program              ----------25th/07/2025

