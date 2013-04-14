"""
	FaceBook friend world Mapping algorithm
"""
from pyfb import Pyfb
import codecs,urllib2
import simplejson

def getHometown(friend):
	try:
		url = 'https://graph.facebook.com/'
		url += friend.id
		auth = ''
		url += auth
		response = urllib2.urlopen(url)
		html = response.read()
		parsed_data = simplejson.loads(html)
		p1 = parsed_data
		name = ''
		name2 = ''
		try:
			hometown = parsed_data['hometown']
			print hometown
			name = hometown['name']
			location = p1['location']
			print location
			name2 = location['name']
			a,b = name2.split(",")
			name += ","
			name += b
		except Exception:
			name = "location not given",Exception
		return name
	except:
		print "URL Failure"
		return ' '

#Your APP ID. You Need to register the application on facebook
#http://developers.facebook.com/
FACEBOOK_APP_ID = ''

facebook = Pyfb(FACEBOOK_APP_ID)

#Opens a new browser tab instance and authenticates with the facebook API
#It redirects to an url like http://www.facebook.com/connect/login_success.html#access_token=[access_token]&expires_in=0
#facebook.authenticate()

#Copy the [access_token] and enter it below
#token = raw_input("Enter the access_token\n")
token = ''
#Sets the authentication token
facebook.set_access_token(token)

#Gets info about myself 
me = facebook.get_myself()

f = codecs.open("friends.txt", "w", "utf-8")

friends = facebook.get_friends()

for friend in friends:
	f.write(friend.name)
	f.write(":")
	f.write(friend.id)
	f.write(":")
	try:
		f.write(getHometown(friend).encode('utf8'))
	except:
		f.write(" ")
	f.write("\n")

f.close()

