L = [3,5,10,12,15]

def modlist():
    for i in L:
        if i%5==0:
            i+=10
        print(i)
modlist()
