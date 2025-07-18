import db_connect
import colored_message

class question:
    def __init__(self):
        self.connection = None
        self.question = question
        self.db = db_connect.db_connect()
        self.coloredMessage = colored_message.ColoredMessage()

    def ask_question(self, age, child_name):
        answers = []
        self.connection = self.db.connect_to_db()

        if self.connection:
            # query to get all the questions for child age
            query = "SELECT * FROM questions where start_age <="+str(age)+" and end_age >="+str(age)+";"

            #opening the connection, executing the query and closing the connection
            questions = self.db.execute_select_query(self.connection, query)
            self.db.close_connection(self.connection)

            #loop through the list of questions and ask the user each question
            for each_question in questions:
                each_question["question_text"] = each_question["question_text"].replace("the child", child_name)
                each_question["question_text"] = each_question["question_text"].replace("the baby", child_name)

                correct_choice = False

                while not correct_choice:
                    self.coloredMessage.print(f'\n{each_question["question_text"]} ', "blue")
                    print(f' 1] {each_question["option_a"]} '
                          f'\n 2] {each_question["option_b"]}')

                    choose = input("Select a valid option(1 or 2): ")
                    if choose == "1" or choose == "2":
                        correct_choice = True
                        answers.append(choose)

                    else:
                        self.coloredMessage.print("Invalid choice please select either 1 or 2", "red")

            print(answers)
question().ask_question(2, "favour")