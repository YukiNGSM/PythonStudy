for i in reversed(range(1,10,2)):
    print(i,'の段',sep='')
    for j in reversed(range(1,10)):
        print(i,'×',j,'=',i*j)