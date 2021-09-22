x={
    'id':'100',
    'name':'大原太郎',
    'age':'19',
}
x.update(age=20)
for key,value in x.items():
    print(key,':',value)