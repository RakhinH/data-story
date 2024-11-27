import sqlite3

# Connect to the database
conn = sqlite3.connect('example.db')
c = conn.cursor()

# Create tables
c.execute('''CREATE TABLE IF NOT EXISTS Student_info (
                student_id INTEGER PRIMARY KEY,
                teacher_id INTEGER,
                student_first TEXT,
                student_last TEXT,
                student_attendance INTEGER,
                student_course TEXT,
                FOREIGN KEY (parent_id) REFERENCES Parent_info(student_parent_id)
                FOREIGN KEY(student_contact) REFERENCES Student_contact_info(student_contact_info_id),
                
             )''')

c.execute('''CREATE TABLE IF NOT EXISTS Student_contact_info (
                student_contact_info_id INTEGER PRIMARY KEY,
                student_email_address TEXT,
                student_house_address TEXT,
                student_number INTEGER,
                student_nickname TEXT,

             )''') 

c.execute('''CREATE TABLE IF NOT EXISTS Parent_info (
                student_parent_id INTEGER PRIMARY KEY, 
                student_id  INTEGER,
                parent_first TEXT,
                parent_last TEXT,
                FOREIGN KEY(parent_contact) REFERENCES Parent_contact_info(parent_contact_info_id),
             )''')

c.execute('''CREATE TABLE IF NOT EXISTS Parent_contact_info (
                parent_contact_info_id INTEGER PRIMARY KEY,
                parent_email_address TEXT,
                parent_house_address TEXT,
                parent_number INTEGER,
                parent_nickname TEXT,
             )''')

c.execute('''CREATE TABLE IF NOT EXISTS Teacher_info (
                teacher_id INTEGER PRIMARY KEY,
                teacher_first TEXT,
                teacher_last TEXT,
                FOREIGN KEY(teacher_contact) REFERENCES Teacher_contact_info(teacher_contact_info_id),
             )''')   

c.execute('''CREATE TABLE IF NOT EXISTS Teacher_contact_info (
                teacher_contact_info_id INTEGER PRIMARY KEY
                teacher_number INTEGER,
                teacher_email_address TEXT,a
                teacher_nickname TEXT,
             )''')               






c.execute("INSERT INTO ")

conn.close()