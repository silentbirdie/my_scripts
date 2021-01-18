#!/usr/bin/env python3
from ftplib import FTP
host     = "localhost"
user     = "chris"
password = "qwerty"
ftp      = FTP(host,user,password)
ftp.cwd("/home/chris")
files = ftp.nlst()   # attention files avec s ( car file est un mot reservé )
print (files)
print(type(files))
