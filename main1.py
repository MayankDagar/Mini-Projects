def Primeornot(N):
    for i in range(2, N):
        if N%i==0:
            print(N, "is not a prime number")
            break
        else:
            print(N, "is a prime number")
            break

def Is_Palindrome(N):
    if N==N[::-1]:
        print(N, "is a palindrome")
    else:
        print(N, "is not a palindrome")

def Fact(N):
    z = 1
    for i in range(1, N+1):
        z *= i
    print("Factorial: ", z)

def count(N):
    print(len(N))

while True:
    print("*************************************************")
    print("1. Check the number is prime or not.")
    print("2. Check the number palindrome or not.")
    print("3. Find the factorial of a number.")
    print("4. Count the number of digits")
    print("5. Exit")
    print("*************************************************")
    a = int(input("Enter the function number which you want to run: "))
    if a == 1:
        b = int(input("Enter the number: "))
        Primeornot(b)
    elif a == 2:
        b = input("Enter the number: ")
        Is_Palindrome(b)
    elif a == 3:
        b = int(input("Enter the number: "))
        Fact(b)
    elif a == 4:
        b  = input("Enter the number: ")
        count(b)
    elif a == 5:
        quit()
    else:
        print("Invalid option")
