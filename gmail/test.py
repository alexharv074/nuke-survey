#!/usr/bin/env python3

import smtplib
import os, sys

def mail():
    gmail_user = 'alexharv074@gmail.com'
    gmail_password = os.environ['NUKE_SURVEY_GMAIL_PASSWORD']

    sent_from = gmail_user
    to = [gmail_user]
    subject = 'Test message'
    body = 'This is a test message'

    email_text = """\
From: {}
To: {}
Subject: {}

{}
""".format(sent_from, ", ".join(to), subject, body)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print('Email sent!')
    except:
        print('Something went wrong...', sys.exc_info())

if __name__ == '__main__':
    mail()

# vim: set ft=python:
