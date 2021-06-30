import sqlite3
import pdfkit
import converting_to_pdf
import csv
import pandas as pd
from fpdf import FPDF
def students_table():
      conn = sqlite3.connect('database/school.db')
      db_df = pd.read_sql_query("SELECT * FROM students", conn)
      db_df.to_csv('pdfs/students_table.csv', index=False)


def teachers_table():
    conn = sqlite3.connect('database/school.db')
    db_df = pd.read_sql_query("SELECT * FROM teachers", conn)
    db_df.to_csv('pdfs/teacher_table.csv', index=False)
def schools_table():
    conn = sqlite3.connect('database/school.db')
    db_df = pd.read_sql_query("SELECT * FROM schools", conn)
    db_df.to_csv('pdfs/school_table.csv', index=False)

def main():
    n = int(input("choose which table to send: \n 1. students \n 2. teachers \n 3. schools \n "))
    converting_to_pdf.create_pdf(n)

if __name__ == '__main__':
    main()