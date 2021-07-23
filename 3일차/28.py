dict1={"TV": 2000000,
"냉장고": 1500000,
"책상": 350000,
"노트북": 1200000,
"가스레인지": 200000,
"세탁기": 1000000}
result_key=sorted(dict1.keys(),reverse=False)
result_value=sorted(dict1.values(),reverse=True)
result=sorted(dict1.items(), key=lambda v:v[1],reverse=True)
# print(result)
# print(result_key)
# print(result_value)
for key,value in result:
    print(key+':',value)