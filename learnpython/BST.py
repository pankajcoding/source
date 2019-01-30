# The main usage for a BSTree is to use a tree to organize pairs of key=value nodes in order ahead
# of time, as you insert or delete them

class Node:
	def __init__(self,key,left=None,right=None):
		self.key=key
		self.left=left
		self.right=right

class BST:
	def __init__(self):
		self.root=None

	def get(self,key):
		root=self.root
		while(root):
			if key==root.key:
				return root
			elif key<root.key:
				root=root.left
			elif key>root.key:
				root=root.right
		return None

	def set(self,key):
		if self.root==None:
			self.root=Node(key,None,None)
		else:
			root=self.root
			while(root!=None):
				# print(root.key)
				if key<root.key:
					if root.left==None:
						root.left=Node(key,None,None)
						return
					else:
						root=root.left

				elif key>root.key:
					if root.right==None:
						root.right=Node(key,None,None)
						return
					else:
						root=root.right


	def delete(self,key):
		node=self.get(key)
		print('delete key',node.key)
		if node==None:
			return
		elif node.left==None and node.right==None:
			print('case1')
			del node
			node=None
			return
		elif node.left==None or node.right==None:
			if node.left==None:
				node.key=node.right.key
				node.right=None
			elif node.right==None:
				node.key=node.left.key
				node.left=None
		elif node.left!=None and node.right!=None:
			nodeMin=self.getMin(node.right)
			print('nodeMin',nodeMin.key)
			self.delete(nodeMin.key)
			node.key=nodeMin.key

	def getMin(self,node):
		if node!=None:
			while root:
				if root.left!=None:
					root=root.left
				else:
					return root

	

	def traverse(self,root):
		 if root!=None:
		 	self.traverse(root.left)
		 	print(root.key)
		 	self.traverse(root.right)
		 return
b=BST()
b.set(2)
print('')
b.set(1)
b.traverse(b.root)
print('')

b.set(3)
b.traverse(b.root)
print('')

b.set(10)
b.traverse(b.root)
b.delete(1)
print('')
b.traverse(b.root)