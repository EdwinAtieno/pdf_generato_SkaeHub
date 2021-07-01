import os
import smtplib
import trail
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('email')
EMAIL_PASSWORD = os.environ.get('password')

def number_of_contact(n,meso,cont,pdf):
    content=cont
    msg = EmailMessage()
    meso=meso
    contacts = n
    msg['Subject'] = meso
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = contacts
    msg.set_content(content)

    files=pdf
    for file in files:
        with open(file, 'rb') as f:
            file_data = f.read()
            file_name= f.name
        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)


    smtp= smtplib.SMTP_SSL( 'smtp.gmail.com', 465)
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)






def main(att):
        meso=input("Enter the subject:\n")
        content=input("Enter message to receiver\n")

        pdf=[]
        all=['student.pdf','teachers.pdf','school.pdf']
        if att ==1:
            pdf.append('student.pdf')
        if att ==2:
            pdf.append('teachers.pdf')
        if att == 3:
            pdf.append('school.pdf')
        if att == 4:
            pdf= all

        em= int(input("enter the number of emails to send:  "))
        n=[]
        for i in range(em):
            emails=input("enter email; \n")
            n.append(emails)
        print("these are the emails to be sent to ", n)
        number_of_contact(n, meso, content, pdf)

if __name__ == '__main__':
    main()