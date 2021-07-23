word=input()
if 65<=ord(word)<=90:
    print('{}(ASCII: {}) => {}(ASCII: {})'.format(word,ord(word),chr(ord(word)+32),ord(word)+32))
elif 97<=ord(word)<=122:   #ord string 아스키 10진수로
    print('{}(ASCII: {}) => {}(ASCII: {})'.format(word,ord(word),chr(ord(word)-32),ord(word)-32))
else:
    print(word)