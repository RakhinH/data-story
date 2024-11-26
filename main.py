import sqlite3

# Connect to the database
conn = sqlite3.connect('example.db')
c = conn.cursor()

# Create tables
c.execute('''CREATE TABLE IF NOT EXISTS Student_info (
                student_id INTEGER PRIMARY KEY,
                FOREIGN KEY (teacher_student_id) REFERENCES Teacher_info(teacher_id),
                student_first TEXT,
                student_last TEXT,
                FOREIGN KEY (student_contact) REFERENCES Student_contact_info(student_contact_info_id),
                student_attendance INTEGER,
                student_course TEXT,
                
             )''')

c.execute('''CREATE TABLE IF NOT EXISTS Student_contact_info (
                student_contact_info_id INTEGER PRIMARY KEY,
                student_email_address TEXT, 
                student_house_address TEXT,
                student_number INTEGER,
                student_nickname TEXT,

             )''') 

c.execute('''CREATE TABLE IF NOT EXISTS Parent_info (
                parent_id INTEGER PRIMARY KEY,
                parent_first TEXT,
                parent_last TEXT,
                FOREIGN KEY (parent_contact) REFERENCES Parent_contact_info(parent_contact_info_id),
             )''')

c.execute('''CREATE TABLE IF NOT EXISTS Parent_contact_info (
                parent_contact_info_id INTEGER PRIMARY KEY,
                parent_email_address TEXT,
                parent_house_address TEXT,
                parent_number INTEGER,
                parent_nickname TEXT,
             )''')

c.execute('''CREATE TABLE IF NOT EXISTS Teacher_info (
               PRIMARY KEY teacher_id INTEGER,
               FOREIGN KEY (teacher_contact) REFERENCES Teacher_contact_info(teacher_contact_info_id),
               teacher_qualification TEXT,
               teacher_first TEXT,
               teacher_last TEXT,
             )''')   

c.execute('''CREATE TABLE IF NOT EXISTS Teacher_contact_info (
               PRIMARY KEY teacher_contact_info_id INTEGER,
               teacher_number INTEGER,
               teacher_email_address TEXT,
               teacher_nickname TEXT,
               teacher_house_address TEXT,
             )''') 

c.execute("INSERT INTO Student_info VALUES (, 1, 'John', 'Doe', 1, 'Math', 90)")            
                




conn.close()