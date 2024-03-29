#############################
#program spider.py
#author: aahz
#version: 1.1
#date: June 2006
#description: start on command line with URL arguement
#Finds pages within a web site
#############################

"""
	This is a very simple web crawler application
	all that has to be done is giving it the website to go
	through and return a list of all links on the page
	
	Sample use is : python Class4.py http://pythonfood.com/spider-test/
"""

#Import modules to reuse the wheels
import sys
import urllib2 as u
import urlparse
import htmllib,formatter
from cStringIO import StringIO

def log_stdout(msg):
	"""Print msg to the screen."""
	print msg
	
def get_page(url, log):
	"""Retrieve URL and return contents, log errors"""
	try:
		page = u.urlopen(url)
	except u.URLError:
		log("Error retrieving: " + url)
		return ''
	body = page.read()
	page.close()
	return body
	
def find_links(html):
	"""Return a list of links in html"""
	# We're using the parser just to get the HREFs
	writer = formatter.DumbWriter(StringIO())
	f = formatter.AbstractFormatter(writer)
	parser = htmllib.HTMLParser(f)
	parser.feed(html)
	parser.close()
	return parser.anchorlist
	
class Spider:
	"""
		The heart of this program , find all the links within
		a web site
		
		run() contains the main loop
		process_page() retrieves each page and finds the links
	"""
	def __init__(self,startURL,log=None):
		# This method sets initial values
		self.URLs = set()
		self.URLs.add(startURL)
		self.include = startURL
		self._links_to_process = [startURL]
		if log is None:
			#Use log_stdout function if no log provided
			self.log = log_stdout
		else:
			self.log = log
			
	def run(self):
		#Processes list of URLs one at a time
		while self._links_to_process:
			url = self._links_to_process.pop()
			self.log("Retrieving: " + url)
			self.process_page(url)
			
	def url_in_site(self,link):
		# Checks whether the link starts with the base URL
		return link.startswith(self.include)
		
	def process_page(self,url):
		# Retrieves page and finds links in it
		html = get_page(url,self.log)
		for link in find_links(html):
			# Handles relative links
			link = urlparse.urljoin(url,link)
			self.log("Checking: " + link)
			# Make sure this is a new link within the current site
			if link not in self.URLs and self.url_in_site(link):
				self.URLs.add(link)
				self._links_to_process.append(link)
				
if __name__ == '__main__':
	# This code runs when script is started from command line
	startURL = sys.argv[1]
	spider = Spider(startURL)
	spider.run()
	for URL in sorted(spider.URLs):
		print URL