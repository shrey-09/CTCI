# 4.3
# List Of List of Depths


# class TreeNode():
#     def __init__(self,v):
#         self.val=v
#         self.left=None
#         self.right=None
# class ListNode():
#     def __init__(self,v):
#         self.val=v
#         self.next=None


def arrayToLL(arr):
    if len(arr)==0:
        return None
    head=ListNode(arr[0].val)
    p=head
    for x in range(1,len(arr)):
        temp=ListNode(arr[x].val)
        p.next=temp
        p=temp
    return head

def listOfDepths(root):
    if not root:
        return []
    arr=[ListNode(root.val)]
    cl=[root]
    nl=[]
    while len(cl)>0:
        temp=cl.pop(0)
        if temp:
            nl.append(temp.left)
            nl.append(temp.right)
        if len(cl)==0:
            head=arrayToLL(nl)
            arr.append(head)
            cl,nl=nl,cl
    return arr