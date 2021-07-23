def func(x):
    if x==1 or x==2:
        return 1
    return func(x-1)+func(x-2)
list1=[func(i) for i in range(1,11)]
print(list1)