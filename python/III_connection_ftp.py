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
#list of files
#
for key in dico_files:
    print(str(key) + ": " + dico_files[key])
