#!/usr/bin/env python3
from ftplib import FTP
host     = "localhost"
user     = "chris"
password = "qwerty"
ftp      = FTP(host,user,password)
ftp.cwd("/home/chris")
files = ftp.nlst()
list_length = len(files)
#conversoin of list
def Convert(files):
        it = iter(files)
        res_dct = dict(zip(range(1,list_length), it))
        return res_dct
print(Convert(files))
