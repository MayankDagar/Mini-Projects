import csv

def add():
    f = open("Csv files/shop.csv", "w")
    d = csv.writer(f)
    L = []
    n = int(input("How many items do you want to enter: "))
    for i in range(n):
        id = int(input("Enter item id: "))
        name = input("Enter item name: ")
        price = int(input("Enter price: "))
        l = [id, name, price]
        L.append(l)
    d.writerows(L)
    f.close()

def countr():
    f = open("Csv files/shop.csv", "r")
    d = csv.reader(f)
    c = 0
    for i in d:
        c += 1
    print("Total number of items in file: ", c)
    f.close()

while True:
    print("*************************************************")
    print("1. Add items")
    print("2. Count items")
    print("3. Exit")
    print("*************************************************")
    a = int(input("Enter the function number which you want to run: "))
    if a==1:
        add()
    elif a==2:
        countr()
    elif a==3:
        quit()
    else:
        print("Invalid option")
