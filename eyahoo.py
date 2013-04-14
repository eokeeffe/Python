#import easy to use xml parser called minidom:
from xml.dom.minidom import parseString
#all these imports are standard on most modern python implementations
 
#open the xml file for reading:
file = open('yahoo.com.txt','r')
#convert to string:
data = file.read()
#close file because we dont need it anymore:
file.close()
#parse the xml you got from the file
dom = parseString(data)
#retrieve the first xml tag (<tag>data</tag>) that the parser finds with name tagName:
xmlTag = dom.getElementsByTagName('url')
#just print the data
for i in xmlTag:
    print " ".join(t.nodeValue for t in i.childNodes if t.nodeType == t.TEXT_NODE)