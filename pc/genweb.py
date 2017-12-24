###
### genpc.py
###

from collections import namedtuple
import re
import csv
import smtplib

def read_pc(fname):
    pclist = []
    with open(fname, encoding='ISO-8859-1') as csvfile:
        pcreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        headers = next(pcreader)
        for row in pcreader:
           pclist.append({key: value for key, value in zip(headers, row)})

    return pclist

if __name__=="__main__":
    pc = read_pc("finalpc.csv")
    for p in pc:
        name = p["Name"]
        affiliation = p["Affiliation"]
        url = p["URL"]

        if url:
            line = '<div class="pcmember"><a href="' + url +'"><span class="pcname">' + name + '</span></a> <span class="affiliation">' + affiliation + '</span>'
        else:
            line = '<div class="pcmember"><span class="pcname">' + name + '</span> <span class="affiliation">' + affiliation + '</span>'
        line += '</div>'
        
        print (line)
