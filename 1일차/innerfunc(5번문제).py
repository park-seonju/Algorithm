def problem(*args):
    result=1
    for i in args:
        if type(i) !=int:
            print('에러발생')
            return
        result*=i
    print(result)
problem(1,2,'4',3)