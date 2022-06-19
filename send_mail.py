import time
import smtplib
from email.message import EmailMessage

class Mail:
    def __init__(self) -> None:
        pass

    # sending mail
    def sendMail(self,message):
        
        message = "STATUS (ETL-Project1) :\n"+message
        mail = EmailMessage()
        sendtime = time.strftime("at %H:%M:%S, on %D/%M/%Y")
        mail['Subject'] = "ETL done "+sendtime[0:len(sendtime)-8]
        mail['From'] = "< FROM ID >"
        mail['To'] = "< TO ID >"
        mail.set_content(message)
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login("< SENDING MAIL ID >","< MAIL ID PASSWORD >")
        server.send_message(mail)
        server.close()
