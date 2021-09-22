color={
    '赤':'red', 
    '白':'white',
    '黒':'black',
    '青':'blue',
    '緑':'green',
}

def view(array):
    keys=list(array.keys())
    for key in keys:
        value=array.get(key)
        print(key,':',value,sep='')
        
view(color)