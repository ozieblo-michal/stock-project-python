# download .zip file with raw data

import urllib.request
class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.69 Safari/537.36"
urllib._urlopener = AppURLopener()
urllib._urlopener.retrieve("https://static.stooq.pl/db/h/d_pl_txt.zip",
                           "d_pl_txt.zip")

# unzip only needed files

import zipfile

archive = zipfile.ZipFile('d_pl_txt.zip')

for file in archive.namelist():
    if file.startswith('data/daily/pl/wse stocks/'):
        archive.extract(file,
                        '/Users/michalozieblo/Desktop/wse-dash/wseStocks')

# delete used .zip file

import os

myfile = "d_pl_txt.zip"

try:
    os.remove(myfile)
except OSError as e:
    print ("Error: %s - %s." % (e.filename, e.strerror))