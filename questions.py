#importing the random class.
import random

#importing the database configuration file
import db_connect
#importing our colored custom message
import colored_message
#importing our email sending file
import email_sender

#importing the saves responses files
import save_session

class question:
    #the class constructor, defining and initialising all the class variables
    def __init__(self):
        self.connection_error = None
        self.question_id_list = None
        self.connection = None
        self.questions_id = []

        #creating an instance of the dbconnect and colored message class
        self.db = db_connect.db_connect()
        self.coloredMessage = colored_message.ColoredMessage()
        self.age = 0
        self.child_name = None
        self.parent_email = None
        self.prev_diagnosis = None
        self.is_guest = None
        self.user_id = None
        self.child_id = None
        self.total_risk_level = None

    #The function that fetches all questions according to child's age and set the class variables
    def ask_question(self, user_id, child_id, age, child_name, parent_email, is_guest, prev_diagnosis):
        answers = {}
        self.age = age
        self.child_name = child_name
        self.parent_email = parent_email
        self.is_guest = is_guest
        self.prev_diagnosis = prev_diagnosis
        self.user_id = user_id
        self.child_id = child_id


        self.coloredMessage.print("Fetching questions...", "blue")

        #connecting to the Aiven cloud database
        self.connection = self.db.connect_to_db()

        if self.connection:
            # query to get all the questions for child age
            query = "SELECT * FROM questions where start_age <="+str(age)+" and end_age >="+str(age)+";"

            #opening the connection and executing the query
            questions = self.db.execute_select_query(self.connection, query)

            #loop through the list of questions and ask the user each question
            for each_question in questions:
                each_question["question_text"] = each_question["question_text"].replace("the child", child_name)
                each_question["question_text"] = each_question["question_text"].replace("the baby", child_name)

                correct_choice = False

                #loop to keep asking question until user enters a valid choice
                while not correct_choice:
                    self.coloredMessage.print(f'\n{each_question["question_text"]} ', "blue")
                    print(f' 1] {each_question["option_a"]}'
                          f'\n 2] {each_question["option_b"]}')

                    choose = input("Select a valid option(1 or 2): ")
                    if choose == "1" or choose == "2":
                        correct_choice = True
                        answers[each_question["question_id"]] = choose
                        self.questions_id.append(each_question["question_id"])

                    else:
                        self.coloredMessage.print("Invalid choice please select either 1 or 2", "red")

            #calling the function to analyse all answers
            self.coloredMessage.print("\n\tAnalysing your answers, please wait...\n", "blue")
            self.analyse_question(answers, age)

        else:
            self.coloredMessage.print("OOPs! It seems you lost your internet connection!", "red")

    #function to analyse the answers and risk levels
    def analyse_question(self, answers, age):
        self.question_id_list = []

        #checking for questions the user answered YES to the symptoms
        for question_id, answer in answers.items():
            if answer == "1":
                self.question_id_list.append(question_id)

        question_id_placeholders = ', '.join(['%s'] * len(self.question_id_list))

        #checking if the established database connection is still active
        if self.connection:

            # query to get all quest risks and analyse
            query = (
                f"SELECT s.risk_level, s.advice "
                f"FROM question_risks r "
                f"INNER JOIN suggestions s ON r.suggestion_code = s.suggestion_code "
                f"WHERE r.min_age <= %s AND r.max_age >= %s AND r.question_id IN ({question_id_placeholders});"
            )
            params = [age, age] + self.question_id_list
            #opening the connection and executing the query
            result = self.db.execute_select_query(self.connection, query, params)

            #calling the analyse risk function to analyse the query result
            self.analyse_risk(result)

        else:
            self.coloredMessage.print("OOPs! It seems you lost your internet connection!", "red")


    #function to anlayse each question risk and get the right suggestion
    def analyse_risk(self, suggestions):
        risk_level = []
        total_risk_level = 0
        risk = "Low"

        for each_suggestion in suggestions:
            risk_level.append(each_suggestion["risk_level"])
            total_risk_level += int(each_suggestion["risk_level"])

        if total_risk_level >= 10:
            risk = "High"

        elif total_risk_level >= 7:
            risk = "Medium"

        elif 3 in risk_level:
            risk = "High"

        #calling the final suggestion function after analysing final risk levels
        self.final_suggestion(suggestions, risk)


    #function to display the suggestions or advice, including risk level and messages.
    def final_suggestion(self, suggestions, risk_level):
        doctor_details = None
        short_topic = None

        if risk_level == "Low":
            self.total_risk_level = 1
            short_topic = f"You don't need to panic. {self.child_name} is going through a mild reaction that you can manage for a few days"
            self.coloredMessage.print(f"\n\t_______RISK LEVEL: LOW_________"
                                      f"\n{short_topic}", "blue")

        elif risk_level == "Medium":
            self.total_risk_level = 2
            short_topic = f"{self.child_name}'s symptoms are moderate, But it is important you monitor closely for any improvement or worsening"
            self.coloredMessage.print(f"\n\t_______RISK LEVEL: MEDIUM_________"
                                      f"\n {short_topic}", "yellow")

        elif risk_level == "High":
            self.total_risk_level = 2
            short_topic = "Serious case identified here! you need to act immediately"
            self.coloredMessage.print("\n\t_______RISK LEVEL: HIGH_________"
                                      f"\n{short_topic}", "red")

        #fetching suggestions for all cases and personalising it by displaying the child's name in between.
        i = 1
        email_suggestions = ""

        for each_suggestion in suggestions:
            each_suggestion["advice"] = each_suggestion["advice"].replace("the child", self.child_name)
            each_suggestion["advice"] = each_suggestion["advice"].replace("the baby", self.child_name)
            print(f' {i}] {each_suggestion["advice"]}')
            email_suggestions += f'{i}] {each_suggestion["advice"]}\n'
            i+=1

        if risk_level == "High" or risk_level == "Medium":
            #check for a suitable doctor in the doctors database and refer the user
            if self.connection:

                # query to get all question risks and analyse
                query = (
                    f"SELECT name, specialty, phone, location "
                    f"FROM doctors "
                    f"WHERE start_age_group <= %s AND end_age_group >= %s and risk_level = %s;"
                )
                params = [self.age, self.age, risk_level]
                # opening the connection and executing the query
                doctors = self.db.execute_select_query(self.connection, query, params)

                # Select a random doctor from the list of all qualified and possible doctors
                doctor = random.choice(doctors)
                print("\n")

                if risk_level == "Medium":
                    doctor_details = f'Contact {doctor["name"].upper()} if symptoms worsens any moment!'
                    self.coloredMessage.print(doctor_details, "blue")

                elif risk_level == "High":
                    doctor_details = f'{self.child_name} needs an immediate attention. Give first aid and Contact {doctor["name"].upper()} immediately'
                    self.coloredMessage.print(doctor_details, "red")

                doctor_details += f'\n\t Phone Number: {doctor["phone"]}'+f'\n\t Location: {doctor["location"]}'+f'\n\t Specialty: {doctor["specialty"]}\n'
                print(f'\n\t Phone Number: {doctor["phone"]}'+f'\n\t Location: {doctor["location"]}'+f'\n\t Specialty: {doctor["specialty"]}\n')
                print()

            else:
                self.coloredMessage.print("OOPs! It seems you lost your internet connection!", "red")

        #if the user is registered, send their suggestion to their email and store the response in the database.
        if not self.is_guest:
            answers = ', '.join(map(str, self.question_id_list))
            email_sender.EmailSender().send_email_to_parent(self.parent_email, self.child_name, risk_level, email_suggestions, short_topic, doctor_details)

            self.coloredMessage.print("\n\tSaving your health details, please wait...", "blue")
            save_session.store_session_result(self.user_id, self.child_id, answers, email_suggestions, self.total_risk_level, self.parent_email)

        else:
            self.coloredMessage.print("\n\tThank you for using EarlyAid. We hope you enjoyed this!\n\n", "blue")
            exit(2)


