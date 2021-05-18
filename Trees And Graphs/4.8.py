# 4.8
# First Common Ancestor

def lowestCommonAncestor(root, p, q):
    if root==None:
        return None
    if root==p or root==q:
        return root
    
    leftLCA= lowestCommonAncestor(root.left,p,q)
    rightLCA= lowestCommonAncestor(root.right,p,q)
    
    if leftLCA and rightLCA:
        return root
    elif leftLCA==None:
        return rightLCA
    else:
        return leftLCA