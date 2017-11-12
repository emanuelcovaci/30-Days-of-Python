from smtplib import SMTP, SMTPAuthenticationError, SMTPException

host = "smtp.gmail.com"
port = 587
username = "yourusername@gmail.com"
password = "yourpassword"

from_email = username
to_list = [username]

message = "Type here your message!"

connection = SMTP(host, port)
connection.ehlo()
connection.starttls()
try:
    connection.login(username, password)
    connection.sendmail(from_email, to_list, message)
except SMTPAuthenticationError:
    print "Authentication Error \n Username or Password are wrong!"
except:
    print "An error occured!"

connection.quit()
