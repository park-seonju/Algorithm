n=int(input())
arr=list(map(int,input().split()))

st=[arr[0]]

for num in arr[1:]:
    if st[-1] >num: # 10,20,30
        l,r=0,len(st)-1 #0,2
        while l<=r: #0,2 / 2 2 / 2 1
            mid=(l+r)//2 # 1 / 2  
            if st[mid]<num: l=mid+1 #20<30 l=2 /  
            else: r=mid-1 # r=1
        st[l]=num # 2 20
    elif st[-1]<num:st.append(num)
    print(st)
print(st)