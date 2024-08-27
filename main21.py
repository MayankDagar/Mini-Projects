R={"OM":76, "JAI":45, "BOB":89, "ALI":65, "ANU":90, "TOM":82}
L = []

def push():
    for i in R:
        if R[i]>=75:
            L.append(i)
    print(L)

def pop():
    if L==[]:
        print("Stack is empty")
    else:
        print("Poped element is: ", L.pop())

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
