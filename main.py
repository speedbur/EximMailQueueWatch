import os
import smtplib
import sys
from email.mime.text import MIMEText
import settings


def check():
    command_line_result = os.popen(settings.EXIM_PATH + " " + settings.EXIM_MAILQUEUE_SIZE_PARAM)
    check_mail_queue_size(command_line_result)


def check_mail_queue_size(command_line_result):
    count = int(command_line_result)
    if count >= settings.EXIM_WARN_QUEUE_SIZE:
        raise Exception("mail queue size is " + str(count) + " and exceeds maximum value of " + str(
            settings.EXIM_MAILQUEUE_SIZE_PARAM))


def main():
    try:
        check()
    except Exception, e:
        msg = MIMEText(e.__str__())
        msg['Subject'] = "Exim error " + settings.HOSTNAME
        msg['From'] = settings.FROM_MAIL
        msg['To'] = settings.TO_MAIL
        s = smtplib.SMTP(settings.SMTP_ADDRESS)
        s.sendmail(msg['From'], [msg['To']], msg.as_string())
        s.quit()
        sys.exit(1)

if __name__ == "__main__":
    main()

