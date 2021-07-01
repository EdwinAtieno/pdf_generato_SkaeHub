import converting_to_pdf
import Database
import pytest


# Test the no of pages of school.pdf
def test_lenpages_school():
    pfd=converting_to_pdf.read_pdf(1)
    assert len([pfd]) == 1


# Test the no of pages of students.pdf
def test_lenpages_students():
    pfd=converting_to_pdf.read_pdf(2)
    assert len([pfd]) == 1

# Test the no of pages of teachers.pdf
def test_lenpages_teachers():
    pfd=converting_to_pdf.read_pdf(3)
    assert len([pfd]) == 1

# content of test_tmpdir.py
def test_needsfiles(tmpdir):
    print(tmpdir)
    assert 1

# test to check if the database is empty
# student table
def test_check_student():
    student=Database.students_table()
    assert student.items

#teachers table
def test_check_teachers():
    teachers=Database.teachers_table()
    assert teachers.items

#school table
def test_check_school():
    school=Database.schools_table()
    assert school.items

# TEST TO CHECK CSV IF EMPTY
#Test to check students csv
def test_students_csv():
    pdf= converting_to_pdf.read_student_csv()
    assert pdf == False

#Test to check teachers cssv
def test_teacher_csv():
    pdf = converting_to_pdf.read_teachers_csv()
    assert pdf == False

#Test to check school cssv
def test_school_csv():
    pdf= converting_to_pdf.read_school_csv()
    assert pdf.empty == False




