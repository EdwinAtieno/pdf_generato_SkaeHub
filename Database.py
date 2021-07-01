import sqlite3
import csv
import pandas as pd
conn = sqlite3.connect('database/school.db')
c = conn.cursor()
"""
def database():
    # database stored in the memory
    conn = sqlite3.connect('database/school.db')
    c = conn.cursor()
    conn.close()"""
def create_tables():

    c.execute("""
                    CREATE TABLE students(
                        SIS_ID integer,
                        School_SIS_ID integer,
                        First_Name message_text ,
                        Last_Name message_text ,
                        Student_Number integer,
                        Middle_Name message_text,
                        Grade integer,
                        Graduation_Year date
                        )""")

    c.execute("""CREATE TABLE teachers (
                        School_SIS_ID	integer,
                        First_Name	message_text,
                        Last_Name	message_text,
                        Middle_Name	message_text,
                        Teacher_Number	integer     
                        )""")

    c.execute("""CREATE TABLE schools (
                        SIS_ID	integer,
                        Name	message_text,
                        School_Number	integer,
                        Grade_Low	integer ,
                        Grade_High	integer ,
                        Principal_Name	message_text ,
                        Address	message_text 
                            )""")
    conn.commit()

def insert_data():

    with open('csv/Student.csv', 'r') as student:
        no_students=0
        for row in student:
             c.execute("INSERT INTO students VALUES (?,?,?,?,?,?,?,?)", row.split(","))
             conn.commit()
             no_students +=1

    #c.execute("SELECT * FROM students")
    #print(c.fetchall())
    print("\n {} Records transferred".format(no_students))

    with open('csv/Teacher.csv', 'r') as teacher:
          no_teacher=0
          for row in teacher:
               c.execute("INSERT INTO teachers VALUES (?,?,?,?,?)", row.split(","))
               conn.commit()
               no_teacher +=1
             #c.execute("SELECT * FROM students")
            #print(c.fetchall())
    print("\n {} Records transferred".format(no_teacher))

    with open('csv/School.csv', 'r') as school:
         no_school=0
         for row in school:
             c.execute("INSERT INTO schools VALUES (?,?,?,?,?,?,?)", row.split(","))
             conn.commit()
             no_school +=1

            #c.execute("SELECT * FROM students")
            #print(c.fetchall())
    print("\n {} Records transferred".format(no_school))
    conn.close()


def students_table():
    conn = sqlite3.connect('database/school.db')
    db_df = pd.read_sql_query("SELECT * FROM students", conn)
    return db_df
def teachers_table():
    conn = sqlite3.connect('database/school.db')
    db_df = pd.read_sql_query("SELECT * FROM teachers", conn)
    return db_df

def schools_table():
    conn = sqlite3.connect('database/school.db')
    db_df = pd.read_sql_query("SELECT * FROM schools", conn)
    return db_df


def main():
    #database()
    create_tables()
    insert_data()
    students_table()

if __name__ == '__main__':
    main()
