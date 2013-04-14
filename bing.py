from BeautifulSoup import BeautifulSoup, SoupStrainer
import mechanize

class BingCrawler():
    def __init__(self,dbname):
        print "Beginning"
        self.nl = None
        self.bl = None
        self.fl = None
        self.conn = sql.connect(user='root',db = dbname, passwd='root', host='127.0.0.1')
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def getLinks(self):
        print "Getting links"
        br = mechanize.Browser()
		br.set_handle_robots(False)
		br.open("http://www.bing.com/search?count=50&q=%s"%'news')
		content = br.response()
		content = content.read()
		soup = BeautifulSoup(content)
		links = soup.findAll("li", { "class" : "sa_wr" })
		for link in links:
			tempString = link.find('a', href=True)['href']
			try:
                self.cursor.execute("INSERT INTO Links(link) VALUES(%s)",(tempString))
                self.conn.commit()
            except():
                print "Probably already exists"
        print "Finished writing news links"

b = Bingcrawler('linkcrawler').getLinks()
del b