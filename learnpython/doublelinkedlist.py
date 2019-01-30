class Node:

	def __init(self,data,nxt,prev):
		self.data=data
		self.next=nxt
		self.prev=prev


class DLL:

	def __init(self):
		self.begin=None
		self.end=None

	def push(seld,data):
		if self.end==None:
			n1=Node(data,None,self.end)
			begin=n1
			end=n1
		elif 
			pass

		elif
			prev=end
			n1=None(data,None,end)
			self.end.next=n1
			self.end=self.end.next








def test_push():
	colors=LinkedList()
	colors.push("Magneta")
	assert colors.count()==1
	colors.push("Alizarian")
	assert colors.count()==2
	colors.push("Alizarian")
	print(colors.count())
