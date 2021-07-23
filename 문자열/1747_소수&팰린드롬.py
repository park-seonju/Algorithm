def eratosfunc(l):
    eratos=[1]*(l+1)
    eratos[0],eratos[1]=0,0
    for i in range(2,l):
        if eratos[i]:
            for j in range(i*2,l,i):
                eratos[j]=0
    return eratos
def palindrome(number):
    s=str(number)
    if s==s[::-1]:
        return True
    return False
n=int(input())
prime=eratosfunc(1003001)
for num in range(n,1003001):
    if prime[num] and palindrome(num):
        print(num)
        break
else:
    print(1003001)


# n = int(input())

# def is_pel(number):
#     l, r = 0, len(number)-1
#     while l < r:
#         if number[l]==number[r]:
#             l += 1
#             r -= 1
#         else:
#             return False
#     return True

# def is_prime(number):
#     num = int(number**(0.5))
#     for i in range(2, num+1):
#         if number%i == 0:
#             return False
#     return True

# if n==1:
#     n = 2
    
# while True:
#     if is_pel(str(n)) and is_prime(n):
#         print(n)
#         break
#     n += 1