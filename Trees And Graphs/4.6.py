# 4.6
# Successor (Binary Tree)

class Node:
    def __init__(self,val,p):
        self.parent=p
        self.val=val
        self.right=None
        self.left=None

def leastRight(node):
    while node.left:
        node=node.left
    return node

def inorderSuccessor(node):
    if not node:
        return None
    if node.right:
        return leastRight(node.right)
    else:
        t=node.val
        while node.parent and t>node.parent.val:
            node=node.parent
        return node.parent

def createTree():
    root=Node(45,None)
    root.left=Node(17,root)
    root.left.left=Node(7,root.left)
    root.left.left.left=Node(6,root.left.left)
    root.left.left.right=Node(8,root.left.left)
    root.left.right=Node(26,root.left)
    root.right=Node(58,root)
    root.right.left=Node(57,root.right)
    root.right.right=Node(69,root.right)
    return root

root=createTree()

print(root.val,inorderSuccessor(root).val)
print(root.left.val,inorderSuccessor(root.left).val)
print(root.left.left.val,inorderSuccessor(root.left.left).val)
print(root.left.left.left.val,inorderSuccessor(root.left.left.left).val)
print(root.left.left.right.val,inorderSuccessor(root.left.left.right).val)
print(root.left.right.val,inorderSuccessor(root.left.right).val)
print(root.right.val,inorderSuccessor(root.right).val)
print(root.right.left.val,inorderSuccessor(root.right.left).val)
# print(root.right.right.val,inorderSuccessor(root.right.right).val) RunTimeError, None has no object ".val"