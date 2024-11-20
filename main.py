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
                student_contact_info_id INTEGER,
                student_attendance INTEGER,
                student_course TEXT,
                FOREIGN KEY(student_timetable) REFERENCES Timetable(id),
                
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
                student_id  INTEGER,
                parent_first TEXT,
                parent_last TEXT,
                parent_contact_info_id INTEGER,
             )''')

c.execute('''CREATE TABLE IF NOT EXISTS Parent_contact_info (
                parent_contact_info_id INTEGER PRIMARY KEY,
                parent_email_address TEXT,
                parent_house_address TEXT,
                parent_number INTEGER,
                parent_nickname TEXT,
             )''')

c.execute('''CREATE TABLE IF NOT EXISTS Teacher_info (
                
             )''')   

c.execute('''CREATE TABLE IF NOT EXISTS Teacher_contact_info (
                
             )''')               

c.execute('''CREATE TABLE IF NOT EXISTS Timetable (
                
             )''')
c.execute('''CREATE TABLE IF NOT EXISTS Books (
                id INTEGER PRIMARY KEY,
                title TEXT,
                author_id INTEGER,
                FOREIGN KEY(author_id) REFERENCES Authors(id)
             )''')



conn.close()