import pylast

#My current information for the lastfm site
api_key = '067991349b7ca99ac97dee9f1af60580'
api_secret = '4001bfb74d27d249047005d5eab4befd'
#user info
username = 'EJ0K' 
password_hash = pylast.md5("saffey1") 
#connecting api works for majority of functions
network = pylast.get_lastfm_network(api_key,api_secret,username,password_hash)
user = pylast.User(username, network)

def UserShouts(username,limit):
	shouts = []
	shouts = network.get_user(username).get_shouts(limit=limit)
	#for i in shouts:
	#	print i
	return shouts

def UserTopTags(username,limit):
	tags = []
	tags = network.get_user(username).get_top_tags(limit=limit)
	#for i in tags:
	#	print i
	return tags

def UserTopArtists():
	top_artists = []
	top_artists = network.get_user(username).get_top_artists()
	#for i in top_artists:
	#	print i
	return top_artists
	
def UserTopAlbums():
	top_albums = []
	top_albums = network.get_user(username).get_top_albums()
	#for i in top_albums:
	#	print i
	return top_albums

def UserGetLovedTracks(username,limit):
	loved_tracks = []
	loved_tracks = network.get_user(username).get_loved_tracks(limit=limit)
	#for i in loved_tracks:
	#	print i
	return loved_tracks

def UserInfo():
	name = network.get_user(username)+"|"
	name += network.get_user(username).get_gender()+"|"
	name += network.get_user(username).get_id()
	return name

def getFriends():
	return network.get_user(username).get_friends()
		
def UserCurrentlyPlaying():
	return network.get_user(username).get_now_playing()

def printUserNeighbours(neighbours):
	for i in neighbours:
		print i
	return 0

def getNeighbours(username,limit):
	return network.get_user(username).get_neighbours(limit=limit)
	
def SaveUserNeighbours(username,limit):
	name = username+".txt"
	fh = open(name,"w")
	neighbours = []
	neighbours = getNeighbours(username,limit)
	for i in neighbours:
		print >>fh, str(i)
	fh.close()
	return name
	
def getAlbumTracks(name,album_name,limit):
	album =  pylast.Album(name,album_name,network)
	songs = []
	songs = album.get_tracks()
	#for i in songs:
		#print i
	return songs

def getArtist_Top_Albums(name):
	f = open(name+".txt",'w')
	artist = pylast.Artist(name,network)
	top_albums = getArtistAlbums(artist)
	var = 0
	while var < len(top_albums):
		print >>f, top_albums[var][0]
		var += 1
	f.close()
	list = extractInformation(name+".txt")
	#for item in list:
	#	print item
	return list

def getArtistAlbums(artist):
	top_albums = []
	top_albums = artist.get_top_albums()
	return top_albums
	
def extractInformation(filename):
	list = []
	f = open(filename,'r')
	while f.readline():
		list.append(f.readline())
	f.close()
	return list

mylist = SaveUserNeighbours("EJ0K",50)

#print extractInformation(mylist)
#printUserNeighbours( extractInformation(mylist) )