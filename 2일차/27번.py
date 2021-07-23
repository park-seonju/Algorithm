list1=[12,24,35,24,88,120,155,88,120,155]

def remove(list1):
    result=list(sorted(set(list1)))
    print(result)
remove(list1)