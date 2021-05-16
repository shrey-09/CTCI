# 4.4
# Check Balanced

def checkBalanced(root):
    if not root:
        return True,0
    l,r=0,0
    if root.left:
        bl,l=checkBalanced(root.left)
        if not bl:
            return False,max(l+1,r+1)
    if root.right:
        br,r=checkBalanced(root.right)
        if not br:
            return False,max(l+1,r+1)
    
    if abs(l-r)>1:
        return False,max(l+1,r+1)
    return True,max(l+1,r+1)

def isBalanced(root):
    a,b=checkBalanced(root)
    return a
    
    