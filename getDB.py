#!/usr/bin/env python
__author__ = "Dawid Urbanski"
__license__ = "GPL"
__version__ = "1.0.0"

import requests
import json

#curl \
#-X POST \
#-H "Content-Length: 0" \
#-H "Content-Type: application/json" \
#http://m.rozklady.mpk.krakow.pl/Services/data.asmx/GetDate


res = requests.post(
    url="http://m.rozklady.mpk.krakow.pl/Services/data.asmx/GetDate",
    data="",
    headers={
      'Content-Type': 'application/json',
      'Content-Length': '0'})
if not res.ok:
  print "fail to get date!"
  quit()

date=res.json()

print date



#wget http://m.rozklady.mpk.krakow.pl/Data/rozklady-2016-10-19-12-54.zip.zip

date2str=str(date['d']).replace(':','-').replace(' ','-')

url = "http://m.rozklady.mpk.krakow.pl/Data/rozklady-{0}.zip.zip".format(date2str)

print url

##r = requests.get(url, stream=True)
#if not r.ok:
#  print "fail to get DB!"
#  quit()
#
#import zipfile, StringIO
#
#z = zipfile.ZipFile(StringIO.StringIO(r.content))
#print z.extractall()


import urllib2
import os.path

fileName=date2str+".zip"

if not os.path.isfile(fileName):
  response = urllib2.urlopen(url)
  zipcontent= response.read()
  with open(fileName, 'w') as f:
    f.write(zipcontent)

print fileName+" - done"
