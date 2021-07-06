""" import sqlite 3 to read databse
also import other files so as to use them in the project"""
import sqlite3
import pdfkit
import converting_to_pdf
import csv
import send_email
import pandas as pd
from fpdf import FPDF

# function which extracts students data from student table then convert it to CSV
def student_table():
      conn = sqlite3.connect('database/school.db')
      db_df = pd.read_sql_query("SELECT * FROM students", conn)
      db_df.to_csv('pdfs/students_table.csv', index=False)

# function which extracts teachers data from teachers table then convert it to CSV
def teachers_table():
    conn = sqlite3.connect('database/school.db')
    db_df = pd.read_sql_query("SELECT * FROM teachers", conn)
    db_df.to_csv('pdfs/teacher_table.csv', index=False)

# function which extracts school data from school table then convert it to CSV
def schools_table():
    conn = sqlite3.connect('database/school.db')
    db_df = pd.read_sql_query("SELECT * FROM schools", conn)
    db_df.to_csv('pdfs/school_table.csv', index=False)

# function which prompts user for input also used to call the other functions
def main():
    n = int(input("choose which table to print: \n 1. students \n 2. teachers \n 3. schools \n 4. all \n"))
    converting_to_pdf.create_pdf(n)
    pdf=int(input("choose which table to send: \n 1. students \n 2. teachers \n 3. schools \n 4. All \n"))
    send_email.main(pdf)

if __name__ == '__main__':
    main()