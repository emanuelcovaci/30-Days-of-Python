import smtplib
from smtplib import SMTPException
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

host = "smtp.gmail.com"
port = 587
username = "hungrypy@gmail.com"
password = "iamhungry2016"
from_email = username
to_list = ["hungrypy@gmail.com"]

try:
    email_conn = smtplib.SMTP(host, port)
    email_conn.ehlo()
    email_conn.starttls()
    email_conn.login(username, password)

    the_msg = MIMEMultipart("alternative")
    the_msg["Subject"] = "Test"
    the_msg["From"] = from_email
    the_msg["To"] = to_list

    plain_text = "Testing for email with html"
    plain_html = "<html>" \
                 "<body>" \
                 "<h1>Hello</h1></body></html>"

    part_1 = MIMEText(plain_text, 'plain')
    part_2 = MIMEText(plain_html, 'html')

    the_msg.attach(part_1)
    the_msg.attach(part_2)

    email_conn.sendmail(from_email, to_list, the_msg.as_string())
    email_conn.quit()
except SMTPException:
    print "Error send mail!"
