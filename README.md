
1. Installation and setup

First clone this repository to your local machine using https://github.com/EdwinAtieno/pdf_generator_SkaeHub.git

Checkout into the master branch using git checkout master

Create a virtualenv on your machine and install the dependencies via pip install -r requirements.txt and activate it.

cd into the app folder and run python run-app.py --interactive
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

SUPPORTING VIDEOS
1) TESTING PROJECT:
    Database, Csv, pdf and email
    ![PROJECT TEST](https://user-images.githubusercontent.com/60142434/124177159-87ac8480-dab8-11eb-9474-06548cb96ceb.gif)
    
    
2) DATABASE CREATION
    Reading data from CSV convert to database
    ![Data creation](https://user-images.githubusercontent.com/60142434/124177247-a14dcc00-dab8-11eb-931f-ed466205aa71.gif)
    
    
    
3) PDF GENERATING AND SENDING THROUGH EMAIL
    Main task was to create pdf and be able to send copies 
    ![Pdf generator and email](https://user-images.githubusercontent.com/60142434/124177338-c4787b80-dab8-11eb-9050-4e267447f8cd.gif)
    
    
    
    
    

    
    
    
    
    


