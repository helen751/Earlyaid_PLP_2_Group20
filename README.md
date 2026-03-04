
# EarlyAid: Child Symptom Checker CLI

> **Empowering parents and guardians with instant, structured child health assessments, first aid guidance, and referrals.**

---

## ✨ Overview

**EarlyAid** is a command-line Python application designed to:
- Help caregivers quickly assess child symptoms (age 0–12 years)
- Provide age-specific first aid guidance
- Recommend urgent care or referral to a doctor if needed

The app supports:
- Multiple children per user
- Secure user accounts (parent/guardian)
- Cloud-based data storage (MySQL - AIVEN) 
- Doctor referral for critical cases
- Email notifications
- History tracking of user symptoms and responses

---

## 🏗️ Directory Structure

```
Earlyaid_PLP_2_Group20/
│
├── Earlyaid_PLP_2_Group20/
│   ├── main.py               # App entry point (Welcome, CLI navigation)
│   ├── user_class.py         # User (parent/guardian) registration, login, child management
│   ├── db_connect.py         # Database connection (MySQL)
│   ├── colored_message.py    # Colored output utility
│   ├── questions.py          # Symptom checker logic
│   ├── email_sender.py       # Email alerts/notifications
│   ├── save_session.py       # Session management (optional, CLI resume)
│   ├── exit_or_restart.py    # Exit/restart app utilities
│   ├── admin.py # The admin panel to add new questions specific for each age group or delete existing questions
│   ├── earlyaid_schema.sql   # MySQL schema for all tables and rows prefilled.
│   └── README.md             # All App instructions
├── .venv/                    # (Python virtual environment)
└── .git/                     # (git repo files)
```

---

## 🚀 Features

- **Admin Panel:**  
  To manage all questions and the application.

- **Secure Registration & Login:**  
  Parents/guardians register and manage accounts securely with details:
  - Username
  - Email
  - Password.

- **Multiple Child Support:**  
  Add/manage several children with age-specific info. The user/parent add each childs:
  - Name
  - Age
  - Previous Diagnosis

- **Structured Symptom Checker:**  
  Answers a series of health related questions based on the child's age.

- **Answers/Symptoms Analysis**  
  Based on the user's answers, the system analyses and scores each symptom risk depending on the child's age.

- **Personalized Health Guidance:**  
  Provides first aid advice or refers to doctor based on symptom/risk If low symptom, it just gives advice, but Medium and High risk needs doctor referral.

- **Critical Alerts:**  
  Sends email notifications for user to make reference to later.

- **Colorful, User-Friendly CLI:**  
  Interactive interface with colored text for clarity.

- **Error Handling:**  
  All errors are handled gracefully and well test. The app is user-friendly and easy to flow.
---

## 🛠️ Setup & Installation

### 1. Clone the Repo

```bash
git clone https://github.com/helen751/Earlyaid_PLP_2_Group20.git
cd Earlyaid_PLP_2_Group20/Earlyaid_PLP_2_Group20
```

### 2. Install Dependencies

- Ensure **Python 3.8+** is installed.
- Install [MySQL Server](https://dev.mysql.com/downloads/mysql/).
- Install required Python libraries:

```bash
pip install mysql-connector-python
```

*(We created a color CLI library to add colors in the app. the custom `colored_message.py` is provided.)*

### 3. Database Setup

- The code is already connecting to our AIVEN MYSQL server.
- We have Seven tables in the schema, and you can run this sql code on your code terminal to view the tables.

```sql
-- In your MySQL client:
select * from users_parent;
select * from children;
select * from questions;
select * from question_risks;
select * from suggestions;
select * from responses;
select * from doctors
```

- Optionally, use `admin.py` to add your custom questions.

### 4. Configure Database Connection

- Open `db_connect.py`. The group's MySQL credentials are already setup:
  

---

## 👨‍💻 How to Use

### Start the App

```bash
python main.py
```

### Main Actions

- **Register:**  
  Follow prompts to create your account.

- **Login:**  
  Enter email and password.

- **Add Child:**  
  Input child's name, age, and health details.

- **Symptom Check:**  
  Answer questions; receive guidance or referral.

- **Receive Email:**  
  If registered, receive an email stating your advice nd referral on your email.

- **Guest Mode:**  
  Explore symptom checker without registration (limited features).

- **Menu Navigation:**  
  You can choose to check up another child, restart the app or quit.

---

## 🧩 Core Modules & Functions
- **admin.py**
  - `main`: contains the main logic where the admin is asked to add, delete question or quit.
  - `add_question`: asks the user for question details and add it
  - `delete_question`: deletes a question from the database according to the question text
  - Admin logic, authenticates admin and locks the admin if incorrect passwords are entered 3 times.
  - The correct password for the admin panel is `"earlyadmin"`

- **main.py**
  - `display_welcome()`: CLI welcome screen
  - `display_about()`: App description
  - `show_instructions()`: CLI instructions
  - `main()`: Entry logic (navigates to user actions)

- **db_connect.py**
  - `db_connect()`: Connects app to MySQL

- **user_class.py** (Class: `User`)
  - `Reg_user()`: Register parent/guardian
  - `Login()`: User authentication
  - `Child_details()`: Add/manage children
  - `Child_info()`: Gets all details of a user's children
  - `Guest()`: Use app as guest
  - `user_acess()`: Main post-login menu

- **questions.py**
  - `ask question()`: Loads and asks health questions based on age
  -  `Analyse risk`: analyses the risk associated with each answer using child age
  - `suggestion`: shows suggestion for each identified symptom and displays doctor's info


- **email_sender.py**
  - Sends email alert to the user

- **save_session.py**
  - `store_session_result`: stores the response and suggestion of each child analysis in the database.

- **exit_or_restart.py**
  - `exit_or_restart`: displays the final menu, for user to choose to either evaluate another child, restart app or quit.

- **colored_message.py**
  - `print`: our custom library, called to show messages in colors used as
  - print(text, color)

---

## 🗃️ Key Database Tables

```sql
CREATE TABLE IF NOT EXISTS users_parent (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    password VARCHAR(255),
    date_created DATETIME
);

CREATE TABLE IF NOT EXISTS children (
    child_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    name VARCHAR(255),
    age INT,
    prev_diagnosis TEXT,
    FOREIGN KEY(user_id) REFERENCES users_parent(user_id)
);
-- Key tables in the app powering other parts of the app
```
ONE-TO-MANY RELATIONSHIP
---

## 📧 Email Notification Setup

- The app uses Python's `smtplib` and `email` to send emails for each registered analysis.
- **Set up sender email and password in `email_sender.py`.**  
  (this is already setup using app password in gmail. Email: `earlyaid.notify@gmail.com`)

---

## 🙌 Contributing
All team members contributed in developing this working application

---

## 👩‍💻 Authors (Group 20, PLP EarlyAid Project)

- Helen Ugoeze Okereke
- Francis Shyaka
- Grace Karimi Njunge
- Erioluwa Mercy Akintayo 
- Cindy Teta
- Bendou Janna Vitalina Soeur 

---

## 💡 Inspiration

This project was developed as part of the **Peer Learning Project (PLP) Group 20** summative, in **ALU.**
The flowchart, schema diagram and screenshots are all in the document submitted

---
