import sqlite3
import csv
import pytest



def database(dabase_path):
    # database stored in the memory
    conn = sqlite3.connect(dabase_path)
    try:
        c = conn.cursor()
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
    except sqlite3.Error as e:
        print(e, "Sorry something went wrong")

@pytest.fixture
def read_data(dabase_path):

    conn = sqlite3.connect(dabase_path)
    c = conn.cursor()
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
def main():
    database('database/school.db')
    read_data('database/school.db')




if __name__ == '__main__':
    main()