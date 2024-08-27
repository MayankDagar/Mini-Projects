def REMOVE_A():
    f = open("Text files/Country.txt", "r")
    z = open("Text files/a.txt", "w")
    d = f.readlines()
    for i in d:
        if "a" in i:
            z.write(i)
    z.close()
    f.close()
REMOVE_A()
