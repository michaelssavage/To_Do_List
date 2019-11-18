class Node:

	def __init__(self,item):
		self.item = item
		self.next = None
		self.prev = None

class Queue:

	def __init__(self):
		self.head = None
		self.last = None

	def enqueue(self, item): 
		if self.last is None: 
			self.head = Node(item) 
			self.last = self.head 

		else: 
			self.last.next = Node(item) 
			self.last.next.prev = self.last
			self.last = self.last.next

	def dequeue(self):
		if self.head == None: 
			return None

		else:
			temp = self.head.item 
			self.head = self.head.next
			try:
				self.head.prev = None
				return temp
			except:
				return

	def todo(self):
		if self.head:
			return self.head.item
		else:
			return "List is empty."

	def showAll(self):
		if self.head:
			temp = self.head
			show = []
			while temp != None:
				print(temp.item)
				temp = temp.next
		else:
			print("List is empty.")
