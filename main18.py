import random
while True:
    print("Random number is: ", random.randrange(7))
    n = input("Want to continue: (Y/N): ").lower()
    if n == "n":
        quit()
        
