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

INSERT INTO doctors (name, specialty, phone, location, start_age_group, end_age_group, risk_level)
VALUES
('Dr. Alice Umutoni', 'Pediatrics', '+250781111111', 'Kigali', 0, 12, 'Low'),
('Dr. Jean Niyonzima', 'Child Psychology', '+250782222222', 'Musanze', 4, 12, 'Medium'),
('Dr. Grace Mukamana', 'Pediatric Surgery', '+250783333333', 'Huye', 1, 12, 'High'),
('Dr. Eric Bizimana', 'Neonatology', '+250784444444', 'Rubavu', 0, 1, 'High'),
('Dr. Diane Ishimwe', 'Pediatric Nutrition', '+250785555555', 'Muhanga', 0, 12, 'Medium'),
('Dr. Peter Habimana', 'Pediatric Dentistry', '+250786666666', 'Gicumbi', 2, 12, 'Low'),
('Dr. Laura Uwase', 'Developmental Pediatrics', '+250787777777', 'Nyagatare', 0, 8, 'Medium'),
('Dr. Samuel Rugamba', 'Pediatric Infectious Diseases', '+250788888888', 'Rusizi', 0, 12, 'High'),
('Dr. Christine Ingabire', 'Pediatric Cardiology', '+250789999999', 'Nyanza', 3, 12, 'High'),
('Dr. John Karangwa', 'Pediatric Pulmonology', '+250790000000', 'Rulindo', 5, 12, 'Medium'),
('Dr. Anita Uwase', 'Pediatrics', '+250790234567', 'Rwamagana', 0, 12, 'Low'),
('Dr. Alain Ndayambaje', 'Pediatric Neurology', '+250790345678', 'Bugesera', 2, 12, 'Medium'),
('Dr. Solange Umuhoza', 'Pediatric Dermatology', '+250790456789', 'Karongi', 0, 12, 'Low'),
('Dr. Patrick Tuyisenge', 'Pediatric Cardiology', '+250790567890', 'Burera', 1, 12, 'High'),
('Dr. Keza Ishimwe', 'Child Psychiatry', '+250790678901', 'Kirehe', 4, 12, 'Medium'),
('Dr. David Gatera', 'Pediatric Infectious Diseases', '+250790789012', 'Ngoma', 0, 12, 'High'),
('Dr. Florence Mukeshimana', 'Pediatric Pulmonology', '+250790890123', 'Nyamasheke', 3, 12, 'High'),
('Dr. Jeanette Uwizeye', 'Developmental Pediatrics', '+250790901234', 'Kamonyi', 0, 10, 'Medium'),
('Dr. Claude Nkurunziza', 'Pediatric Gastroenterology', '+250791012345', 'Nyaruguru', 1, 12, 'Medium'),
('Dr. Aline Kankindi', 'Pediatric Endocrinology', '+250791123456', 'Gatsibo', 5, 12, 'Medium');

