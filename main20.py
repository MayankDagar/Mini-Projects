L = []

def push():
    no = int(input("Enetr book number: "))
    name = input("Enter book name: ")
    price = int(input("Enter book price: "))
    l = [no, name, price]
    L.append(l)

def pop():
    if L == []:
        print("Stack is empty")
    else:
        print("Deleted element is: ", L.pop())

def display():
    print(L[::-1])

while True:
    print("*************************************************")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")
    print("*************************************************")
    a = int(input("Enter the function number which you want to run: "))
    if a==1:
        push()
    elif a==2:
        pop()
    elif a==3:
        display()
    elif a==4:
        exit()
    else:
        print("Invalid option")
