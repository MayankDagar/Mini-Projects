import pickle

def CreateFile():
    f = open("Binary files/Book.dat", "wb")
    book_no = int(input("Enter book number: "))
    book_name = input("Enter book name: ")
    author = input("Enter author name: ")
    price = int(input("Enter price: "))
    l = [book_no, book_name, author, price]
    pickle.dump(l, f)
    f.close()

def CountRec():
    f = open("Binary files/Book.dat", "rb")
    a = pickle.load(f)
    b = input("Enter author name you want to search: ").lower()
    c = 0
    if a[2].lower() == b:
        c += 1
    print("Total number books by", b, "is: ", c)

while True:
    print("*************************************************")
    print("1. Add record")
    print("2. Count record")
    print("3. Exit")
    print("*************************************************")
    a = int(input("Enter the function number which you want to run: "))
    if a == 1:
        CreateFile()
    elif a == 2:
        CountRec()
    elif a == 3:
        quit()
    else:
        print("Invalid option")
