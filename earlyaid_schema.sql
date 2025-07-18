CREATE DATABASE IF NOT EXISTS earlyaid_db;
USE earlyaid_db;

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

CREATE TABLE IF NOT EXISTS doctors (
    doctor_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    specialty VARCHAR(255),
    phone VARCHAR(50),
    location VARCHAR(255),
    start_age_group INT,
    end_age_group INT,
    risk_level VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS questions (
    question_id INT AUTO_INCREMENT PRIMARY KEY,
    question_text TEXT,
    start_age INT,
    end_age INT,
    option_a TEXT NOT NULL,
    option_b TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS question_risks (
    risk_id INT AUTO_INCREMENT PRIMARY KEY,
    question_id INT,
    min_age INT,
    max_age INT,
    risk_level INT,
    suggestion_code VARCHAR(50),
    FOREIGN KEY(question_id) REFERENCES questions(question_id),
    INDEX(suggestion_code)
);

CREATE TABLE IF NOT EXISTS suggestions (
    suggestion_id INT AUTO_INCREMENT PRIMARY KEY,
    suggestion_code VARCHAR(50),
    risk_level INT,
    advice TEXT,
    FOREIGN KEY(suggestion_code) REFERENCES question_risks(suggestion_code)
);

CREATE TABLE IF NOT EXISTS responses (
    response_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    child_id INT NOT NULL,
    answer TEXT,
    suggestion TEXT,
    risk_score INT,
    timestamp DATETIME,
    FOREIGN KEY(user_id) REFERENCES users_parent(user_id),
    FOREIGN KEY(child_id) REFERENCES children(child_id)
);

