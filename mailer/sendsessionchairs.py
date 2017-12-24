### 
### sendpresenters.py
###

from collections import namedtuple
import re
import csv
import smtplib

SMTP_SERVER = 'email-smtp.us-east-1.amazonaws.com'
SMTP_USERNAME = # need to assign this
SMTP_PASSWORD = # need to assign this
CHAIRS_ADDR = # 'ccs2017pcchairs@gmail.com'

def read_pc(fname):
    pclist = []
    with open(fname, encoding='ISO-8859-1') as csvfile:
        pcreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        headers = next(pcreader)
        for row in pcreader:
           pclist.append({key: value for key, value in zip(headers, row)})

    return pclist

def send_invite(name, email, sessionid, fromaddr):
    toaddr = email
    replytoaddr = 'evans@virginia.edu'
    cc = ['evans@virginia.edu']
    message_subject = "ACM CCS 2017 Session Chair Information"
    with open ("sessionchair.txt", "r") as myfile:
        msg = ''.join([line for line in myfile.readlines()])

    assert msg.find('$NAME') > 0
    msg = msg.replace('$NAME', name, 1)
    assert msg.find('$NAME') == -1

    assert msg.find('$SESSIONID') > 0
    msg = msg.replace('$SESSIONID', sessionid[1] + sessionid[0], 1)
    msg = msg.replace('$SESSIONIDURL', 'https://acmccs.github.io/session-' + sessionid, 1)
    assert msg.find('$SESSIONID') == -1

    body = "From: %s\r\n" % fromaddr \
           + "To: %s\r\n" % toaddr \
           + "CC: %s\r\n" % ",".join(cc) \
           + "Reply-To: %s\r\n" % replytoaddr \
           + "Subject: %s\r\n" % message_subject \
           + "\r\n" \
           + msg

    print(body)
    toaddrs = [toaddr] + cc

    smtp_server = SMTP_SERVER
    smtp_username = SMTP_USERNAME
    smtp_password = SMTP_PASSWORD
    smtp_port = '587'
    smtp_do_tls = True

    server = smtplib.SMTP(
        host = smtp_server,
        port = smtp_port,
        timeout = 10
        )
    server.set_debuglevel(10)
    server.starttls()
    server.ehlo()
    server.login(smtp_username, smtp_password)
    server.sendmail(fromaddr, toaddrs, body)
    print (server.quit())

if __name__=="__main__":
    pc = read_pc("sessionchairs.csv")
    fromaddrs = {'Dave': 'David Evans <evans@virginia.edu>' }

    print ("Read PC list: " + str(len(pc)))
    for p in pc:
        print(p["Chair"] + " - " + p["ChairEmail"])
        assert '@' in p["ChairEmail"] 

    for p in pc:
        send_invite(p["Chair"], p["ChairEmail"], p["SessionID"], fromaddrs['Dave'])
