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

--inserting into the questions table
select * from questions;

insert into questions(question_text, start_age, end_age, option_a, option_b) values
                                                                                 ('Is the child Vomiting?', 0, 12, 'Yes', 'No');

insert into questions (question_text, start_age, end_age, option_a, option_b) values
    ('Does the child have a fever?', 0, 12, 'Yes', 'No');

insert into questions (question_text, start_age, end_age, option_a, option_b) values
    ('Is the baby experiencing watery stools?', 0, 2, 'Yes', 'No');
insert into questions (question_text, start_age, end_age, option_a, option_b) values
    ('Has the baby been having trouble sleeping or staying awake?', 0, 2, 'Yes', 'No');
insert into questions (question_text, start_age, end_age, option_a, option_b) values
    ('Is the child refusing to drink fluids or eat?', 0, 2, 'Yes', 'No');

insert into questions (question_text, start_age, end_age, option_a, option_b) values
    ('Is the child feeling any stomach pain or discomfort?', 3, 5, 'Yes', 'No');


insert into questions (question_text, start_age, end_age, option_a, option_b) values
    ('Is the child experiencing a persistent headache?', 3, 12, 'Yes', 'No');
insert into questions (question_text, start_age, end_age, option_a, option_b) values
    ('Has the child been feeling weak or dizzy?', 3, 12, 'Yes', 'No');
insert into questions (question_text, start_age, end_age, option_a, option_b) values
    ('Is the child experiencing frequent urination or increased thirst?', 6, 12, 'Yes', 'No');

update question_risks set risk_level = 2 where risk_id = 9;
select * from question_risks;


-- General Questions (0-12 Years)

-- Is the child Vomiting?
insert into question_risks (question_id, min_age, max_age, risk_level, suggestion_code) values
    (1, 0, 2, 3, 'vomiting_in_babies'),  -- High risk for 0-2 years
    (1, 3, 12, 2, 'vomiting_in_children');

-- Does the child have a fever?
insert into question_risks (question_id, min_age, max_age, risk_level, suggestion_code) values
    (2, 0, 2, 3, 'fever_in_babies'),  -- High risk for 0-2 years
    (2, 3, 5, 2, 'fever_in_children'),  -- Medium risk for 3-5 years
    (2, 6, 12, 1, 'fever_in_older_children'); -- Low risk for 6-12 years

-- Is the baby experiencing watery stools?
insert into question_risks (question_id, min_age, max_age, risk_level, suggestion_code) values
    (3, 0, 2, 3, 'watery_stools_in_babies');  -- High risk for 0-2 years

-- Has the baby been having trouble sleeping or staying awake?
insert into question_risks (question_id, min_age, max_age, risk_level, suggestion_code) values
    (4, 0, 2, 2, 'sleep_trouble_in_babies');  -- Medium risk for 0-2 years

-- Is the child refusing to drink fluids or eat?
insert into question_risks (question_id, min_age, max_age, risk_level, suggestion_code) values
    (5, 0, 2, 3, 'refusing_to_eat_in_babies'),  -- High risk for 0-2 years
    (5, 3, 12, 2, 'refusing_to_eat_in_children');

-- Is the child feeling any stomach pain or discomfort?
insert into question_risks (question_id, min_age, max_age, risk_level, suggestion_code) values
    (6, 3, 5, 3, 'stomach_pain_in_children'),  -- Medium risk for 3-5 years
    (6, 6, 12, 2, 'stomach_pain_in_older_children'); -- Low risk for 6-12 years

-- Is the child experiencing a persistent headache?
insert into question_risks (question_id, min_age, max_age, risk_level, suggestion_code) values
    (7, 3, 12, 2, 'persistent_headache_in_children');

-- Is the child experiencing frequent urination?
insert into question_risks (question_id, min_age, max_age, risk_level, suggestion_code) values
    (8, 3, 5, 3, 'weakness_in_children'),
(8, 6, 12, 2, 'weakness_in_older_children');

insert into question_risks (question_id, min_age, max_age, risk_level, suggestion_code) values
    (8, 6, 12, 2, 'frequent_urination_in_children');



