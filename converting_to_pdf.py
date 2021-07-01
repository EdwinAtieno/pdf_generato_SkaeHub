import trail
import csv
from fpdf import FPDF
import PyPDF2

def create_pdf(n):

    if n == 1:
        trail.students_table()
        with open('pdfs/students_table.csv', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
                pdf = FPDF()
                pdf.add_page()
                page_width = pdf.w - 2 * pdf.l_margin

                pdf.set_font('Times', 'B', 14.0)
                pdf.cell(page_width, 0.0, 'Students Data', align='C')
                pdf.ln(10)

                pdf.set_font('Courier', '', 8)

                col_width = page_width / 8

                pdf.ln(1)

                th = pdf.font_size

                for row in reader:
                    # print(row)
                    pdf.cell(col_width, th, str(row[0]), border=1)
                    pdf.cell(col_width, th, row[1], border=1)
                    pdf.cell(col_width, th, row[2], border=1)
                    pdf.cell(col_width, th, row[3], border=1)
                    pdf.cell(col_width, th, row[4], border=1)
                    pdf.cell(col_width, th, row[5], border=1)
                    pdf.cell(col_width, th, row[6], border=1)
                    pdf.cell(col_width, th, row[7], border=1)
                    pdf.ln(th)

                pdf.ln(10)

                pdf.set_font('Times', '', 10.0)
                pdf.cell(page_width, 0.0, '- end of report -', align='C')

                pdf.output('student.pdf', 'F')
    if n == 2:
        trail.teachers_table()
        with open('pdfs/teacher_table.csv', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
                pdf = FPDF()
                pdf.add_page()
                page_width = pdf.w - 2 * pdf.l_margin

                pdf.set_font('Times', 'B', 14.0)
                pdf.cell(page_width, 0.0, 'Teachers Data', align='C')
                pdf.ln(10)

                pdf.set_font('Courier', '', 12)

                col_width = page_width / 5

                pdf.ln(1)

                th = pdf.font_size

                for row in reader:
                    # print(row)
                    pdf.cell(col_width, th, str(row[0]), border=1)
                    pdf.cell(col_width, th, row[1], border=1)
                    pdf.cell(col_width, th, row[2], border=1)
                    pdf.cell(col_width, th, row[3], border=1)
                    pdf.cell(col_width, th, row[4], border=1)
                    pdf.ln(th)

                pdf.ln(10)

                pdf.set_font('Times', '', 10.0)
                pdf.cell(page_width, 0.0, '- end of report -', align='C')

                pdf.output('teachers.pdf', 'F')
    if n == 3:
        trail.schools_table()
        with open('pdfs/school_table.csv', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
                pdf = FPDF()
                pdf.add_page()
                page_width = pdf.w -(-2) * pdf.l_margin

                pdf.set_font('Times', 'B', 14.0)
                pdf.cell(page_width, 0.0, 'Schools Data', align='C')
                pdf.ln(10)

                pdf.set_font('Courier', '', 8)

                col_width = page_width / 8

                pdf.ln(1)

                th = pdf.font_size

                for row in reader:
                    # print(row)
                    pdf.cell(col_width, th, str(row[0]), border=1)
                    pdf.cell(col_width, th, row[1], border=1)
                    pdf.cell(col_width, th, row[2], border=1)
                    pdf.cell(col_width, th, row[3], border=1)
                    pdf.cell(col_width, th, row[4], border=1)
                    pdf.cell(col_width, th, row[5], border=1)
                    pdf.cell(col_width, th, row[6], border=1)
                    pdf.ln(th)

                pdf.ln(10)

                pdf.set_font('Times', '', 10.0)
                pdf.cell(page_width, 0.0, '- end of report -', align='C')

                pdf.output('school.pdf', 'F')

    if n == 4:
        trail.students_table()
        with open('pdfs/students_table.csv', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
                pdf = FPDF()
                pdf.add_page()
                page_width = pdf.w - 2 * pdf.l_margin

                pdf.set_font('Times', 'B', 14.0)
                pdf.cell(page_width, 0.0, 'Students Data', align='C')
                pdf.ln(10)

                pdf.set_font('Courier', '', 8)

                col_width = page_width / 8

                pdf.ln(1)

                th = pdf.font_size

                for row in reader:
                    # print(row)
                    pdf.cell(col_width, th, str(row[0]), border=1)
                    pdf.cell(col_width, th, row[1], border=1)
                    pdf.cell(col_width, th, row[2], border=1)
                    pdf.cell(col_width, th, row[3], border=1)
                    pdf.cell(col_width, th, row[4], border=1)
                    pdf.cell(col_width, th, row[5], border=1)
                    pdf.cell(col_width, th, row[6], border=1)
                    pdf.cell(col_width, th, row[7], border=1)
                    pdf.ln(th)

                pdf.ln(10)

                pdf.set_font('Times', '', 10.0)
                pdf.cell(page_width, 0.0, '- end of report -', align='C')

                pdf.output('student.pdf', 'F')

        trail.teachers_table()
        with open('pdfs/teacher_table.csv', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
                pdf = FPDF()
                pdf.add_page()
                page_width = pdf.w - 2 * pdf.l_margin

                pdf.set_font('Times', 'B', 14.0)
                pdf.cell(page_width, 0.0, 'Teachers Data', align='C')
                pdf.ln(10)

                pdf.set_font('Courier', '', 12)

                col_width = page_width / 5

                pdf.ln(1)

                th = pdf.font_size

                for row in reader:
                    # print(row)
                    pdf.cell(col_width, th, str(row[0]), border=1)
                    pdf.cell(col_width, th, row[1], border=1)
                    pdf.cell(col_width, th, row[2], border=1)
                    pdf.cell(col_width, th, row[3], border=1)
                    pdf.cell(col_width, th, row[4], border=1)
                    pdf.ln(th)

                pdf.ln(10)

                pdf.set_font('Times', '', 10.0)
                pdf.cell(page_width, 0.0, '- end of report -', align='C')

                pdf.output('teachers.pdf', 'F')

        trail.schools_table()
        with open('pdfs/school_table.csv', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
                pdf = FPDF()
                pdf.add_page()
                page_width = pdf.w - (-2) * pdf.l_margin

                pdf.set_font('Times', 'B', 14.0)
                pdf.cell(page_width, 0.0, 'Schools Data', align='C')
                pdf.ln(10)

                pdf.set_font('Courier', '', 8)

                col_width = page_width / 8

                pdf.ln(1)

                th = pdf.font_size

                for row in reader:
                    # print(row)
                    pdf.cell(col_width, th, str(row[0]), border=1)
                    pdf.cell(col_width, th, row[1], border=1)
                    pdf.cell(col_width, th, row[2], border=1)
                    pdf.cell(col_width, th, row[3], border=1)
                    pdf.cell(col_width, th, row[4], border=1)
                    pdf.cell(col_width, th, row[5], border=1)
                    pdf.cell(col_width, th, row[6], border=1)
                    pdf.ln(th)

                pdf.ln(10)

                pdf.set_font('Times', '', 10.0)
                pdf.cell(page_width, 0.0, '- end of report -', align='C')

                pdf.output('school.pdf', 'F')







def read_pdf(n):
    if n==1:
        # creating a pdf file object
        pdfFileObj = open('students.pdf', 'rb')

        # creating a pdf reader object
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

        # printing number of pages in pdf file
        print(pdfReader.numPages)

        # creating a page object
        pageObj = pdfReader.getPage(0)

        # extracting text from page
        print(pageObj.extractText())

        # closing the pdf file object
        pdfFileObj.close()
    elif n==2:
        # creating a pdf file object
        pdfFileObj = open('teachers.pdf', 'rb')

        # creating a pdf reader object
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

        # printing number of pages in pdf file
        print(pdfReader.numPages)

        # creating a page object
        pageObj = pdfReader.getPage(0)

        # extracting text from page
        print(pageObj.extractText())

        # closing the pdf file object
        pdfFileObj.close()
    elif n==3:
        # creating a pdf file object
        pdfFileObj = open('school.pdf', 'rb')

        # creating a pdf reader object
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

        # printing number of pages in pdf file
        print(pdfReader.numPages)

        # creating a page object
        pageObj = pdfReader.getPage(0)

        # extracting text from page
        print(pageObj.extractText())

        # closing the pdf file object
        pdfFileObj.close()

def main():
    n=int(input("enter 1=student.pdf\n 2=teacher.pdf\n 3=school.pdf"))
    while n <=3:
        read_pdf(n)
    print("wrong choice")
if __name__ == '__main__':
    main()