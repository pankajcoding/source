class Node:

	def __init__(self,data,nxt=None):
		self.data=data
		self.next=nxt

class LinkedList(object):
	"""docstring for LInkedList"""
	def __init__(self):
		self.begin=None
		self.end=None

	def push(self,data):
		if self.end==None:
			n1=Node(data,None)
			self.begin=n1
			self.end=n1
		elif self.end!=None:
			n1=Node(data,None)
			self.end.next=n1
			self.end=n1

	def pop(self):
		print(self.count())
		if self.count()==0:
			return None
		elif self.count()==1:
			temp=self.end
			self.head=None
			self.begin=None
			return temp.data

		elif self.count()>1:
			temp=self.begin
			while temp.next!=self.end:
				temp=temp.next
			tempnode=self.end
			self.end=temp
			self.end.next=None
			return tempnode.data

	def unshift(self):
		if self.begin==None:
			return	None
		elif self.count()==1:
			data=self.begin.data
			self.begin=None
			self.end=None
			return data
		else:
			data=self.begin.data
			self.begin=self.begin.next
			return data

	def get(self,index):
		print('index',index)
		if index>self.count()-1:
			return None
		else:
			i=0
			temp=self.begin
			while(i<index):
				temp=temp.next
				i+=1
			print(temp.data)
			return temp.data




	def count(self):
		if self.begin==None:
			return 0
		else:
			length=1
			temp=self.begin
			while temp.next!=None:
				temp=temp.next
				length+=1
			return length












def test_push():
	colors=LinkedList()
	colors.push("Magneta")
	assert colors.count()==1
	colors.push("Alizarian")
	assert colors.count()==2
	colors.push("Alizarian")
	print(colors.count())

def test_pop():
	colors=LinkedList()
	colors.push('Magneta')
	colors.push('Alizarian')
	assert colors.pop()=="Alizarian"
	assert colors.pop()=='Magneta'
	assert colors.pop()==None
	assert colors.pop()==None

def test_unshift():
	colors=LinkedList()
	colors.push("Viridian")
	colors.push("Sap Green")
	colors.push("Van Dyke")
	print( colors.unshift())
	assert colors.unshift() == "Sap Green"
	assert colors.unshift() == "Van Dyke"
	assert colors.unshift() == None
	assert colors.unshift() == None




def test_get():
	colors = LinkedList()
	colors.push("Vermillion")
	assert colors.get(0) == "Vermillion"
	colors.push("Sap Green")
	assert colors.get(0) == "Vermillion"
	assert colors.get(1) == "Sap Green"
	colors.push("Cadmium Yellow Light")
	assert colors.get(0) == "Vermillion"
	assert colors.get(1) == "Sap Green"
	assert colors.get(2) == "Cadmium Yellow Light"
	assert colors.pop() == "Cadmium Yellow Light"
	assert colors.get(0) == "Vermillion"
	assert colors.get(1) == "Sap Green"
	assert colors.get(2) == None
	colors.pop()
	assert colors.get(0) == "Vermillion"
	colors.pop()
	assert colors.get(0) == None


test_get()