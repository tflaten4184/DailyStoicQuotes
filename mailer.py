# This script constructs the email by caller mapper, then sends to all subscribers.

import os # Use for environment variable for email password
from email.message import EmailMessage
import ssl
import smtplib
import mapper


def send_mail(content):

    with open("subscribersList.txt") as subscribersFile:
        subscribersList = [line.strip() for line in subscribersFile]

        for receiver in subscribersList:
            email_sender = os.environ['botEmail']
            email_password = os.environ['apikey']
            email_receiver = receiver

            subject = "Daily Stoic Quote"
            body = content

            em = EmailMessage()
            em["From"] = email_sender
            em["To"] = email_receiver
            em["Subject"] = subject
            em.set_content(body)

            context = ssl.create_default_context()

            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender, email_receiver, em.as_string())

if __name__ == "__main__":

    # Logfile for debugging .env variables
    # with open("logfile.txt", "w") as logfile:
    #     logfile.write(os.environ['botEmail'])
    #     logfile.write(os.environ['apikey'])
    #######

    quotes_map = mapper.get_quotes_map()
    # print("main")
    # print(get_today_quote(quotes_map))
    content = mapper.get_today_quote(quotes_map)
    content += f"""\n-----------------------\n\nIf you'd like to be removed from this email list, please reach out to {os.environ['maintainerEmail']} to request removal."""
    print(content)
    send_mail(content)