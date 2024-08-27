def hash():
    f = open("Text files/space.txt", "r")
    d = f.read()
    a = d.replace(" ", "#")
    b = a.replace("\n", "#")
    print(b, end="#")
    f.close()
hash()
