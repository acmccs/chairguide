### 
### sendinvites.py
###

from collections import namedtuple
import time
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

def send_nag(name, email, fromaddr):
    toaddr = email
    replytoaddr = CHAIRS_ADDR
    cc = [CHAIRS_ADDR]
    message_subject = "CCS Reviews Due Friday!"
    with open ("nag.txt", "r") as myfile:
        msg = ''.join([line for line in myfile.readlines()])

    assert msg.find('$NAME') > 0
    msg = msg.replace('$NAME', name, 1)
    assert msg.find('$NAME') == -1

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
    pc = read_pc("noreviews.csv")
    fromaddrs = {'Dave': 'David Evans <evans@virginia.edu>', 
                 'Tal': 'Tal G. Malkin <tal@cs.columbia.edu>', 
                 'Dongyan': 'Dongyan Xu <dxu@cs.purdue.edu>' }

    print ("Read PC list: " + str(len(pc)))
    for p in pc:
        print(p["Name"] + " - " + p["Email"])
        assert '@' in p["Email"] 

    for p in pc:
        send_nag(p["Name"], p["Email"], fromaddrs['Dave'])
        time.sleep(10)
