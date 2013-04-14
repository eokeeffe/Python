from geopy import geocoders
import geopy

import sqlite3 as sql
con = sql.connect('locations.db')
def unique_list(l):
    ulist = []
    [ulist.append(x) for x in l if x not in ulist]
    return ulist
def generateCoordinates(f):
	g = geocoders.Google("Key here")
	c = open("coordinates.dat","w")
	fails = 0
	pfails = 0
	for friend in f:
		lat = 0
		lon = 0
		if friend[0] != None:
			location = ''
			location += friend[0]
			location += ","
			location += friend[1]
			try:
				geocodes = g.geocode(location,exactly_one = False)
				location, (lat, lon) = geocodes
				x,y = lon
				print x,y
				c.write(str(x))
				c.write(":")
				c.write(str(y))
				c.write("\n")
			except(geopy.geocoders.google.GQueryError,ValueError):
				#print "Problem with geocode",fails
				fails += 1
	print "Number of geocode fails =",fails
	print "Saving Coordinates"
	c.close()

def createDatabase():
	cur = con.cursor()
	cur.execute("DROP TABLE IF EXISTS location")
	cur.execute("CREATE TABLE location(PRIMARY_KEY city TEXT, Name TEXT)")
	#cur.executemany("INSERT INTO Cars VALUES(?, ?)", cars)

def insertintoDatabase():
	cur = con.cursor()
	f = open("friends.txt")
	list = []
	for friend in f:
		name,id,loc = friend.split(":")
		locs = loc.split(',')
		city = ''
		country = ''
		if len(locs)>1:
			city += locs[0]
			country += locs[1]
		print city,country
		
		cur.execute("INSERT INTO location VALUES(?, ?)", [city,country])
	f.close()

def retrieveLocations():
	cur = con.cursor()
	cur.execute("SELECT DISTINCT * FROM location")
	rows = cur.fetchall()
	return rows

createDatabase()
insertintoDatabase()
list = retrieveLocations()
generateCoordinates(list)
con.close()