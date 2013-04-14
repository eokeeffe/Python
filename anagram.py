import urllib
from collections import defaultdict
words = urllib.urlopen('http://www.puzzlers.org/pub/wordlists/unixdict.txt').read().split()
print len(words)
anagram = defaultdict(list) # map sorted chars to anagrams
for word in words:
	anagram[tuple(sorted(word))].append( word )

count = max(len(ana) for ana in anagram.itervalues())
print "count=",count
for ana in anagram.itervalues():
	if len(ana) >= count:
		print ana