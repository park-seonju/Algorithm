def reversesort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr) // 2
    arr1 = arr[:mid]
    arr2 = arr[mid:]
    arr3 = merge(reversesort(arr1),reversesort(arr2))
    return arr3
 
def merge(arr1,arr2):
    result = []
    while len(arr1)>0 or len(arr2)>0:
        if len(arr1)>0 and len(arr2)>0:
            piv1 = arr1[0]
            piv2 = arr2[0]
            if piv1>piv2:
                result.append(piv1)
                arr1 = arr1[1:]
            else:
                result.append(piv2)
                arr2 = arr2[1:]
        elif len(arr1)>0:
            result += arr1
            arr1 = []
        elif len(arr2)>0:
            result += arr2
            arr2 = []
    return result
n=int(input())
boxes=[]
for i in range(n):
    info=list(map(int,input().split()))
    print(reversesort(info))