"""
	ADT's in python
	
	This module will help learn the basic
	use of some ADTs in python
	
	functions and documenation are there to assist in
	how they work
"""

class LinkedList:
	def __init__(self):
		"""
			Constructor with no arguements
		"""
		self.count = 0
		self.head = Node(None)
		self.tail = Node(None)
	
	def size(self):
		return self.count
	
	def insertAfter(self,node,element):
		temp = Node(element)
		temp.prev = node
		temp.next = node.next
		if(node.next == None):
			self.tail = temp
		else:
			node.next.prev = temp
		node.next = temp

	def insertBefore(self,node,element):
		temp = Node(element)
		temp.prev = node.prev
		temp.next = node
		if(node.prev == None):
			self.head = temp
		else:
			node.prev.next = temp
		node.prev = node
	
	def insertFirst(self,element):
		temp = Node(element)
		if(self.head.element == None):
			self.head= temp
			self.tail= temp
			temp.prev = None
			temp.next = None
		else:
			self.insertBefore(self.head,temp)

	def insertLast(self,element):
		temp = Node(element)
		if(self.tail.element == None):
			self.insertFirst(temp)
		else:
			self.insertAfter(self.tail,temp)

	def remove(self,element):
		temp = Node(element)
		
		if(str(temp.element) == str(self.head.element)):
			self.head = self.head.next
			self.head.prev = None
			self.count -= 1
			return element
		elif(str(temp.element) == str(self.tail.element)):
			self.tail = self.tail.prev
			if(self.tail.next != None):
				self.tail.next = None
			self.count -= 1
			return element
		else:
			current = self.head
			while current:
				if(str(current.element) == str(temp.element)):
					print "Found a Match"
					break
				print current.element == temp
				current = current.next 
			
			if(current == None):
				return None
			if(current.next != None):
				current.next.prev = current.next
			if(current.prev != None):
				current.prev.next = current.prev
			self.count -= 1
			return element

	def Next(self,node):
		return node.next
	
	def Prev(self,node):
		return node.prev
	
	def __str__(self):
		string = ""
		node = self.head
		while node:
			string = string + str(node.element) +" "
			node = self.Next(node)
		return string

class EmptyLinkedList(Exception):
	def __init__(self,value):
		self.value = value
	def __str__(self):
		return repr(self.value)

class Node:
	"""
		Inner Class that acts as the Node object
		Node contains an element , next and previous references
	"""
	def __init__(self,element):
		self.element = element
		self.next = None
		self.prev = None
	def __str__(self): 
		return str(self.element)

ll = LinkedList()
ll.insertFirst(1)
ll.insertFirst(2)
ll.insertLast(3)
ll.insertLast(4)
removed = ll.remove(2)
print "removed =",removed
print "from",ll