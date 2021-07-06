# import the necessary imports
import os
import smtplib
import main
import imghdr

# import EmailMessage function
from email.message import EmailMessage

# use the os get() to get my email password and username
# they are saved in the computer to help protect your privacy.
EMAIL_ADDRESS = os.environ.get('email')
EMAIL_PASSWORD = os.environ.get('password')

# function which will help in creating an email for the user
def number_of_contact(n,meso,cont,pdf):
    content=cont
    msg = EmailMessage()
    meso=meso

    # Email sending format
    contacts = n
    msg['Subject'] = meso
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = contacts
    msg.set_content(content)

    #loop for attaching the pdfs to your email
    files=pdf
    for file in files:
        with open(file, 'rb') as f:
            file_data = f.read()
            file_name= f.name
        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    # Creating connection with my email
    smtp= smtplib.SMTP_SSL( 'smtp.gmail.com', 465)
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
    return msg





# main function
def main(att):
        # prompt the user to write the subject
        # and full message
        meso=input("Enter the subject:\n")
        content=input("Enter message to receiver\n")

        # create a list which will contain the attachments to be sent
        pdf=[]
        all=['student.pdf','teachers.pdf','school.pdf']
        if att ==1:
            pdf.append('student.pdf')
        if att ==2:
            pdf.append('teachers.pdf')
        if att == 3:
            pdf.append('school.pdf')
        if att == 4:
            pdf.append('School_DB.pdf')

        # Ask user for the number of email to receive the email
        em= int(input("enter the number of emails to send:  "))
        n=[]

        # loop that accepts more than email address
        for i in range(em):
            emails=input("enter email, correct format jsjddj@gmail.com; \n")
            n.append(emails)
        print("these are the emails to be sent to ", n)

        # call the number_of_contact function
        number_of_contact(n, meso, content, pdf)

#if __name__ == '__main__':
 #   main()