"""
	Doing stuff on the web 
	So here's the stuff that this file covers
	
	-get all the links of a web page and store them in a
	 file for later viewing
"""

import urllib,urllib2
import htmllib, formatter
from cStringIO import StringIO
from xml.etree import ElementTree as ET

def Read_from_website(name):
	try:
		page = urllib2.urlopen(name)
		f = open("pythonDocs.html","w")
		
		for line in page:
			f.write(line)
		
		print page.info()
		print page.geturl()
	except Exception:
		print "error in opening the site or file to write"
	else:
		print "Written content in the file succesfully"
		f.close()
		
def ParseHTML():
	linkFile = open("linksFile.txt","w")
	myfile = open("pythonDocs.html",'rb')
	html = myfile.read()
	
	dumdum = formatter.DumbWriter(StringIO())
	fermat = formatter.AbstractFormatter(dumdum)
	parsley = htmllib.HTMLParser(fermat)
	parsley.feed(html)
	
	for item in parsley.anchorlist:
		linkFile.write(item)
		linkFile.write("\n")
	
	parsley.close()
	myfile.close()
	linkFile.close()

website = 'http://www.python.org/doc/current/modindex.html'
Read_from_website(website)

ParseHTML()

