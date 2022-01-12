import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from Confidentials import SMTP_USERNAME, SMTP_PASSWORD

filename_cv = "CV_KS.pdf"
cv = MIMEApplication(open(filename_cv, 'rb').read())
cv.add_header('Content-Disposition', 'attachment', filename=filename_cv)

filename_fiche = 'fiche_competences_Mag_1A_2021-2022.pdf'
comp = MIMEApplication(open(filename_fiche, 'rb').read())
comp.add_header('Content-Disposition', 'attachment', filename=filename_fiche)

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_FROM = "killian.steunou@gmail.com"

EMAIL_SUBJECT = "Stage fin de 3A TSE"

def send_email(NAME, EMAIL_TO):
    EMAIL_MESSAGE = """Bonjour {},\n\nJe suis en 3ème année d’Éco-Maths à TSE et en Magistère d'Économiste Statisticien, et je recherche un stage de 3 à 4 mois débutant en mai 2022.\n\nJe suis passionné par l’Intelligence Artificielle, la Data Science et tout ce qui touche au Big Data.\nGrâce à la première année de Magistère, j’ai acquis des compétences d’analyse de données (k-means clustering, ACP, AFC…), et je maitrise très bien les langages R et Python (je réalise régulièrement des projets en Python, je m’intéresse de près à la programmation).\n\nLe stage que je recherche serait donc orienté Data Science/Analysis, et dans l’idéal me permettrait d’apprendre à utiliser un outil de Data Visualisation (comme Tableau, PowerBI ou Dataiku), compétence qu’il m’est nécessaire d’acquérir pour mener à bien mon projet professionnel.\n\nSavez-vous si mon profil pourrait intéresser votre entreprise en tant que stagiaire ?\n\nJe reste disponible pour en discuter,\nMerci pour votre aide,\n\nKillian Steunou\n\nTel : +33 6 95 74 30 22\n@ : killian.steunou@gmail.com\n\np.s. : mon cv est en pièce jointe, ainsi qu’une fiche de compétence, au cas où :)\n""".format(NAME)
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

    