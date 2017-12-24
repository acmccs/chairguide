###
### process.py
###

from collections import namedtuple
import re
import csv

PCMember = namedtuple('PCMember', ['affiliations', 'conferences'])

def last_name(name):
    return name.split(' ')[-1]

def first_names(name):
    return name.split(' ')[:-1]

### Reads .csv files into PC member dictionary
def read_pc(sname, confname, pcdict):
    with open(sname) as csvfile:
        pcreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in pcreader:
            # print("Read: " + str(row))
            if len(row) < 2:
                print("Bad row: " + str(row))
                assert False

            name = row[0]
            affiliation = row[1]
            if len(row) >= 3:
                country = row[2]

            if name in pcdict:
                closest = name
            else:
                # check for ambiguous names
                lastname = last_name(name)
                # print ("Lastname: " + lastname)
                firstnames = first_names(name)
                closest = None
                if '.' in firstnames[0]:
                    for pcname in pcdict:
                        plast = last_name(pcname)
                        if lastname == plast:
                            pcfirst = first_names(pcname)
                            if firstnames[0][0] == pcfirst[0][0]:
                                # print ("Last name match: " + lastname + " =? " + pcname)
                                # assert (not closest)
                                closest = pcname
                            # print ("Not a match: " + lastname + " / " + pcname)

            if closest:
                if not affiliation in pcdict[closest].affiliations:
                    pcdict[closest].affiliations.append(affiliation)

                pcdict[closest].conferences.append(confname)
            else:
                pcdict[name] = PCMember(affiliations = [affiliation], 
                                        conferences = [confname])

def pcsize(pcdict, conf):
    count = 0
    for person, precord in pcdict.items():
        if conf in precord.conferences:
            count += 1
    return count

def overlap(pcdict, confs):
    result = []
    count = 0
    lastconf = confs[-1]
    for person, precord in pcdict.items():
        if lastconf in precord.conferences:
            count += 1

        inall = True
        for conf in confs:
            if not conf in precord.conferences:
                inall = False
                break

        if inall:
            result.append(person)

    # print ("Overlap: " + str(len(result)) + " out of " + str(count) + " / " + str(len(result)/count))
    return result

def show_overlap(pcdict, confs):
    alloverlap = overlap(pcdict, confs)
    print("Overlap " + str(confs) + ": (" + str(len(alloverlap)) + ")\n\t" + str(alloverlap))

