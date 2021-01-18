#!/usr/bin/env python3
from ftplib import FTP
host     = "localhost"
user     = "chris"
password = "qwerty"
ftp      = FTP(host,user,password)
ftp.cwd("/home/chris")
ftp.retrlines('LIST')
