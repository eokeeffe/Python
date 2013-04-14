from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
# lon_0 is central longitude of projection.
# resolution = 'c' means use crude resolution coastlines.

def drawMap(lons,lats):
	# make sure the value of resolution is a lowercase L,
	#  for 'low', not a numeral 1
	map = Basemap(projection='robin', lat_0=0, lon_0=50,
              resolution='h', area_thresh=1000.0)
	map.drawcoastlines()
	map.drawcountries()
	map.fillcontinents(color='coral')
	map.drawmapboundary()
	
	map.drawmeridians(np.arange(0, 360, 30))
	map.drawparallels(np.arange(-90, 90, 30))
	
	# draw parallels and meridians.
	myx,myy = map(53.4508, -6.1544)
	x,y = map(lats,lons)
	#map.drawgreatcircle(myx,myy,x,y,linewidth=3,color='b')
	map.plot(x, y, 'ro')
	plt.title("FriendMap")
	#map.bluemarble()
	plt.show()

def getpoints(file):
	list = []
	list2 = []
	f = open(file)
	for point in f:
		a = point.split(":")
		a[1] = a[1].rstrip()
		#print a
		list.append(float(a[0]))
		list2.append(float(a[1]))
	f.close()
	return list,list2
	
list,list2 = getpoints("coordinates.dat")
drawMap(list,list2)