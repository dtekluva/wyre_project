# from django.test import TestCase

# # Create your tests here.
import smtplib, ssl

port = 465  # For SSL
password = input("Type your password and press enter: ")

# Create a secure SSL context
context = ssl.create_default_context()

sender_email = "inyangete@gmail.com"
receiver_email = "kboysreel@gmail.com"
user = "omotayo"
message = f"""{user} logged in"""

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("inyangete@gmail.com", password)
    # TODO: Send email here
    server.sendmail(sender_email, receiver_email, message)