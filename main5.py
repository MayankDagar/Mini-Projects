def oddeven():
    for i in L:
        if i%2 == 0:
             Even.append(i/2)
        else:
            Odd.append(i**2)
    print("Even numbers: ", Even)
    print("Odd numbers: ", Odd)

L = []
Even = []
Odd = []
n = int(input("How many values do you want to enter: "))
for i in range(n):
    a = int(input("Enter the number: "))
    L.append(a)
oddeven()