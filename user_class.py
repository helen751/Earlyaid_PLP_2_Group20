import mysql.connector
from uuid import uuid4

def connect_to_database():
    try:
        connection = mysql.connector.connect( 
            host='earlyaid-groupwork-earlyaid.f.aivencloud.com',
            port = 20881,
            user = 'avnadmin',
            password = 'AVNS_OpDfbrT75J5ncPh1a5q',
            database = 'earlyaid_db',
            ssl_disabled= False
        )  
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")

connect_to_database()

class User:
    def __init__ (self):
        self.name= None
        self.email = None
        self.password1= None
        self.password = None
        self.child_name = None
        self.child_age = None
        self.prev_diagnosis= None
        self.child_details = None

    def Reg_user(self):
        print("Holla! Please provide your account details for registration")
        connect1 = connect_to_database()
        cursor = connect1.cursor()

        self.user_name=input("Please input your name: ")
        self.email=input("Please input your email")
        while True:
            self.password1 = input("Please input your account passoerd: ")
            self.password = input("Please input your passowrd again: ")
            if self.password1 == self.password:
                print("your passwords match!")
                break
            else:
                print("your passwords don't match please try again")

        cursor.execute("""
            INSERT INTO users_parent (user_id, name, email, password)
            VALUES (%s, %s, %s,%s)
        """, (1,self.name, self.email, self.password1))
        connect1.commit()
        print(f"Details for {self.name} have been successfully added.")
        
        cursor.close()
        connect1.close()

        print(f"Dear {self.user_name} your account has been registered!")
        print("Please provide your child's details for registration")

    def Child_details(self):
        children_no=int(input("How many children do you have under 12 years? "))
        for i in range (children_no):
            self.child_name = input("Please please input child no {i}'s name:  ")
            self.child_age = input("Please input their age: ")
            self.prev_diagnosis = input(f" Does {self.child_name} have any previous diagnosis or underlying conditions?")
            print(f" Your child: {self.child_name} has been registered ")


    def Login(self):
        self.email= input("Please input your email: ")
        self.password1 = input("Please input your account password: ")

        self.child_details = input("Which child would you like to examine?: ")
    def Guest(self):
        self.child_age =input("Please input your child's age: ")
        self.prev_diagnosis = input(" Does your child have any previous diagnosis or underlying conditions?: ")

    def user_acess(self):
        self.user_choice = input("How would you want to access our app? input either 1,2,or 3:\n1. Register\n2.Login\n3.Guest\n")
        match self.user_choice:
            case "1":
                self.Reg_user()
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
    
   