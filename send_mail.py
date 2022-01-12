import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from Confidentials import SMTP_USERNAME, SMTP_PASSWORD

# The documents to attach to the e-mail
# 1st one :
filename_cv = "your_document.pdf"
cv = MIMEApplication(open(filename_cv, 'rb').read())
cv.add_header('Content-Disposition', 'attachment', filename=filename_cv)
# 2nd one :
filename_fiche = 'other_document.pdf'
comp = MIMEApplication(open(filename_fiche, 'rb').read())
comp.add_header('Content-Disposition', 'attachment', filename=filename_fiche)


SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_FROM = "prenom.nom@gmail.com"

EMAIL_SUBJECT = "Your e-mail subject here"

def send_email(NAME, EMAIL_TO):
    EMAIL_MESSAGE = """Hello {},\n\nMy name is Killiand and blablabla.\n\nKind regards,\n\nKillian \n\n""".format(NAME)
    s = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    s.starttls()
    s.login(SMTP_USERNAME, SMTP_PASSWORD)
    msg = MIMEMultipart()
    msg['Subject'] = EMAIL_SUBJECT
    msg['From'] = EMAIL_FROM
    msg['To'] = EMAIL_TO
    msgText = MIMEText(EMAIL_MESSAGE)
    msg.attach(msgText)
    msg.attach(cv)
    msg.attach(comp)
    #message = 'Subject: {}\n\n{}'.format(EMAIL_SUBJECT, EMAIL_MESSAGE)
    #message = message.encode('utf-8')
    s.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
    s.quit()

    
