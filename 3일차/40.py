list1=[]
while True:
   try:
      a = input()
      list1.append(a)
   except:
       break;
for i in list1:
   print(">> {}".format(i.upper()))