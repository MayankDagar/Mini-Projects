import csv

def addCsvFile():
    f = open("Csv files/user.csv", "w")
    a = csv.writer(f)
    L = []
    n = int(input("How many username and password you want to enter: "))
    for i in range(n):
        u = input("Enter username: ")
        p = input("Enter password: ")
        l = [u, p]
        L.append(l)
    a.writerows(L)
    f.close()

def search():
    f = open("Csv files/user.csv", "r")
    a = csv.reader(f)
    n = input("Enter username to check password: ")
    for i in a:
        if i[0] == n:
            print("Password: ", i[1])
            break
        else:
            print("Username not found")
            break
    f.close()

while True:
    print("*************************************************")
    print("1. Add username and password")
    print("2. Search password")
    print("3. Exit")
    print("*************************************************")
    a = int(input("Enter the function number which you want to run: "))
    if a==1:
        addCsvFile()
    elif a==2:
        search()
    elif a==3:
        quit()
    else:
        print("Invalid option")
