#Import the function that connects my file to the databbse
from db_connect import db_connect
import colored_message
import questions

#User class which is in charge of collecting user details, storing them in the database and allowing user access to the app
class User:

    #initializing the variables that I'll be using in more than one method
    def __init__ (self):
        self.child_id = None
        self.name= None
        self.email = None
        self.password1= None
        self.password = None
        self.child_name = None
        self.age = None
        self.prev_diagnosis= None
        self.child_details = None
        self.parent_id = None
        self.coloredMessage = colored_message.ColoredMessage()
        self.ask_questions = questions.question()

    #Reg_user method which Registers the user through collecting their details and storing them in the database 
    def Reg_user(self):
        self.coloredMessage.print("\nHolla! Please provide your account details for registration", "red")
        print("Loading...")
        # Establishing a connection to the database
        db_connect1 = db_connect()
        connect1 = db_connect1.connect_to_db()

        #Starting the cursor
        cursor = connect1.cursor()

        #username entry and input validation
        while True:
            self.name = input("Please enter your account user name: ").strip() #removes any trailing white spaces
            if not self.name:
                self.coloredMessage.print("The field is empty, please type a valid input", "red")
            elif not any (char.isalpha() for char in self.name):
                self.coloredMessage.print("Your assignment name should contain at least one alphabetic character, please try again", "red")
            elif len(self.name) < 3 or len(self.name) > 50:
                self.coloredMessage.print("Your name should be between 3 and 50 characters long, please try again", "red")
            else:
                    break
            
        #user email entry and input validation
        while True:
            self.email = input("Please input your email: ").strip()

            #checking if the user email entered exists in the database
            email_query = "SELECT email FROM users_parent WHERE email = %s"
            cursor.execute(email_query,(self.email, ))
            emails =cursor.fetchone()

            if not self.email:
                self.coloredMessage.print("The field is empty, please type a valid input", "red")
            elif emails:
                self.coloredMessage.print("This email is already registered, please input another email or login using this email.\nSelect a number", "red")
                
                #user options if similar email is found in database and input validation
                while True:  
                    email_choice =input("1.Enter another email\n2.Login\n").strip()
                    if email_choice == "1":
                        break
                    elif email_choice == "2":
                        self.Login()
                    elif not email_choice:
                        print("The field is empty please input either no.1 or 2" )
                    else:
                        print("invalid input, please enter either 1 or 2")
            

            elif not any (char.isalpha() for char in self.email):
                self.coloredMessage.print("Your email name should contain at least one alphabetic character, please try again", "red")
            elif "@" not in self.email or "." not in self.email :
                self.coloredMessage.print("Your email should contain an @ symbol and a dot.", "red")
            elif len(self.email) < 5 or len(self.email) > 50:
                self.coloredMessage.print("Your email should be between 5 and 50 characters long, please try again", "red")
            else:           
                    break
            
        #user password entry and input validation
        while True:
            self.password1 = input("Please input your account password: ")
            if not self.password1:
                self.coloredMessage.print("The field is empty, please type a valid input", "red")
            elif not 4 <= len(self.password1) <= 15:
                self.coloredMessage.print("Your password should be between 4 and 15 characters long, please try again", "red")
            elif not any (char.isalpha() for char in self.password1):
                self.coloredMessage.print("Your password should contain at least one alphabetic character, please try again", "red")
            elif not any (char.isdigit() for char in self.password1):
                self.coloredMessage.print("Your password should contain at least one numeric character, please try again", "red")
            else:
                self.password = input("Please input your password again: ")
                if self.password1 == self.password:
                    self.coloredMessage.print("your passwords match!", "yellow")
                    print(f"Thank you {self.name} for registering with Early Aid\n")
                    break
                else:
                    self.coloredMessage.print("your passwords don't match please try again", "red")

        #inserting user details into the users_parent table in the database  
        cursor.execute("""
            INSERT INTO users_parent (name, email, password)
            VALUES (%s, %s,%s)
        """, (self.name, self.email, self.password1))

        #commiting the insert changes
        connect1.commit()

        #Closing the cursor and the database connection
        cursor.close()
        connect1.close()

    # Child details method which will collect the child details and insert them into child table.
    def Child_details(self):
        self.coloredMessage.print("Loading...", "blue")

        #instantiating the method that allows the file to connect to the database
        db_connect1 = db_connect()
        connect1 = db_connect1.connect_to_db()

        #starting the cursor
        cursor = connect1.cursor()

        print("\nPlease provide your child's details for registration")

        #children no entry and input validation
        while True:
            children_no=(input("How many children do you have under 12 years? "))

            if not children_no.isdigit():
                self.coloredMessage.print("Your input should be a number, please try again", "red")
            elif not children_no:
                self.coloredMessage.print("The field is empty, please type a valid input", "red")
            elif not 0< int (children_no) <= 100 :
                self.coloredMessage.print("Children number range from 1 to 100 please try again", "red")
            else :
                break

        for i in range (int (children_no)):

            # child name entry and input validation
            while True:
                self.child_name = input(f"\nPlease please provide child no.{i+1}'s name:  ")
                if not self.child_name:
                    self.coloredMessage.print("The field is empty, please type a valid input", "red")
                elif not any (char.isalpha() for char in self.child_name):
                    self.coloredMessage.print("Your child's name should contain at least one alphabetic character, please try again", "red")
                elif len(self.child_name) < 3 or len(self.child_name) > 50:
                    self.coloredMessage.print("Your child's name should be between 3 and 50 characters long, please try again", "red")
                else:
                    break

            #child age entry and input validation
            while True:
                self.age = (input(f"Please input {self.child_name}'s age: "))
                if not self.age:
                    self.coloredMessage.print("The field is empty, please type a valid age", "red")
                elif not self.age.isdigit():
                    self.coloredMessage.print("Your child's age should be a whole number, please try again", "red")
                elif not 0 <= int(self.age) <= 12:
                    self.coloredMessage.print("Your child's age should be between 0 and 12 years, please try again", "red")
                else:
                    break
            #previos diagnosis entry and input validation
            while True:
                self.prev_diagnosis = input(f"Does {self.child_name} have any previous diagnosis or underlying conditions? ")
                if not self.prev_diagnosis:
                    self.coloredMessage.print("The field is empty, please type a valid input", "red")
                elif not any (char.isalpha() for char in self.prev_diagnosis):
                    self.coloredMessage.print("Your input should contain at least one alphabetic character, please try again", "red")
                elif len(self.prev_diagnosis)<4:
                    self.coloredMessage.print("Your input should be at least 4 characters long, please try again", "red")
                else:
                    break   

            # Fetching the user_id of the parent to link with the child
            cursor.execute("SELECT user_id FROM users_parent WHERE email = %s",(self.email,))
            self.parent_id = cursor.fetchone()[0]
            connect1.commit()

            # Inserting the child's details into the database
            cursor.execute("""
            INSERT INTO children (user_id,name, age, prev_diagnosis)
            VALUES (%s,%s,%s,%s)
            """, (self.parent_id, self.child_name, self.age, self.prev_diagnosis))

           #Commiting the insert changes
            connect1.commit()
        
            self.coloredMessage.print(f"\n\tYour child: {self.child_name} has been registered ", "green")

        #closing the cursor and the database connection
        cursor.close()
        connect1.close()
        self.coloredMessage.print("\nAll your children have been registered, and your account has been created\n", "green")

    #login method which will allow the user access the app after confirming that they have registered.
    def Login(self):

        #Instantiating the method which allows connection to the database
        db_connect1=db_connect()
        connect1 = db_connect1.connect_to_db()

        #Starting the cursor
        cursor = connect1.cursor(buffered=True)

        self.coloredMessage.print(f"\n\n\tWelcome back ! Please login to your account", "blue")

        #user email entry and input validation
        while True:
            self.email= input("Please input your account email: ")

            if not self.email:
                self.coloredMessage.print("The field is empty, please type a valid input", "red")
            elif not any (char.isalpha() for char in self.email):
                self.coloredMessage.print("Your email should contain at least one alphabetic character, please try again", "red")
            elif "@" not in self.email or "." not in self.email :
                self.coloredMessage.print("Your email should contain an @ symbol and a dot.", "red")
            elif len(self.email) < 5 or len(self.email) > 50:
                self.coloredMessage.print("Your email should be between 5 and 50 characters long, please try again", "red")
            else:
                break

        #Confirming if the user entered the right email
        login_query = "SELECT password, user_id FROM users_parent WHERE email =%s"
        cursor.execute(login_query, (self.email,))
        output = cursor.fetchall()

        #Provides the user with three options if their email is not registered  
        if not output :
            self.coloredMessage.print("This email is not registered.", "red")
            self.user_acess()
            
        else:
            #user password entry and input validation.
            while True:
                self.parent_id = output[0][1]
                self.password1 = input("Please input your account password: ")
                #Checking if the user input the correct password
                if self.password1 == output[0][0]:
                    self.coloredMessage.print("\n\tYou have successfully logged in. Welcome to Early Aid!\n ", "green")
                    break
                elif not self.password1:
                    self.coloredMessage.print("the field is empty, please input a valid password", "red")
                else:
                    self.coloredMessage.print("Your password is incorrect, please try again", "red")
        cursor.close()
        connect1.close()

    def child_info(self, parent_id_f=None, parent_email_f=None):
        self.coloredMessage.print("Fetching your kids' names, please wait...", "blue")
        db_connect1=db_connect()
        connect1 = db_connect1.connect_to_db()

        if self.parent_id is None:
            self.parent_id = parent_id_f
            self.email = parent_email_f

        #Starting the cursor
        cursor = connect1.cursor(buffered=True)
        
        child_query = "SELECT child_id, name, age, prev_diagnosis FROM children WHERE user_id = %s"
        cursor.execute(child_query, (self.parent_id,))
        child_output = cursor.fetchall()
        child_output = [list(row) for row in child_output]
        
        if not child_output:
            self.coloredMessage.print("You have no registered children, please register your children first", "yellow")
            self.Child_details()
            self.Login()
            return
        elif len(child_output) == 1:
            self.child_name = child_output[0][1]
            self.age = child_output[0][2]
            self.prev_diagnosis = child_output[0][3]
            self.child_id = child_output[0][0]

            print(f"You have one registered child,{self.child_name}")
            while True:
                child_choice = input(f"\nPress 0 if you want to add more children or 1 if you want to continue with {self.child_name}: ")
                if not child_choice.isdigit():
                    self.coloredMessage.print("Your choice should be a whole number, please try again", "red")
                elif not child_choice:
                    self.coloredMessage.print("The field is empty, please type a valid input", "red")
                elif not 0 <= int(child_choice) <= 1:
                    self.coloredMessage.print("Invalid choice, please enter either 0 or 1", "red")
                else:
                    break

        else:
            print("Here are your registered children:")
            for i, child in enumerate(child_output,start = 1):
                print(f"{i}.{child[1]} ({child[2]} yrs old)")
            while True:
                print("Which child would you like to examine?(choose a number): ")
                child_choice = input("Enter 0 if you want to add more children ")
                if not child_choice.isdigit():
                    self.coloredMessage.print("Your choice should be a whole number, please try again", "red")
                elif not child_choice:
                    self.coloredMessage.print("The field is empty, please type a valid input", "red")
                elif not 0 <= int(child_choice) <= len(child_output):
                    self.coloredMessage.print("Invalid choice, please choose a valid child number", "red")
                else:
                    break

        # Closing the cursor and database connection
        cursor.close()
        connect1.close()

        #display the selected child
        if child_choice == "0":
            self.Child_details()
            self.child_info()
        else :
            selected_child = int(child_choice)-1
            child_id = child_output[selected_child][0]
            self.child_name = child_output[selected_child][1]
            self.age = child_output[selected_child][2]
            self.prev_diagnosis = child_output[selected_child][3]
            self.coloredMessage.print(f"\n\tYou have selected {self.child_name} for examination.\n\n","blue")
            is_guest = False

            self.ask_questions.ask_question(self.parent_id, child_id, self.age, self.child_name, self.email, is_guest, self.prev_diagnosis)



    #allows the user to access the app as a guest without necessarily registering
    def Guest(self):
        is_guest = True
        child_id = None
        #child name entry and input validation
        while True:
                self.child_name = input("Please input your child's name: ")
                if not self.child_name:
                    self.coloredMessage.print("The field is empty, please type a valid input", "red")
                elif not any (char.isalpha() for char in self.child_name):
                    self.coloredMessage.print("Your child's name should contain at least one alphabetic character, please try again", "red")
                elif len(self.child_name) < 3 or len(self.child_name) > 50:
                    self.coloredMessage.print("Your child's name should be between 3 and 50 characters long, please try again", "red")
                else:
                    break

        #child age entry and input validation
        while True:
            self.age = (input(f"Please input {self.child_name}'s age: ")).strip()
            if not self.age:
                self.coloredMessage.print("The field is empty, please type a valid age", "red")
            elif not self.age.isdigit():
                self.coloredMessage.print("Your child's age should be a number, please try again", "red")
            elif not 0 <= int(self.age) <= 12:
                self.coloredMessage.print("Your child's age should be between 0 and 12 years, please try again", "red")
            else:
                break

        #previous diagnosis entry and input validation
        while True:
            self.prev_diagnosis = input(f"Does {self.child_name} have any previous diagnosis or underlying conditions? ")
            if not self.prev_diagnosis:
                self.coloredMessage.print("The field is empty, please type a valid input", "red")
            elif not any (char.isalpha() for char in self.prev_diagnosis):
                self.coloredMessage.print("Your input should contain at least one alphabetic character, please try again", "red")
            elif len(self.prev_diagnosis)<4:
                self.coloredMessage.print("Your input should be at least 4 characters long, please try again", "red")
            else:
                self.ask_questions.ask_question(self.parent_id, child_id, self.age, self.child_name, self.email, is_guest, self.prev_diagnosis)

            
    #method which allows the user to access the app through whichever method they decide to.
    def user_acess(self):
        user_choice = input("How would you want to access our app? input either 1,2,or 3:\n1. Register\n2. Login\n3. Guest\n")
        if user_choice == "1":
            self.Reg_user()
            self.Child_details()
            self.Login()
            self.child_info()
        elif user_choice== "2":
            self.coloredMessage.print("Loading ...", "blue")
            self.Login()
            self.child_info()
        elif user_choice== "3":
            self.coloredMessage.print("Accessing app as guest ", "yellow")
            self.Guest()
        else:
            self.coloredMessage.print("Invalid input, please try again", "red")
            self.user_acess()


    
   