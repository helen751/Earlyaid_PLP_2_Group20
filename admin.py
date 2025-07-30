import mysql.connector
import colored_message

coloredMessage = colored_message.ColoredMessage()


def connect_db():
    try:
        connection = mysql.connector.connect(
            host='earlyaid-groupwork-earlyaid.f.aivencloud.com',
            port=20881,
            user='avnadmin',
            password='AVNS_OpDfbrT75J5ncPh1a5q',
            database='earlyaid_db',
            ssl_disabled=False
        )
        if connection.is_connected():
            print('Connected to the database.')
            return connection
    except mysql.connector.Error as e:
        print(f'Error: {e}')
        return None

# This function is for adding a new yes/no question to the database
# It includes validation for age and duplicate questions
def add_question(cursor):
    print("\nAdding a new yes/no question.")
    
    # Check for duplicate question
    while True:
        question_text = input("Enter your yes/no question (e.g., 'Is the child coughing frequently?'): ").strip()
        cursor.execute("SELECT 1 FROM questions WHERE question_text = %s", (question_text,))
        if cursor.fetchone():
            print("This question already exists in the database. Please enter a different question.")
        else:
            break

    # Get valid age input (Not greater than 12)
    while True:
        try:
            start_age = int(input("Enter the start age for this question: "))
            end_age = int(input("Enter the end age for this question: "))
            if start_age > 12 or end_age > 12:
                print("Start and end age must be less than or equal to 12.")
            elif start_age > end_age:
                print("Start age cannot be greater than end age.")
            else:
                break
        except ValueError:
            print("Please enter a valid number for age.")

    risk_level = int(input("Enter the risk level (1-5): "))

    # Ensure that the suggestion code is unique to every question
    while True:
        suggestion_code = input("Enter a unique suggestion code for this question (e.g., CUS1): ").strip().upper()
        cursor.execute("SELECT 1 FROM question_risks WHERE suggestion_code = %s", (suggestion_code,))
        if cursor.fetchone():
            print("That suggestion code already exists. Please enter a different one.")
        else:
            break

    suggestion_text = input("Enter the advice or suggestion for this question: ").strip()

    # Insert the new question added by the admin into the questions table
    cursor.execute("""
        INSERT INTO questions (start_age, end_age, question_text, option_a, option_b)
        VALUES (%s, %s, %s, %s, %s)
    """, (start_age, end_age, question_text, "Yes", "No"))

    question_id = cursor.lastrowid

    # Insert into question_risks table
    cursor.execute("""
        INSERT INTO question_risks (question_id, min_age, max_age, risk_level, suggestion_code)
        VALUES (%s, %s, %s, %s, %s)
    """, (question_id, start_age, end_age, risk_level, suggestion_code))

    # Insert into suggestions table the suggestion code, risk level as well as advice
    cursor.execute("""
        INSERT INTO suggestions (suggestion_code, risk_level, advice)
        VALUES (%s, %s, %s)
    """, (suggestion_code, risk_level, suggestion_text))

    print("Question, risk, and suggestion successfully added.")

# This function is for deleting a question from the database and it deletes associated risks and suggestions
def delete_question(cursor):
    print("\nDeleting a question.")
    question_text = input("Enter the exact question text to delete: ").strip()

    # Find question ID
    cursor.execute("SELECT question_id FROM questions WHERE question_text = %s", (question_text,))
    result = cursor.fetchone()

    if result:
        question_id = result[0]

        # Get the suggestion_code before deleting
        cursor.execute("SELECT suggestion_code FROM question_risks WHERE question_id = %s", (question_id,))
        code_result = cursor.fetchone()
        if code_result:
            suggestion_code = code_result[0]
            cursor.execute("DELETE FROM suggestions WHERE suggestion_code = %s", (suggestion_code,))

        cursor.execute("DELETE FROM question_risks WHERE question_id = %s", (question_id,))
        cursor.execute("DELETE FROM questions WHERE question_id = %s", (question_id,))
        print("Question and associated data deleted.")
    else:
        print("No question found with that text.")

def main():
    conn = connect_db()
    if not conn:
        return

    cursor = conn.cursor()
    while True:
        action = input("\nDo you want to (A)dd a question, (D)elete a question, or (Q)uit? ").strip().upper()

        if action == 'A':
            add_question(cursor)
            conn.commit()
        elif action == 'D':
            delete_question(cursor)
            conn.commit()
        elif action == 'Q':
            break
        else:
            print("Please enter a valid option: A, D, or Q.")

    cursor.close()
    conn.close()
    print("Done.")

#the authorisation logic for admin access
coloredMessage.print("\n\tWELCOME TO EARLY AID ADMIN PANEL\n", "blue")

trial = 3
i = 1
correct_password = "earlyadmin"

while i <= trial:
    passw = input("Enter Admin password to proceed: ")

    if passw == correct_password:
        coloredMessage.print("\n\tAuthorisation Successful!", "green")
        coloredMessage.print("\tloading the admin dashboard...", "green")
        i = trial
        main()

    elif passw != correct_password and i == trial:
        coloredMessage.print(f"You have tried the incorrect password {trial} times, SYSTEM LOCKED", "red")

    elif passw != correct_password:
        coloredMessage.print(f"Wrong password! ({trial-i} trials remaining)", "red")
    i = i + 1
