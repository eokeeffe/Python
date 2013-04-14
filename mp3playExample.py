import mp3play
import time

filename = r'C:\Users\user\MyMusic\something_good.mp3'
mp3 = mp3play.load(filename)

mp3.play()

# Let it play for up to 30 seconds, then stop it.
while  (mp3.seconds() < 30) :

	name = raw_input("Stop Now?")
	
	if(name == "stop"):
		mp3.stop()
