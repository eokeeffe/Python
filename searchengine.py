from pysqlite2 import dbapi2 as sqlite
import urllib2
from BeautifulSoup import *
from urlparse import urljoin
# Create a list of words to ignore
ignorewords = set(['the','of','to','and','a','in','is','it'])

class crawler:
	# Initialize the crawler with the name of the database
	def __init__(self,dbname):
		self.con = sqlite.connect(dbname)
		
	def __del__(self):
		self.con.close()

	def dbcommit(self):
		self.con.commit()

	# Auxiliary Function for getting an entry id and adding
	# it if it's not present
	def getentry(self,table,field,value,createnew=True):
		cur = self.con.execute(
		"select rowid from %s where %s='%s'" % (table,field,value))
		
		res = cur.fetchone()
		if res == None:
			cur = self.con.execute(
			"insert into %s (%s) values ('%s')" % (table,field,value))
			return cur.lastrowid
		else:
			return res[0]
		
	# Index an individual page
	def addtoindex(self,url,soup):
		if self.isindexed(url): return
		print 'Indexing '+url
		
		# Get the individual words
		text = self.gettextonly(soup)
		words = self.seperatewords(text)
		
		# Get the URL id
		urlid = self.getentryid('urllist','url',url)
		
		# Link each word to this url
		for i in range(len(words)):
			word = words[i]
			if word in ignorewords: continue
			wordid = self.getentryid('wordlist','word',word)
			self.con.execute("insert into wordlocation(urlid,wordid,location) \
			values (%d%d%d)" % (urlid,wordid,i)

	# Extract the text from an HTML page (no tags)
	def gettextonly(self,soup):
		v = soup.string
		if v == None:
			c = soup.contents
			resulttext = ''
			for t in c:
				subtext = self.gettextonly(t)
				resulttext += subtext+'\n'
			return resulttext
		else:
			return v.strip()
		
	# Seperate the words by any whitespace character
	def seperatewords(self,text):
		splitter = re.compile('\\W*')
		return [s.lower() for s in splitter.split(text) if s != '']
		
	# Return true if this url is already indexed
	def isindexed(self,url):
		u = self.con.execute \
		("select rowid from urllist where url='%s'" % url).fetchone()
		if u != None:
			# Check if it has actually been crawled
			v = self.con.execute('select * from wordlocation where urlid=%d' % u[0]).fetchone()
			if v != None: return True
		return False
	
	# Add a link between two pages
	def addlinkref(self,urlFrom,urlTo,linkText):
		words = self.seperateWords(linktext)
		fromid = self.getentryid('urllist','url',urlFrom)
		toid = self.getentryid('urllist','url',urlTo)
		if fromid == toid: return
		cur = self.con.execute("insert into link(fromid,toid) values (%d%d)" % (fromid,toid))
		linkid = cur.lastrowid
		for word in words:
			if word in ignorewords: continue
			wordid = self.getentryid('wordlist','word',word)
			self.con.execute("insert into linkwords(linkid,wordid) values (%d%d)" % (linkid,wordid))
			
	# Starting with a list of pages , do a breadth
	# first search to the given depth, indexing pages
	# as we go
	def crawl(self,pages,depth=2):
		pass
		
	# Create the database tables
	def createindextables(self):
		try:
			self.con.execute('create table urllist(url)')
			self.con.execute('create table wordlist(word)')
			self.con.execute('create table wordlocation(urlid,wordid,location)')
			self.con.execute('create table link(fromid integer,toid integer)')
			self.con.execute('create table linkwords(wordid,linkid)')
			self.con.execute('create index wordidx on wordlist(word)')
			self.con.execute('create index urlidx on urllist(url)')
			self.con.execute('create index wordurlidx on wordlocation(wordid)')
			self.con.execute('create index urltoidx on link(toid)')
			self.con.execute('create index urlfromidx on link(fromid)')
		except:
			print "DB has all tables and links needed"
		finally:
			self.dbcommit()
		
	def crawl(self,pages,depth=2):
		for i in range(depth):
			newpages = set()
			for page in pages:
				try:
					c = urllib2.urlopen(page)
				except:
					print "Could not open %s" % page
					continue
				soup = BeautifulSoup(c.read())
				self.addtoindex(page,soup)
				
				links = soup('a')
				for link in links:
					if ('href' in dict(link.attrs)):
						url = urljoin(page,link['href'])
						if url.find("'") != -1: continue
						url = url.split('#')[0] # remove location portion
						if url[0:4] == 'http' and not self.isindexed(url):
							newpages.add(url)
						linkText = self.gettextonly(link)
						self.addlinkref(page,url,linkText)
				self.dbcommit()
			pages = newpages