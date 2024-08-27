def count():
    f = open("Text files/space.txt", "r")
    d = f.readlines()
    a = 0
    for i in d:
        if i[0].lower()=="p" or i[0].lower()=="t":
            a += 1
    print("Number of lines starting with P and T: ", a)
    f.close()

def vowel():
    f = open("Text files/space.txt", "r")
    d = f.readlines()
    a = 0
    for i in d:
        if i[0].lower()=="a" or i[0].lower()=="e" or i[0].lower()=="i" or i[0].lower()=="o" or i[0].lower()=="u":
            a += 1
    print("Number of lines starting with vowels: ", a)
    f.close()

while True:
    print("*************************************************")
    print("1. How many lines starting with P and T")
    print("2. How many lines starting with vowels")
    print("3. Exit")
    print("*************************************************")
    a = int(input("Enter the function number which you want to run: "))
    if a==1:
        count()
    elif a==2:
        vowel()
    elif a==3:
        quit()
    else:
        print("Invalid option")