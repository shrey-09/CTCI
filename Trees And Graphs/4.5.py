# 4.5
# Valid BST

def isValidBST(self, root: TreeNode) -> bool:
    
    def validBST(root,start,end):
        if not root:
            return True
        if start<root.val<end:
            if root.left and root.right:
                return validBST(root.left,start,root.val) and validBST(root.right,root.val,end)
            elif root.left:
                return validBST(root.left,start,root.val)
            elif root.right:
                return validBST(root.right,root.val,end)
            else:
                return True
        else:
            return False
    
    return validBST(root,-float('inf'),float('inf'))