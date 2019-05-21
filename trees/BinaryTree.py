class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def preorder_traversal(root):
    if not root:
        return
    else:
        print(root.data,end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)
def preorder_traversal_iterative(root):
    if not root:
        return
    stack=[]
    stack.append(root)
    while stack:
        node=stack.pop()
        print(node.data,end=" ")
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
        print()

def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)

def inorder_iterative(root):
    if not root:
        return
    stack=[]
    node=root
    while node or stack:
        if node:
            stack.append(node)
            node=node.left
        else:
            node=stack.pop()
            print(node.data,end=" ")
            node=node.right

def postorder(root):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data,end=" ")

def postorder_irterative(root):
    if not root:
        return
    stack=[]
    node=root
    visited=set()
    while stack or node:
        # print('visited',visited)
        if node:
            stack.append(node)
            node=node.left
        else:
            node=stack.pop()
            if node.right and not node.right in visited:
                stack.append(node)
                node=node.right
            else:
                visited.add(node)
                print(node.data,end=" ")
                node=None
                
def level_order(root):
    if not root:
        return
    q=[]
    q.append(root)
    while q:
        node=q.pop(0)
        print(node.data)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
        
def zigzag(root):
    if not root:
        return
    lefttoright=True
    currentLevel=[]
    nextLevel=[]
    
    while currentLevel:
        node=currentLevel.pop(0)
        print(node.data,end="")
        



root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)
root.right.left=node(6)
root.right.right=node(7)
# preorder_traversal(root)
# print()
# preorder_traversal_iterative(root)
# print("inorder")
# inorder(root)
# print()
# inorder_iterative(root)
# print("postorder")
# postorder(root)
# print()
# postorder_irterative(root)
print('level_order')
level_order(root)