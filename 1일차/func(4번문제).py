num=int(input())
def fibonacci(num):
    list1=[1]
    for i in range(1,num):
        if(i==1):
            list1.append(1)
        else:
            list1.append(list1[i-2]+list1[i-1])
    print(list1)
fibonacci(num)
