def total_word():
    f = open("Text files/story.txt", "r")
    d = f.read()
    c = 0
    for i in d:
        c += len(i)
    print("Total number or words present in the file is/are: ", c)
    f.close()

def count5():
    f = open("Text files/story.txt", "r")
    d = f.read().split()
    c = 0
    L = []
    for i in d:
        if len(i)>=5:
            c += 1
            L.append(i)
    print("Total number of words having length more tha 5 or equal to 5 is/are: ", c)
    print("Words having length more tha 5 or equal to 5 is/are: ", L)
    f.close()

def count_the():
    f = open("Text files/story.txt", "r")
    d = f.read().split()
    the = 0
    for i in d:
        if i.lower()=="the":
            the += 1
    print("Number of times 'the' is present: ", the)
    f.close()

while True:
    print("*************************************************")
    print("1. Count total number of words present in file.")
    print("2. Count and display words having length 5 or more characters.")
    print("3. Count of word “the”.")
    print("4. Exit")
    print("*************************************************")
    a = int(input("Enter the function number which you want to run: "))
    if a==1:
        total_word()
    elif a==2:
        count5()
    elif a==3:
        count_the()
    elif a==4:
        quit()
    else:
        print("Invalid option")
