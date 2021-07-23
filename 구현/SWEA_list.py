def maximun(boxes):
    maxnum=0
    for i in boxes:
        if i > maxnum:
            maxnum=i
    idx=boxes.index(maxnum)
    boxes[idx]-=1
    return max(boxes)

def minimum(boxes):
    lownum=100
    for i in boxes:
        if i < lownum:
            lownum=i
    idx=boxes.index(lownum)
    boxes[idx]+=1
    return min(boxes)


for test_num in range(1,11):
    top=0
    low=0
    num=int(input())
    boxes=list(map(int,input().split()))
    for _ in range(num):
        top=maximun(boxes)
        low=minimum(boxes)
    print("#{} {}".format(test_num,top-low))