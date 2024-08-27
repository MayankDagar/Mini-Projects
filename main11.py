def start():
    f = open("Text files/Country.txt", "r")
    d = f.readlines()
    w = 0
    h = 0
    for i in d:
        if i[0].lower()=="w":
            w += 1
        elif i[0].lower()=="h":
            h += 1
    print("Number of lines starting with W or w: ", w)
    print("Number of lines starting with H or h: ", h)
    f.close()
start()
