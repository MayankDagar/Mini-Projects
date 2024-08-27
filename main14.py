import pickle

def add():
    f = open("Binary files/students.dat", "wb")
    r = int(input("Enter roll number: "))
    n = input("Enter name: ")
    m = int(input("Enter marks: "))
    l = [r, n, m]
    pickle.dump(l, f)
    f.close()

def search():
    f = open("Binary files/students.dat", "rb")
    a = pickle.load(f)
    b = int(input("Enter roll number you want to search: "))
    if a[0]==b:
        print("Name: ", a[1])
        print("Marks: ", a[2])
    f.close()

while True:
    print("*************************************************")
    print("1. Add students")
    print("2. Search students")
    print("3. ")
    print("4. Exit")
    print("*************************************************")
    a = int(input("Enter the function number which you want to run: "))
    if a==1:
        add()
    elif a==2:
        search()
    elif a==3:
        quit()
    else:
        print("Invalid option")
