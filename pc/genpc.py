###
### genpc.py
###

from collections import namedtuple
import re
import csv
import smtplib

def read_pc(fname):
    pclist = []
    with open(fname) as csvfile: # , encoding='ISO-8859-1') as csvfile:
        pcreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        headers = next(pcreader)
        for row in pcreader:
           pclist.append({key: value for key, value in zip(headers, row)})

    return pclist

if __name__=="__main__":
    pc = read_pc("finalpc.csv")
    line = ""
    maxline = 136
    lines = 0
    skipping = True
    for p in pc:
        name = p["Name"]
        nameu = name.decode("iso-8859-1")
        nameuc = nameu.encode("UTF-8")
        next = nameuc + " (" + p["Affiliation"].decode("iso-8859-1").encode("UTF-8") + ")"

        if len(next) + len(line) + 3 > maxline:
            print (line)
            lines += 1
            line = next
        else:
            if line:
                line = line + " " + u"\u2022" + " " + next.decode("UTF-8")
            else:
                line = next
    if line:
        print (line)
        lines += 1
    print ("Lines: " + str(lines))
