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

    def Reg_user(self):
        print("Holla! Please provide your account details for registration")
        db_connect1 = db_connect()
        connect1 = db_connect1.connect_to_db()
        cursor = connect1.cursor()

        self.user_name=input("Please input your name: ")
        self.email=input("Please input your email")
        while True:
            self.password1 = input("Please input your account passoerd: ")
            self.password = input("Please input your passowrd again: ")
            if self.password1 == self.password:
                print("your passwords match!\n")
                break
            else:
                print("your passwords don't match please try again")

        cursor.execute("""
            INSERT INTO users_parent (user_id, name, email, password)
            VALUES (%s, %s, %s,%s)
        """, (18,self.name, self.email, self.password1))
        connect1.commit()
        
        cursor.close()
        connect1.close()

        print(f"Dear {self.user_name} your account has been succesfully registered!\n")
        print("Please provide your child's details for registration")

    def Child_details(self):
        db_connect1 = db_connect()
        connect1 = db_connect1.connect_to_db()
        cursor = connect1.cursor()


        children_no=int(input("How many children do you have under 12 years? "))
        for i in range (children_no):
            self.child_name = input(f"Please please provide child no.{i}'s name:  ")
            self.age = input("Please input their age: ")
            self.prev_diagnosis = input(f" Does {self.child_name} have any previous diagnosis or underlying conditions?")
            cursor.execute("""
            INSERT INTO children (user_id,child_id,name, age, prev_diagnosis)
            VALUES (%s,%s, %s, %s,%s)
            """, (18,4, self.name, self.age, self.prev_diagnosis))
            connect1.commit()
        
            print(f" Your child: {self.child_name} has been registered ")
        cursor.close()
        connect1.close()
        print("All your children have been registered successfully!\n")

    def Login(self):
        db_connect1=db_connect()
        connect1 = db_connect1.connect_to_db()
        cursor = connect1.cursor()

        self.email= input("Please input your email: ")
        login_query = "SELECT password FROM users_parent WHERE email =%s"
        cursor.execute(login_query, (self.email,))
        output = cursor.fetchone()
        #try calling the reg login,ask yes onr no questions,while loop
        if output is None:
            print("This email is not registered, please register first before logging in or use as guest user")
        else:
            self.password1 = input("Please input your account password: ")
            if self.password1 == output[0]:
                print("You have succesfully logged in. Welcome to Early Aid! ")
        cursor.commit()
        
        
        child_query = "SELECT child_name FROM children WHERE user_id = %s"
        cursor.execute(child_query, (18,))
        child_output = cursor.fetchall()
        for i, child in enumerate(child_output,start = 1):
            print(f"{i}.{child[0]}")

        child_choice = int(input("Which child would you like to examine?(choose a number): "))
        
        cursor.commit()
        cursor.close()
        connect1.close()

        
        selected_child = child_output[child_choice-1][0]
        print(f"You have selected {selected_child} for examination.")

    def Guest(self):
        self.child_age =input("Please input your child's age: ")
        self.prev_diagnosis = input(" Does your child have any previous diagnosis or underlying conditions?: ")

    def user_acess(self):
        self.user_choice = input("How would you want to access our app? input either 1,2,or 3:\n1. Register\n2. Login\n3. Guest\n")
        match self.user_choice:
            case "1":
                self.Reg_user()
                self.Child_details()
                self.Login()
            case "2":
                self.Login()
            case "3":
                print("Accesing app as guest ")
                self.Guest()
    
   


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
    
   