if __name__=="__main__":
    def show_conference_overlaps(conferences):
        for i in range(len(conferences) - 1):
            pccount = pcsize(pcdict, conferences[i + 1])
            olap = len(overlap(pcdict, [conferences[i], conferences[i + 1]]))
            print ("Overlap " + conferences[i] + " => " + conferences[i + 1] + ": " + str(olap) + " out of " + str(pccount) + " (" + str(olap / pccount) + ")")

    def check_names():
        prevlast = None
        print("Close names: ")
        for person in sorted(pcdict, key = lambda e: last_name(e) + " " + ' '.join(first_names(e))):
            if prevlast and last_name(prevlast)[:6] == last_name(person)[:6] and len(last_name(person)) > 3:
                print (prevlast + ", " 
                       + ';'.join(pcdict[prevlast].affiliations) + ", " 
                       + ', '.join(pcdict[prevlast].conferences))
                
                print (person + ", " 
                       + ';'.join(pcdict[person].affiliations) + ", " 
                       + ', '.join(pcdict[person].conferences))
                print ("========")
            prevlast = person

    def output_all(fname):
        with open(fname, 'w', newline='') as csvfile:
            fwriter = csv.writer(csvfile, delimiter=',')
            for person in sorted(pcdict, key = lambda e: last_name(e) + " " + ' '.join(first_names(e))):
                fwriter.writerow([person, 
                                  ';'.join(pcdict[person].affiliations)]
                                 + [len(pcdict[person].conferences)]
                                 + [len([conf 
                                        for conf in pcdict[person].conferences
                                         if re.search("201[4567]", conf)])]
                                 + [len([conf 
                                        for conf in pcdict[person].conferences
                                         if re.search("CCS 201[4567]", conf)])]
                                 + pcdict[person].conferences)

    pcdict = {}
    read_pc("data/ccs2017.csv", "CCS 2017", pcdict)
    read_pc("data/ccs2016.csv", "CCS 2016", pcdict)
    read_pc("data/ccs2015.csv", "CCS 2015", pcdict)
    read_pc("data/ccs2014.csv", "CCS 2014", pcdict)
    read_pc("data/ccs2013.csv", "CCS 2013", pcdict)
    read_pc("data/ccs2012.csv", "CCS 2012", pcdict)
    read_pc("data/ccs2011.csv", "CCS 2011", pcdict)
    read_pc("data/ccs2010.csv", "CCS 2010", pcdict)
    read_pc("data/ccs2009.csv", "CCS 2009", pcdict)
    read_pc("data/ccs2008.csv", "CCS 2008", pcdict)
    read_pc("data/ccs2007.csv", "CCS 2007", pcdict)
    read_pc("data/ccs2006.csv", "CCS 2006", pcdict)
    read_pc("data/ccs2005.csv", "CCS 2005", pcdict)
    read_pc("data/ccs2004.csv", "CCS 2004", pcdict)
    # PC lists for CCS 2003 and (presumably) earlier not on web

    read_pc("data/oakland2017.csv", "Oakland 2017", pcdict)
    read_pc("data/oakland2016.csv", "Oakland 2016", pcdict)
    read_pc("data/oakland2015.csv", "Oakland 2015", pcdict)
    read_pc("data/oakland2014.csv", "Oakland 2014", pcdict)
    read_pc("data/oakland2013.csv", "Oakland 2013", pcdict)
    read_pc("data/oakland2012.csv", "Oakland 2012", pcdict)
    read_pc("data/oakland2011.csv", "Oakland 2011", pcdict)
    read_pc("data/oakland2010.csv", "Oakland 2010", pcdict)
    read_pc("data/oakland2009.csv", "Oakland 2009", pcdict)
    read_pc("data/oakland2008.csv", "Oakland 2008", pcdict)
    read_pc("data/oakland2007.csv", "Oakland 2007", pcdict)
    read_pc("data/oakland2006.csv", "Oakland 2006", pcdict)
    read_pc("data/oakland2005.csv", "Oakland 2005", pcdict)
    read_pc("data/oakland2004.csv", "Oakland 2004", pcdict)

    read_pc("data/usenix2017.csv", "USENIX 2017", pcdict)
    read_pc("data/usenix2016.csv", "USENIX 2016", pcdict)
    read_pc("data/usenix2015.csv", "USENIX 2015", pcdict)
    read_pc("data/usenix2014.csv", "USENIX 2014", pcdict)
    read_pc("data/usenix2013.csv", "USENIX 2013", pcdict)
    read_pc("data/usenix2012.csv", "USENIX 2012", pcdict)
    read_pc("data/usenix2011.csv", "USENIX 2011", pcdict)
    read_pc("data/usenix2010.csv", "USENIX 2010", pcdict)
    read_pc("data/usenix2009.csv", "USENIX 2009", pcdict)
    read_pc("data/usenix2008.csv", "USENIX 2008", pcdict)
    read_pc("data/usenix2007.csv", "USENIX 2007", pcdict)
    read_pc("data/usenix2006.csv", "USENIX 2006", pcdict)
    read_pc("data/usenix2005.csv", "USENIX 2005", pcdict)
    read_pc("data/usenix2004.csv", "USENIX 2004", pcdict)

    read_pc("data/ndss2017.csv", "NDSS 2017", pcdict)
    read_pc("data/ndss2016.csv", "NDSS 2016", pcdict)
    read_pc("data/ndss2015.csv", "NDSS 2015", pcdict)
    read_pc("data/ndss2014.csv", "NDSS 2014", pcdict)
    read_pc("data/ndss2013.csv", "NDSS 2013", pcdict)
    read_pc("data/ndss2012.csv", "NDSS 2012", pcdict)
    read_pc("data/ndss2011.csv", "NDSS 2011", pcdict)
    read_pc("data/ndss2010.csv", "NDSS 2010", pcdict)
    read_pc("data/ndss2009.csv", "NDSS 2009", pcdict)
    read_pc("data/ndss2008.csv", "NDSS 2008", pcdict)
    read_pc("data/ndss2007.csv", "NDSS 2007", pcdict)
    read_pc("data/ndss2006.csv", "NDSS 2006", pcdict)
    read_pc("data/ndss2005.csv", "NDSS 2005", pcdict)
    read_pc("data/ndss2004.csv", "NDSS 2004", pcdict)

    # read_pc("data/crypto2016.csv", "CRYPTO 2016", pcdict)

    output_all("all.csv")

    print ("Total People: " + str(len(pcdict)))

    numslots = 0
    for person, record in pcdict.items():
        numslots += len(record.conferences)

    print ("Total Slots:  " + str(numslots))

    print ("Sorted by Membership: ")

    counts = []
    lastcount = 0
    for person in sorted(pcdict, key = lambda e: len(pcdict[e].conferences)):
        count = len(pcdict[person].conferences)
        if count == lastcount:
            counts[-1] += 1
        else:
            counts.append(1)
            lastcount = count
        print (person + " (" + str(count) + "): " + str(pcdict[person].conferences))

    print("Counts: " + str(counts))

    #print("CCS 2015 => CCS 2016 overlap:")
    #print(str(overlap(pcdict, ['CCS 2015', 'CCS 2016'])))
    #print("CCS 2014 => CCS 2016 overlap:")
    #print(str(overlap(pcdict, ['CCS 2014', 'CCS 2016'])))
    #print("CCS 2014 => CCS 2015 => CCS 2016 overlap:")
    #print(str(overlap(pcdict, ['CCS 2014', 'CCS 2015', 'CCS 2016'])))
    #print("CCS 2013 => CCS 2014 => CCS 2014 => CCS 2016 overlap:")
    #print(str(overlap(pcdict, ['CCS 2013', 'CCS 2014', 'CCS 2015', 'CCS 2016'])))
    #print("CCS 2012 ==> CCS 2016 overlap:")
    #print(str(overlap(pcdict, ['CCS 2012', 'CCS 2013', 'CCS 2014', 'CCS 2015', 'CCS 2016'])))

    ccs_conferences = ['CCS 2004', 'CCS 2005', 'CCS 2006', 'CCS 2007', 'CCS 2008', 'CCS 2009', 'CCS 2010', 'CCS 2011', 'CCS 2012', 'CCS 2013', 'CCS 2014', 'CCS 2015', 'CCS 2016', 'CCS 2017']

    show_conference_overlaps(ccs_conferences)

    usenix_conferences = ['USENIX 2004', 'USENIX 2005', 'USENIX 2006', 'USENIX 2007', 'USENIX 2008', 'USENIX 2009', 'USENIX 2010', 'USENIX 2011', 'USENIX 2012', 'USENIX 2013', 'USENIX 2014', 'USENIX 2015', 'USENIX 2016', 'USENIX 2017']

    show_conference_overlaps(usenix_conferences)

    #show_overlap(pcdict, ['Oakland 2016', 'CCS 2016'])
    #show_overlap(pcdict, ['USENIX 2016', 'CCS 2016'])
    #show_overlap(pcdict, ['Oakland 2016', 'USENIX 2016', 'CCS 2016'])
    #show_overlap(pcdict, ['Oakland 2017', 'CCS 2016'])
    #show_overlap(pcdict, ['Oakland 2017', 'USENIX 2016', 'CCS 2016'])
    #show_overlap(pcdict, ['Oakland 2017', 'USENIX 2016'])
