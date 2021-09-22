x={
    '国語': 75,
    '算数': 80,
    '数学': 80, 
    '理科': 65, 
    '社会': 90, 
    '英語': 70,
}
for key,value in x.items():
    if key=='国語':
        print('{',key,':',value,',',end='')
    elif key=='算数':
        print(key,':',value,'}')
for key,value in x.items():
    if key=='国語':
        print('{',key,':',value,',',end='')
    elif key=='数学':
        print(key,':',value,'}')
for key,value in x.items():
    if key=='国語':
        print('{',key,':',value,',',end='')
    elif key=='数学':
        print(key,':',value,',',end='')
    elif key=='理科':
        print(key,':',value,',',end='')
    elif key=='社会':
        print(key,':',value,',',end='')
    elif key=='英語':
        print(key,':',value,'}',end='')
    