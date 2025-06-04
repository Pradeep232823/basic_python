def BinarySearch(data,key):
    s=0
    e=len(data)-1
    while s<=e:
        mid=(s+e)//2
        if data[mid]==key:
            return mid
        elif data[mid]>key: e=mid-1
        else: s=mid+1
    return -1
a=[5,8,10,12,41,45,81,108]
print(BinarySearch(a,45))