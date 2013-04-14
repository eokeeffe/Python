"""
	Parse an xml file with book names and
	put them into dictionaries
"""
import pprint
 
import xml.dom.minidom
from xml.dom.minidom import Node
 
doc = xml.dom.minidom.parse("book.xml")
 
mapping = {}
 
for node in doc.getElementsByTagName("book"):
  isbn = node.getAttribute("isbn")
  L = node.getElementsByTagName("title")
  for node2 in L:
    title = ""
    for node3 in node2.childNodes:
      if node3.nodeType == Node.TEXT_NODE:
        title += node3.data
    mapping[isbn] = title
 
# mapping now has the same value as in the SAX example:
pprint.pprint(mapping)