# 4.12
# Paths With Sum

class Node:
    def __init__(self,v):
        self.val=v
        self.right=None
        self.left=None

def containsSumFromNode(root,target):
    if not root:
        return 0
    if root.val==target:
        return 1
    if not root.left and not root.right and root.val!=target:
        return 0
    return containsSumFromNode(root.left,target-root.val) + containsSumFromNode(root.right,target-root.val)

def createTree():
    root=Node(45)
    root.left=Node(15)
    root.left.left=Node(30)
    root.left.left.left=Node(30)
    root.left.left.right=Node(40)
    root.left.right=Node(45)
    root.right=Node(60)
    root.right.left=Node(57)
    root.right.right=Node(69)
    return root

def containsSum(root,target):
    if not root:
        return 0
    return containsSumFromNode(root,target) + containsSum(root.left,target) + containsSum(root.right,target)

print(containsSum(createTree(),60))