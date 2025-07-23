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
            print('✅ Connected to the database.')
            return connection
    except mysql.connector.Error as e:
        print(f'Error: {e}')
        return None

#This function is for adding a new yes/no question to the database
#It will prompt the user for the question text, age range, risk level, and a unique suggestion code and insert it to the questions and risks tables
def add_question(cursor):
    print("\n Adding a new yes/no question.")
    question_text = input("Enter your yes/no question (e.g., 'Is the child coughing frequently?'): ").strip()
    start_age = int(input("Enter the start age for this question: "))
    end_age = int(input("Enter the end age for this question: "))
    risk_level = int(input("Enter the risk level (1–5): "))

    # Ensure that the suggestion code is unique
    while True:
        suggestion_code = input("Enter a unique suggestion code for this question (e.g., CUS1): ").strip().upper()
        cursor.execute("SELECT 1 FROM question_risks WHERE suggestion_code = %s", (suggestion_code,))
        if cursor.fetchone():
            print("That suggestion code already exists. Please enter a different one.")
        else:
            break

    # Insert the new question into the questions table
    cursor.execute("""
        INSERT INTO questions (start_age, end_age, question_text, option_a, option_b)
        VALUES (%s, %s, %s, %s, %s)
    """, (start_age, end_age, question_text, "Yes", "No"))

    question_id = cursor.lastrowid

    # Insert risks into the question_risks table
    cursor.execute("""
        INSERT INTO question_risks (question_id, min_age, max_age, risk_level, suggestion_code)
        VALUES (%s, %s, %s, %s, %s)
    """, (question_id, start_age, end_age, risk_level, suggestion_code))

    print("Question and risk successfully added.")

#This function is for deleting a question from the database
def delete_question(cursor):
    print("\nDeleting a question.")
    question_text = input("Enter the exact question text to delete: ").strip()

    # Find question ID
    cursor.execute("SELECT question_id FROM questions WHERE question_text = %s", (question_text,))
    result = cursor.fetchone()

    if result:
        question_id = result[0]
        cursor.execute("DELETE FROM question_risks WHERE question_id = %s", (question_id,))
        cursor.execute("DELETE FROM questions WHERE question_id = %s", (question_id,))
        print("Question and associated risk deleted.")
    else:
        print("No question found with that text.")


def main():
    conn = connect_db()
    if not conn:
        return

    cursor = conn.cursor()
# Loop to allow the user to choose if they want to add or delete the questions or if they want to quit.
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
    print(" Done.")


if __name__ == "__main__":
    main()
