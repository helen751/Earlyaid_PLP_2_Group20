from db_connect import db_connect

class User:
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

    def Reg_user(self):
        print("Holla! Please provide your account details for registration")
        print("Loading...")
        # Establishing a connection to the database
        db_connect1 = db_connect()
        connect1 = db_connect1.connect_to_db()
        cursor = connect1.cursor()

        while True:
            self.name=input("Please enter your account user name: ").strip()
            if not self.name:
                print("The field is empty, please type a valid input")
            elif not any (char.isalpha() for char in self.name):
                print("Your assignmennt name should contain at least one alphabetic character, please try again")        
            elif len(self.name) < 3 or len(self.name) > 50:
                    print("Your name should be between 3 and 50 characters long, please try again")
            else:
                    break

        while True:
            self.email=input("Please input your email: ")
            if not self.email:
                print("The field is empty, please type a valid input")
            elif not any (char.isalpha() for char in self.email):
                print("Your email name should contain at least one alphabetic character, please try again")        
            elif "@" not in self.email or "." not in self.email :
                print("Your email should contain an @ symbol and a dot.")
            elif len(self.email) < 5 or len(self.email) > 50:
                print("Your email should be between 5 and 50 characters long, please try again")
            else:           
                    break

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

            
        cursor.execute("""
            INSERT INTO users_parent (name, email, password)
            VALUES (%s, %s,%s)
        """, (self.name, self.email, self.password1))
        connect1.commit()
        
        cursor.close()
        connect1.close()


    def Child_details(self):
        db_connect1 = db_connect()
        connect1 = db_connect1.connect_to_db()
        cursor = connect1.cursor()

        print("Please provide your child's details for registration")  
        while True:
            children_no=(input("How many children do you have under 12 years? "))
            if not 0<= children_no < 10 :
                print("Children number should be between 0 and 10, please try again")
            elif not children_no:
                print("The field is empty, please type a valid input")
            elif not children_no.isdigit():
                print("Your input should be a number, please try again")
            else :
                break
        for i in range (children_no):
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
            while True:
                self.age = (input(f"Please input {self.child_name}'s age: "))
                if not self.age:
                    print("The field is empty, please type a valid input")
                elif not self.age.isdigit():
                    print("Your child's age should be a number, please try again")
                elif not 0 <= int(self.age) <= 12:
                    print("Your child's age should be between 0 and 12 years, please try again")
                else:
                    break
            #Should we have a list of common conditions for previous diagnosis?

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
           
            connect1.commit()
        
            print(f" Your child: {self.child_name} has been registered ")
        cursor.close()
        connect1.close()
        print("All your children have been registered, and your account has been created")


    def Login(self):
        db_connect1=db_connect()
        connect1 = db_connect1.connect_to_db()
        cursor = connect1.cursor()

        print("Welcome back! Please login to your account")
        while True:
            self.email= input("Please input your account email: ")
            if not self.email:
                print("The field is empty, please type a valid input")
            else:
                break
        login_query = "SELECT user_id, password FROM users_parent WHERE email =%s"
        cursor.execute(login_query, (self.email,))
        output = cursor.fetchone()
        #try calling the reg login,ask yes onr no questions,while loop
        if output is None:
            print("This email is not registered, please register first before logging in or use as guest user")
            choice = input ("would you like to register or login again? choose either 1 or 2:\n1.Register\n2.Login\n")
            if choice == "1":
                self.Reg_user()
                self.Child_details()
                self.Login()
            elif choice == "2":
                self.Login()
            else:
                print("Invalid input, please try again")
                self.Login()
            
        else:

            self.password1 = input("Please input your account password: ")
            if self.password1 == output[0]:
                print("You have succesfully logged in. Welcome to Early Aid! ")
            else:
                print("Your password is incorrect, please try again")
                self.Login()

        #cursor.commit()
        print(output)
        
        
        child_query = "SELECT child_name FROM children WHERE user_id = %s"
        cursor.execute(child_query, (output[0],))
        child_output = cursor.fetchall()
        for i, child in enumerate(child_output,start = 1):
            print(f"{i}.{child[0]}")

        child_choice = int(input("Which child would you like to examine?(choose a number): "))
        
        #cursor.commit()
        #cursor.close()
        connect1.close()

        
        selected_child = child_output[child_choice-1][0]
        print(f"You have selected {selected_child} for examination.")

    def Guest(self):
        self.child_age =input("Please input your child's age: ")
        self.prev_diagnosis = input(" Does your child have any previous diagnosis or underlying conditions?: ")

    def user_acess(self):
        self.user_choice = input("How would you want to access our app? input either 1,2,or 3:\n1. Register\n2. Login\n3. Guest\n")
        if self.user_choice == "1":
            self.Reg_user()
            self.Child_details()
            self.Login()
        elif self.user_choice== "2":
            self.Login()
        elif self.user_choice== "3":
            print("Accesing app as guest ")
            self.Guest()
        else:
            print("Invalid input, please try again")
            self.user_acess()
    

user1=User()
user1.user_acess()         
    # def inputvalidation(self,input_type):
    #     input_type = input_type.strip()

    #     if not input_type:
    #         print("The field is empty, please type a valid input")
    #         return False
        
    #     if input_type == user_name | self.child_name | self.prev_diagnosis:
    #         if not any (char.isalpha() for char in input_type):
    #             print("Your input should contain at least one character, please try again")
    #             return False
            
    #     if input_type == self.email:
    #         if "@" not in self.email:
    
   