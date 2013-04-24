import time
import pylast
import re

from md5 import md5

user_name = ''
user_password = ''
api_key = ''
api_secret = ''
top_tracks_file = open('top_tracks_wordle.txt', 'w')

# to make the output more interesting for wordle viz.
# run against all periods. if you just want one period,
# delete the others from this list
time_periods = ['PERIOD_12MONTHS', 'PERIOD_6MONTHS', 'PERIOD_3MONTHS', 'PERIOD_OVERALL']
# time_periods = ['PERIOD_OVERALL']
#####
## shouldn't have to edit anything below here
#####
md5_user_password = md5(user_password).hexdigest()
#log onto the network
network = pylast.LastFMNetwork(api_key = API_KEY, api_secret = 
    API_SECRET, username = username, password_hash = password_hash)
sg = pylast.SessionKeyGenerator(network)
session_key = sg.get_session_key(user_name, md5_user_password)

user = pylast.User(user_name, api_key, api_secret, session_key)
top_tracks = []
for time_period in time_periods:
    # by default pylast returns a seq in the format:
    #  "Item: Andrew Bird - Fake Palindromes, Weight: 33"
    tracks = user.get_top_tracks(period=time_period)

    # regex that tries to pull out only the track name (
    # for the ex. above "Fake Palindromes"
    p = re.compile('.*[\s]-[\s](.*), Weight: [\d]+')

    for track in tracks:
        m = p.match(str(track))
        track = m.groups()[0]
        top_tracks.append(track)
    # be nice to last.fm's servers
    time.sleep(5)

top_tracks = "\n".join(top_tracks)
top_tracks_file.write(top_tracks)
top_tracks_file.close()
