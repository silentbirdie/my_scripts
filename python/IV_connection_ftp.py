#!/usr/bin/env python3
from ftplib import FTP
host     = "localhost"
user     = "chris"
password = "qwerty"
ftp      = FTP(host,user,password)
#
#current working directory of my ftp
#
ftp.cwd("/home/chris")
#
#list of files
#
files = ftp.nlst()
#
#list length to enter as key values
#
list_length = len(files)
#conversoin of list
def Convert(files):
        it = iter(files)
        res_dct = dict(zip(range(1,list_length), it))
        return res_dct
dico_files = Convert(files)
#
#list of files loop
#


for key in dico_files:
        file_list = print(str(key) + ": " + dico_files[key])






#
# menu
#

selection = str(input("what file to choose?"))
localfile = open(selection, 'wb')
ftp.retrbinary('RETR ' + selection, localfile.write, 1024)
