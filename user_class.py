#Import the function that connects my file to the databbse
from db_connect import db_connect

#User class which is in charge of collecting user details, storing them in the database and allowing user access to the app
class User:

    #initializing the variables that I'll be using in more than one method
    def __init__ (self):
        self.name= None
        self.email = None
        self.password1= None
        self.password = None
        self.child_name = None
        self.age = None
        self.prev_diagnosis= None
        self.child_details = None
        self.parent_id = None

    #Reg_user method which Registers the user through collecting their details and storing them in the database 
    def Reg_user(self):
        print("Holla! Please provide your account details for registration")
        print("Loading...")
        # Establishing a connection to the database
        db_connect1 = db_connect()
        connect1 = db_connect1.connect_to_db()

        #Starting the cursor
        cursor = connect1.cursor()

        #user name entry and input validation
        while True:
            self.name = input("Please enter your account user name: ").strip() #removes any trailing white spaces
            if not self.name:
                print("The field is empty, please type a valid input")
            elif not any (char.isalpha() for char in self.name):
                print("Your assignmennt name should contain at least one alphabetic character, please try again")        
            elif len(self.name) < 3 or len(self.name) > 50:
                    print("Your name should be between 3 and 50 characters long, please try again")
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
                print("The field is empty, please type a valid input")
            elif emails:
                print("This email is already registered, please input another email or login using this email.\nSelect a number")
                
                #user options if similar email is found in database and input validation
                while True:  
                    email_choice =input("1.Enter another email\n2.Login\n").strip()
                    if email_choice == "1":
                        break
                    elif email_choice == "2":
                        self.Login()
                    elif not email_choice:
                        print("The feild is empty please input either no.1 or 2" )
                    else:
                        print("invalid input, please enter either 1 or 2")
            

            elif not any (char.isalpha() for char in self.email):
                print("Your email name should contain at least one alphabetic character, please try again")        
            elif "@" not in self.email or "." not in self.email :
                print("Your email should contain an @ symbol and a dot.")
            elif len(self.email) < 5 or len(self.email) > 50:
                print("Your email should be between 5 and 50 characters long, please try again")
            else:           
                    break
            
        #user password entry and input validation
        while True:
            self.password1 = input("Please input your account password: ")
            if not self.password1:
                print("The field is empty, please type a valid input")
            elif not 4 <= len(self.password1) <= 15:
                print("Your password should be between 4 and 15 characters long, please try again")
            elif not any (char.isalpha() for char in self.password1):
                print("Your password should contain at least one alphabetic character, please try again")        
            elif not any (char.isdigit() for char in self.password1):
                print("Your password should contain at least one numeric character, please try again")        
            else:
                self.password = input("Please input your passowrd again: ")
                if self.password1 == self.password:
                    print("your passwords match!")
                    print(f"Thank you {self.name} for registering with Early Aid\n")
                    break
                else:
                    print("your passwords don't match please try again")

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

        #instantiating the method that allows the file to connect to the database
        db_connect1 = db_connect()
        connect1 = db_connect1.connect_to_db()

        #starting the cursor
        cursor = connect1.cursor()

        print("Loading...")
        print("Please provide your child's details for registration")  

        #children no entry and input validation
        while True:
            children_no=(input("How many children do you have under 12 years? "))
            if not 0<= int (children_no) < 10 :
                print("Children number should be between 0 and 10, please try again")
            elif not children_no:
                print("The field is empty, please type a valid input")
            elif not children_no.isdigit():
                print("Your input should be a number, please try again")
            else :
                break
        for i in range (int (children_no)):

            # child name entry and input validation
            while True:
                self.child_name = input(f"Please please provide child no.{i+1}'s name:  ")
                if not self.child_name:
                    print("The field is empty, please type a valid input")
                elif not any (char.isalpha() for char in self.child_name):
                    print("Your child's name should contain at least one alphabetic character, please try again")        
                elif len(self.child_name) < 3 or len(self.child_name) > 50:
                    print("Your child's name should be between 3 and 50 characters long, please try again")
                else:
                    break

            #child age entry and input validation
            while True:
                self.age = (input(f"Please input {self.child_name}'s age: "))
                if not self.age:
                    print("The field is empty, please type a valid input")
                elif not self.age.isdigit():
                    print("Your child's age should be a whole number, please try again")
                elif not 0 <= int(self.age) <= 12:
                    print("Your child's age should be between 0 and 12 years, please try again")
                else:
                    break
            #previos diagnosis entry and input validation
            while True:
                self.prev_diagnosis = input(f"Does {self.child_name} have any previous diagnosis or underlying conditions? ")
                if not self.prev_diagnosis:
                    print("The field is empty, please type a valid input")
                elif not any (char.isalpha() for char in self.prev_diagnosis):
                    print("Your input should contain at least one alphabetic character, please try again")
                elif len(self.prev_diagnosis)<4:
                    print("Your input should be at least 4 characters long, please try again")
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
        
            print(f"Your child: {self.child_name} has been registered ")

        #closing the cursor and the database connection
        cursor.close()
        connect1.close()
        print("All your children have been registered, and your account has been created\n")

    #login method which will allow the user access the app after confirming that they have registered.
    def Login(self):

        #Instantiating the method which allows connection to the database
        db_connect1=db_connect()
        connect1 = db_connect1.connect_to_db()

        #Starting the cursor
        cursor = connect1.cursor(buffered=True)

        print(f"Welcome back ! Please login to your account")

        #user email entry and input validation
        while True:
            self.email= input("Please input your account email: ")

            if not self.email:
                print("The field is empty, please type a valid input")
            elif not any (char.isalpha() for char in self.email):
                print("Your email should contain at least one alphabetic character, please try again")
            elif "@" not in self.email or "." not in self.email :
                print("Your email should contain an @ symbol and a dot.")
            elif len(self.email) < 5 or len(self.email) > 50:
                print("Your email should be between 5 and 50 characters long, please try again")
            else:
                break

        #Confirming if the user entered the right email
        login_query = "SELECT password FROM users_parent WHERE email =%s"
        cursor.execute(login_query, (self.email,))
        output = cursor.fetchall()

        #Provides the user with three options if their email is not registered  
        if not output :
            print("This email is not registered.")
            self.user_acess()
            
        else:
            #user password entry and input validation.
            while True:
                self.password1 = input("Please input your account password: ")
                #Checking if the user input the correct password
                if self.password1 == output[0][0]:
                    print("You have succesfully logged in. Welcome to Early Aid!\n ")
                    break
                elif not self.password1:
                    print("the field is empty, please input a valid password")
                else:
                    print("Your password is incorrect, please try again")
            


        id_query = "SELECT user_id FROM users_parent WHERE email = %s"
        cursor.execute(id_query,(self.email, ))
        id_output = cursor.fetchone()
        
        child_query = "SELECT name FROM children WHERE user_id = %s"
        cursor.execute(child_query, (id_output[0],))
        child_output = cursor.fetchall()
        if not child_output:
            print("You have no registered children, please register your children first")
            self.Child_details()
            self.Login()
            return
        else:
            print("Here are your registered children:")
            for i, child in enumerate(child_output,start = 1):
                print(f"{i}.{child[0]}")
            while True:
                child_choice = input("Which child would you like to examine?(choose a number): ")
                if not child_choice.isdigit():
                    print("Your choice should be a whole number, please try again")
                elif not child_choice:
                    print("The field is empty, please type a valid input")
                elif not 1 <= int(child_choice) <= len(child_output):
                    print("Invalid choice, please choose a valid child number")     
                else:
                    break

        # Closing the cursor and database connection
        cursor.close()
        connect1.close()

        #display the selected child
        selected_child = child_output[int(child_choice)-1][0]
        print(f"You have selected {selected_child} for examination.")

    #allows the user to access the app as a guest without necessarily registering
    def Guest(self):

        #child name entry and input validation
        while True:
                self.child_name = input("Please input your child's name: ")
                if not self.child_name:
                    print("The field is empty, please type a valid input")
                elif not any (char.isalpha() for char in self.child_name):
                    print("Your child's name should contain at least one alphabetic character, please try again")        
                elif len(self.child_name) < 3 or len(self.child_name) > 50:
                    print("Your child's name should be between 3 and 50 characters long, please try again")
                else:
                    break

        #child age entry and input validation
        while True:
            self.age = (input(f"Please input {self.child_name}'s age: ")).strip()
            if not self.age:
                print("The field is empty, please type a valid input")
            elif not self.age.isdigit():
                print("Your child's age should be a number, please try again")
            elif not 0 <= int(self.age) <= 12:
                print("Your child's age should be between 0 and 12 years, please try again")
            else:
                break

        #previous diagnosis entry and input validation
        while True:
            self.prev_diagnosis = input(f"Does {self.child_name} have any previous diagnosis or underlying conditions? ")
            if not self.prev_diagnosis:
                print("The field is empty, please type a valid input")
            elif not any (char.isalpha() for char in self.prev_diagnosis):
                print("Your input should contain at least one alphabetic character, please try again")
            elif len(self.prev_diagnosis)<4:
                print("Your input should be at least 4 characters long, please try again")
            else:
                break   
            
    #method which allows the user to access the app through whichever method they decide to.
    def user_acess(self):
        self.user_choice = input("How would you want to access our app? input either 1,2,or 3:\n1. Register\n2. Login\n3. Guest\n")
        if self.user_choice == "1":
            self.Reg_user()
            self.Child_details()
            self.Login()
        elif self.user_choice== "2":
            print("Loading ...")
            self.Login()
        elif self.user_choice== "3":
            print("Accesing app as guest ")
            self.Guest()
        else:
            print("Invalid input, please try again")
            self.user_acess()
    
#instantiating the user user access method
user1=User()
user1.user_acess()         

    
   