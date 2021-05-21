def isFound(r1,r2):
    if not r1 and not r2:
        return True
    elif not r1 and r2:
        return False
    elif r1.val!=r2.val:
        return False
    elif r1.val==r2.val:
        return isFound(r1.left,r2.left) and isFound(r1.right,r2.right)

def contains(r1,r2):
    if isFound(r1,r2):
        return True
    return isFound(r1.left,r2) or isFound(r1.right,r2)