from os import listdir
import ftplib


def world():
    return ("Hello, World!")

def getlistdir():
    x = listdir('G:/SAN/Lain-lain/xxxWEBGISxxx')
    return x

def loginftp():
    ftp = ftplib.FTP('192.168.34.10')
    ftp.login(user='resultname', passwd='resultpassword')
    files = []
    ftp.dir(files.append())
