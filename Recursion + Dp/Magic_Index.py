# 8.3
# Magic Index

def magicIndex(arr):
    start,end=0,len(arr)-1
    while start<=end:
        mid=(start+end)//2
        if arr[mid]==mid:
            return mid
        elif arr[mid]<mid:
            start=mid+1
        else:
            end=mid-1
    return -1