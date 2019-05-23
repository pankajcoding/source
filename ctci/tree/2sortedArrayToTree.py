class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None


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
        if mid+1<n:
            node.right=MakeTree(A[mid+1:])
        return node
MakeTree([1,2,3,4,5,6,7])