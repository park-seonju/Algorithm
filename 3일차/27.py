dict = {'홍길동':'010-1111-1111','이순신':'010-1111-2222','강감찬':'010-1111-3333'}
a=input()
for key,value in dict.items():
    if a==key:
        print('아래 학생들의 전화번호를 조회할 수 있습니다.\n홍길동\n이순신\n강감찬\n전화번호를 조회하고자 하는 학생의 이름을 입력하십시오.\n이순신의 전화번호는 {}입니다.'.format(value))