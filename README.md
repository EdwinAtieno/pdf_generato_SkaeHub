
1)REQUIREMENTS_SET_UP
 atomicwrites==1.4.0, attrs==21.2.0, colorama==0.4.4,cycler==0.10.0, fpdf==1.7.2
fpdf2==2.4.2,iniconfig==1.1.1 ,kiwisolver==1.3.1 ,matplotlib==3.4.2 ,numpy==1.21.0 ,packaging==20.9
pandas==1.2.5, pandoc==1.1.0 ,pdfkit==0.6.1 ,Pillow==8.2.0, pluggy==0.13.1, plumbum==1.7.0
ply==3.11,py==1.10.0, pypandoc==1.5, pyparsing==2.4.7, pyPdf==1.13, PyPDF2==1.26.0, pypiwin32==223
pytest==6.2.4, python-dateutil==2.8.1, pytz==2021.1, pywin32==301, six==1.16.0, tabula==1.0.5
toml==0.10.2, wkhtmltopdf==0.2, Wrapper==1.1.0b1
<a source="https://user-images.githubusercontent.com/35099243/123341302-6bf42c00-d556-11eb-8d2e-67dcb030361b.png" href=""></a>

PDF GENERATOR
CLI app that reads the contents of a simple SQLite school database and convert the whole database to a single PDF document. Prompt the user for an email address to send the PDF to. The email should be a proper one with the header, body, designation and PDF attachment.


Process:
1)	Should have a database.
2)	Should incorporate an email.
Database conversion:
1)	Have a database
2)	Connect database SQLITE using python
3)	Read data from a database
4)	Select table to print
5)	Convert database to pdf.
6)	Have a menu to send email



Email part :
1)	Set up the SMTP server and log into your account
2)	Create MIME
3)	Add sender, receiver address into the MIME
4)	Add the mail title into the MIME
5)	Attach the body into the MIME
6)	Open the file as binary mode, which is going to be attached with the email
7)	Read the byte stream and encode the attachment using base64 encoding scheme.
8)	Add header for the attachments.
9)	Start the SMTP session with valid port number with proper security features
10)	Login to the system
11)	Send mail and exit
# Boot_Camp_Project



ALGORITHM:
  1) Create a database
  2) connect database
  3) read the database
  4) Display menu: to select convert 1) all 
  5)                                 2) specific
  6) convert to pdf
  7) ask user if wants to send
  8) Prompt user to input email, header, body, designation and PDF attachment

PROJECT BREAKDOWN
1) Create a database and input values
   -Test
2) Create a pdf converter
   -Test
3) Email set up
    -Test




