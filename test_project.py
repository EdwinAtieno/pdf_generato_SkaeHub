import Database
import trail
import converting_to_pdf
import os
import csv, pdfs





# check database path
def test_database_path():
    is_database = Database.database('school.db')
    assert is_database == os.path.dirname(os.path.abspath(__file__))

#check if database exists
def test_values():
    existing = Database.database('school.db')
    assert existing

# Test to make sure that there is connection and size
def test_connection():
    # Test to make sure that there are 2 items in the database table
    cursor = Database.read_data('school.db')
    assert len(list(cursor.execute('SELECT * FROM school'))) == 3

# test if student_table.csv exists
def test_students_csv():
    type=converting_to_pdf.create_pdf(1)
    assert type

# test if execution os correct
def test_execute_sql():
    conn = Database.read_data('database/school.db')
    sql_out = conn.execute("SELECT * FROM schools WHERE Grade Low =9;")

    assert sql_out[0] == (10001,'Contoso High School',10001,9,12,'Amy Roebuck','2 Microsoft Way')


# check for the size of data in student table
def test_len_students_value():
    conn = Database.read_data('database/school.db')
    sql_out = conn.execute("SELECT * FROM students ;")
    assert len([sql_out]) == 87

# Test if the colums are correct
def test_len_teacher_value():
    conn = Database.read_data('database/school.db')
    sql_out = conn.execute("SELECT * FROM teachers ;")
    assert len([sql_out]) == 13

# Test if prints pdf school
def test_lenpages_school():
    pfd=converting_to_pdf.read_pdf(3)
    assert len([pfd]) == 0


# Test the no of pages of students.pdf
def test_lenpages_students():
    pfd=converting_to_pdf.read_pdf(1)
    assert len([pfd]) == 5

# Test the no of pages of teachers.pdf
def test_lenpages_teachers():
    pfd=converting_to_pdf.read_pdf(2)
    assert len([pfd]) == 1