def upper():
    f = open("Text files\story.txt", "r")
    d = f.read()
    a = 0
    for i in d:
        if i.isupper():
            a += 1
    print("Number of upper case letters are: ", a)
    f.close()

def lower():
    f = open("Text files\story.txt", "r")
    d = f.read()
    a = 0
    for i in d:
        if i.islower():
            a += 1
    print("Number of lower case letters are: ", a)
    f.close()

def digit():
    f = open("Text files\story.txt", "r")
    d = f.read()
    a = 0
    for i in d:
        if i.isdigit():
            a += 1
    print("Number of digits are: ", a)
    f.close()

def space():
    f = open("Text files\story.txt", "r")
    d = f.read()
    a = 0
    for i in d:
        if i==" ":
            a += 1
    print("Number of spaces are", a)
    f.close()

def vowel():
    f = open("Text files\story.txt", "r")
    d = f.read()
    a = 0
    for i in d:
        if i.lower()=="a" or i.lower()=="e" or i.lower()=="i" or i.lower()=="o" or i.lower()=="u":
            a += 1
    print("Number of vowels are: ", a)
    f.close()

while True:
    print("*************************************************")
    print("1. How many upper case letters are present")
    print("2. How many lower case letters are present")
    print("3. How many digits are present")
    print("4. How many spaces are present")
    print("5. How many vowels are present")
    print("6. Exit")
    print("*************************************************")
    a = int(input("Enter the function number which you want to run: "))
    if a==1:
        upper()
    elif a==2:
        lower()
    elif a==3:
        digit()
    elif a==4:
        space()
    elif a==5:
        vowel()
    elif a==6:
        quit()
    else:
        print("Invalid option")