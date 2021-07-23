num = 8
while num > 0:
	num -= 1
	if num % 2 == 0: continue
	print("{:^7}".format("*"*num))