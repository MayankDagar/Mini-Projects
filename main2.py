def largest(a, b, c):
    if (a>b) and (a>c):
        print(a, "is greater")
    elif (b>a) and (b>c):
        print(b, "is greater")
    else:
        print(c, "is greater")
x = int(input("Enter 1st number: "))
y = int(input("Enter 2nd number: "))
z = int(input("Enter 3rd number: "))
largest(x, y, z)
