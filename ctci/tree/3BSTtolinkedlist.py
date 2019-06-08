class LLNode:
    def __init__(self,data):
        self.data=data
        self.next=None

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def linked_list_insert(head,data):
    newlnode=LLNode(data)
    if not head:
        head=newlnode
        return head
    else:
        temp=head
        while temp.next:
            temp=temp.next
            temp=newlnode
            return temp
def BT_to_linkedlist(root):
    if not root:
        return
    currentlevel=0
    linkedlists=[]
    queue=[root,None]
    while len(queue)>1:
        node =queue.pop(0)
        if not node:
            currentlevel+=1
            linkedlists.append()
            queue.append(None)
        else:
            linked_list_insert(linkedlists[currentlevel],node.data)
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)