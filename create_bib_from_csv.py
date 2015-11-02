# -*- coding: utf-8 -*-
"""
Date: 20151030

Author: Vilja Hulden

A script for converting a JSTOR data for research citations file (.csv) into a BibTex file (.bib) for importation into Zotero (or to any reference manager that understands BibTeX, for that matter).

If you do not wish to include the links to the actual files in the Zotero format, set includefiles below to 0.

This script assumes .txt files named as they come from JSTOR Data for Research.

This script assumes that the csv file has the following fields in the following order:
id, doi, title, author, journaltitle, volume, issue, pubdate, pagerange, publisher, type, reviewed-work, abstract

This should be the case for recently created JSTOR files. The fields doi, publisher, type, reviewed-work, and abstract are ignored.
"""

import re


"""SECTION FOR LOCAL DEFINITIONS -- YOU NEED TO CHANGE THESE"""
# Change workdir and filedir so they reflect where your files reside.
# filedir is where the full-text versions of the articles reside.
workdir = "/Users/miki/work/research/digital/scriptsforgithub/JSTORcsv2bib/"
filedir = "samplefilesfake/" #this is where your full text files would be
includefiles = 1 #set 0 if citations only, no links to files
readfile = "samplecitations.csv"  #this is your JSTOR-provided csv file
writefile = "samplecitations.bib" #this is the file created by the script
"""END SECTION FOR LOCAL DEFINITIONS, CODE FOLLOWS"""



with open(workdir+readfile) as f:
    entriestemp = f.read()
    entries = [line for line in entriestemp.split('\n') if line.strip() != '']


bibentries = []

mycounter = 1
for entry in entries[1:]:
    #get all necessary data
    #note that sometime JSTOR citation files come with the fields in a different
    #...order, in which case you would need to adjust here accordingly.
    entrylist = entry.split('\t')
    thisid = entrylist[0]
    title = entrylist[2]
    authorfield = entrylist[3]
    if authorfield:
        authors = re.sub(',',' and ',authorfield)
    journal = entrylist[4]
    volume = entrylist[5]
    number = entrylist[6] 
    pdate = entrylist[7]
    pyear = int(pdate[:4])
    pmonth = int(pdate[6:7])
    pagesfield = entrylist[8].strip()
    if pagesfield:
        pages = re.search('[0-9-]+',pagesfield,flags=0).group(0)
    #create bibkey; if no author and title, create a key with the help
    # ... of a counter
    if authorfield: #because sometimes it's empty
        bibkeyauthor = re.search('[^ ]+($|,)',authorfield,flags=0).group(0).strip().strip(',')
        bibkey = bibkeyauthor+str(pyear)+"-"+str(pmonth)
    elif title: 
        bibkey = re.match('\s*[^ ]+',title,flags=0).group(0)+str(pyear)+"-"+str(pmonth)
    else:
        bibkey = bibkey + str(mycounter)
        mycounter += 1
    thisidfn = re.sub('/','_',thisid)
    thisidfn = "ocr_"+thisidfn+".txt"
    
    
    #then let's transform into a bibentry
    
    bibentry = "@article{"
    bibentry += bibkey + ",\n\t"
    bibentry += "title = {" + title + "},\n\t"
    bibentry += "author = {" + authors + "},\n\t"
    bibentry += "journal = {" + journal + "},\n\t"
    bibentry += "volume = {" + volume + "},\n\t"
    bibentry += "number = {" + number + "},\n\t"
    bibentry += "year = {" + str(pyear) + "},\n\t"
    bibentry += "month = {" + str(pmonth) +"},\n\t"
    bibentry += "pages = {" + pages + "},\n\t"
    if includefiles > 0:
        bibentry += "file = {" + thisidfn + ":" + workdir + filedir + thisidfn + ":text/plain}\n"
    bibentry += "}"
    
    bibentries.append(bibentry)
    

bibentriestext = "\n\n".join(bibentries)

with open(workdir+writefile, 'w') as f:
    f.write(bibentriestext)
    
    
