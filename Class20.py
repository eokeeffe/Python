"""
	Here is how to interface with the facebook API by using python
	Facebook application details	
	How-to-use-pyfb2012
	"""
from pyfb import Pyfb

#Your APP ID. You Need to register the application on facebook
#http://developers.facebook.com/
#FACEBOOK_APP_ID = 'YOUR_APP_ID'
FACEBOOK_APP_ID = ''

facebook = Pyfb(FACEBOOK_APP_ID)

#Opens a new browser tab instance and authenticates with the facebook API
#It redirects to an url like http://www.facebook.com/connect/login_success.html#access_token=[access_token]&expires_in=0
#facebook.authenticate()

#Copy the [access_token] and enter it below
token = ''
#raw_input("Enter the access_token\n")

#Sets the authentication token
facebook.set_access_token(token)

#Gets info about myself 
me = facebook.get_myself()

print "-" * 40
print "Name: %s" % me.name
print 

print "Friends list:"
for i in facebook.get_friends():
	print i.name