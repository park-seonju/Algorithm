string='Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'
moeum='aeiou'
list1=[i for i in string if i not in moeum]
print("".join(list1))