--suggestions table
-- Suggestion for vomiting in babies (High Risk)
insert into suggestions (suggestion_code, risk_level, advice) values
    ('vomiting_in_babies', 3, 'Ensure the baby stays hydrated with small sips of water or oral rehydration solution.');

-- Suggestion for vomiting in children (Medium Risk)
insert into suggestions (suggestion_code, risk_level, advice) values
    ('vomiting_in_children', 2, 'Keep the child hydrated and offer light foods like crackers or Pap. Avoid solid foods until vomiting stops.');

-- Suggestion for fever in babies (High Risk)
insert into suggestions (suggestion_code, risk_level, advice) values
    ('fever_in_babies', 3, 'Use a lukewarm bath or sponge to help reduce fever. Ensure the baby drink plenty water or breast milk.');

-- Suggestion for fever in children (Medium Risk)
insert into suggestions (suggestion_code, risk_level, advice) values
    ('fever_in_children', 2, 'Offer cool drinks and ensure the child rests. A light bath can help lower body temperature.');

-- Suggestion for fever in older children (Low Risk)
insert into suggestions (suggestion_code, risk_level, advice) values
    ('fever_in_older_children', 1, 'Give the child plenty of fluids and rest. Use fever-reducing medications like acetaminophen as directed.');

-- Suggestion for watery stools in babies (High Risk)
insert into suggestions (suggestion_code, risk_level, advice) values
    ('watery_stools_in_babies', 2, 'This may be due to tooth growth or stomach development. Ensure the baby gets frequent, small sips of water or breast milk to prevent dehydration.');

-- Suggestion for sleep trouble in babies (Medium Risk)
insert into suggestions (suggestion_code, risk_level, advice) values
    ('sleep_trouble_in_babies', 2, 'Try establishing a calming bedtime routine. Ensure the baby’s environment is quiet and comfortable.');

-- Suggestion for refusing to eat in babies (High Risk)
insert into suggestions (suggestion_code, risk_level, advice) values
    ('refusing_to_eat_in_babies', 3, 'Offer small, frequent feedings and check for signs of dehydration. Keep the baby comfortable. Check if the child is loosing weight');

-- Suggestion for refusing to eat in children (Medium Risk)
insert into suggestions (suggestion_code, risk_level, advice) values
    ('refusing_to_eat_in_children', 2, 'Offer light, easy-to-digest foods. Encourage hydration and rest. Be patient as the child may regain appetite slowly.');

-- Suggestion for stomach pain in children (Medium Risk)
insert into suggestions (suggestion_code, risk_level, advice) values
    ('stomach_pain_in_children', 2, 'Give the child light meals and ensure they stay hydrated. Use a warm compress to soothe stomach discomfort. let them sleep with the stomach resting on the bed');

-- Suggestion for stomach pain in older children (Low Risk)
insert into suggestions (suggestion_code, risk_level, advice) values
    ('stomach_pain_in_older_children', 1, 'Encourage rest and provide a warm compress to the abdomen. Offer fluids like clear soups or water.');

-- Suggestion for persistent headache in children (Medium Risk)
insert into suggestions (suggestion_code, risk_level, advice) values
    ('persistent_headache_in_children', 2, 'Encourage the child to rest in a quiet, dark room. Offer pain relievers as needed, and keep them hydrated.');

-- Suggestion for weakness in children (High Risk)
insert into suggestions (suggestion_code, risk_level, advice) values
    ('weakness_in_children', 3, 'Ensure the child rests and drinks plenty of fluids. Feed the child with warm milk');

-- Suggestion for weakness in older children (Medium Risk)
insert into suggestions (suggestion_code, risk_level, advice) values
    ('weakness_in_older_children', 2, 'Encourage rest, hydration, and easy-to-digest meals like milk and egg. Monitor for any additional symptoms.');

-- Suggestion for frequent urination in children (Medium Risk)
insert into suggestions (suggestion_code, risk_level, advice) values
    ('frequent_urination_in_children', 2, 'Make sure the child drinks enough water, but avoid excessive sugar or caffeine. Monitor for any additional symptoms.');

select * from suggestions