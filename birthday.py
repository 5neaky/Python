import csv
import smtplib
import ssl
from datetime import date
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def check_birthday():
    # today's date as 3 strings
    today_month, today_day, today_year = date.today().strftime('%m/%d/%Y').split('/')
    # birthday as 3 strings
    p_day, p_month, p_year = birthday.split('.')

    if today_day == p_day and today_month == p_month:
        return True
    else:
        return False

# SSL port (change port if you need)
port = 465
# gmail server log ins
smtp_server = "smtp.gmail.com"
your_email = "Your@email.com"
password = 'Password'
context = ssl.create_default_context()
people = list()
with open('birthdays.csv') as f:
    reader = csv.reader(f)
    for line in reader:
        name, email, birthday = line[0], line[1], line[2]
        people.append((name, email, birthday))

for p in people:
    name = p[0]
    birthday = p[1]
    email = p[2]
    if check_birthday:
        subject = "Happy birthday"
        message = """Hi {receiver_name},\nI am wishing you a happy birthday!\nLove,\ncompany_name""".format(
            receiver_name=name)
        msg = MIMEMultipart()
        msg['From'] = your_email
        msg['To'] = email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        # connection to server
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(your_email, password)
            txt = msg.as_string()
            server.sendmail(your_email, email, txt)
