class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None

def levelOrder(root):
    if not root:
        return
    queue=[root,None]
    i=0
    while len(queue)>1:
        node=queue.pop(0)
        if not node:
            queue.append(None)
            print()
        else:
            print(node.data,end="  ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    

def MakeTree(A):
    n=len(A)
    if n==0:
        return None
    elif n==0:
        return Node(A[0])
    else:
        mid=n//2
        node=Node(A[mid])
        node.left=MakeTree(A[0:mid])
        # if mid+1<n:
        node.right=MakeTree(A[mid+1:])
        return node
root=MakeTree([1,2,3,4,5,6,7])
levelOrder(root)