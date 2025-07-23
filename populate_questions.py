import mysql.connector

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
# It will prompt the user for the question text, age range, risk level, suggestion code, and suggestion text.
def add_question(cursor):
    print("\nAdding a new yes/no question.")
    question_text = input("Enter your yes/no question (e.g., 'Is the child coughing frequently?'): ").strip()
    start_age = int(input("Enter the start age for this question: "))
    end_age = int(input("Enter the end age for this question: "))
    risk_level = int(input("Enter the risk level (1-5): "))

    # Ensure that the suggestion code is unique
    while True:
        suggestion_code = input("Enter a unique suggestion code for this question (e.g., CUS1): ").strip().upper()
        cursor.execute("SELECT 1 FROM question_risks WHERE suggestion_code = %s", (suggestion_code,))
        if cursor.fetchone():
            print("That suggestion code already exists. Please enter a different one.")
        else:
            break

    suggestion_text = input("Enter the advice or suggestion for this question: ").strip()

    # Insert the new question into the questions table
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

# This function is for deleting a question from the database
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

if __name__ == "__main__":
    main()
