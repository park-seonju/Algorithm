fruit = ['   apple    ','banana','  melon']
dict1={i.replace(" ",""):len(i.replace(" ","")) for i in fruit}
print(dict1)