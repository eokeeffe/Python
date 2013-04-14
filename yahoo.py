import httplib2
import oauth2
import time
from xml.dom.minidom import parseString



class YahooCrawler():
	OAUTH_CONSUMER_KEY = ""
	OAUTH_CONSUMER_SECRET = ""
	def __init__(self,dbname):
		
	def getLinks(self):
		url = "http://yboss.yahooapis.com/ysearch/web?q=%s&format=xml"%'news'
		consumer = oauth2.Consumer(key=OAUTH_CONSUMER_KEY,secret=OAUTH_CONSUMER_SECRET)
		params = {
		'oauth_version': '1.0',
		'oauth_nonce': oauth2.generate_nonce(),
		'oauth_timestamp': int(time.time()),
		}
		
		oauth_request = oauth2.Request(method='GET', url=url, parameters=params)
		oauth_request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), consumer, None)
		oauth_header=oauth_request.to_header(realm='yahooapis.com')
		
		# Get search results
		http = httplib2.Http()
		resp, content = http.request(url, 'GET', headers=oauth_header)
		print resp
		print "\n"
		print content
		dom = parseString(data)
		list = []
		#retrieve the first xml tag (<tag>data</tag>) that the parser finds with name tagName:
		xmlTag = dom.getElementsByTagName('url')
		#just print the data
		for i in xmlTag:
			tempString =  " ".join(t.nodeValue for t in i.childNodes if t.nodeType == t.TEXT_NODE)
			list.add(tempString)
		return links