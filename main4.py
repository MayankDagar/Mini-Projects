FRINDS = {}

def search():
    a = input("Enter friend name to search mobile number: ")
    if a in FRINDS:
        print(FRINDS.get(a))

while True:
    x = input("Enter friend name: ")
    y = int(input("Enter friend mobile number :"))
    z = {x:y}
    FRINDS.update(z)
    c = input("Want to add more values: Y/N: ")
    if c.lower() == "n":
        break
search()
