L = []

def push_element():
    stud_no = int(input("Enter student number: "))
    name = input("Enter student name: ")
    fee = int(input("Enter fee: "))
    l = [stud_no, name, fee]
    L.append(l)

def pop_element():
    if L == []:
        print("Stack is empty")
    else:
        print("The deleted element is: ", L.pop())

while True:
    print("*************************************************")
    print("1. Push Elements")
    print("2. Pop elements")
    print("3. Exit")
    print("*************************************************")
    a = int(input("Enter the function number which you want to run: "))
    if a==1:
        push_element()
    elif a==2:
        pop_element()
    elif a==3:
        quit()
    else:
        print("Invalid option")
