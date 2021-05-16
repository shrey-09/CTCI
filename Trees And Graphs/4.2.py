# 4.2
# Minimal Tree

class TreeNode:
    def __init__(self,v):
        self.val=v
        self.right=None
        self.left=None

def inorderTraversal(root):
    if not root:
        return
    if root.left:
        inorderTraversal(root.left)
    print(root.val,end="-")
    if root.right:
        inorderTraversal(root.right)
    return

def minimalTree(arr): #return TreeNode
    if len(arr)==1:
        return TreeNode(arr[0])
    if len(arr)==0:
        return None
    mid=len(arr)//2
    root=TreeNode(arr[mid])
    root.left=minimalTree(arr[:mid])
    root.right=minimalTree(arr[mid+1:])
    return root

arr=[1,3,4,6,8,9,10,20,32,45,87]
inorderTraversal(minimalTree(arr))