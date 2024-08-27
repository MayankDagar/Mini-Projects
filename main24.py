import mysql.connector

connection= mysql.connector.connect(host="localhost", user="root", password="1365", database="LIBRARY")
cursor=connection.cursor()

def add_record():
    book_id= input("Enter Book ID: ")
    title=input("Enter Book Title: ") 
    author=input("Enter Book Author: ")
    cursor.execute(f"INSERT INTO BOOKS (Book_id, Title, Author) VALUES ('{book_id}', '{title}', '{author}')")
    connection.commit()
    print("Record Added Successfully")

def delete_record():
    book_id = input("Enter Book ID to delete: ")
    cursor.execute(f"DELETE FROM BOOKS WHERE Book_id= '{book_id}'")
    connection.commit()
    print("Record Deleted Successfully")

def update_record():
    book_id = input("Enter Book ID to update: ")
    title = input("Enter new Book Title: ")
    author = input("Enter new Book Author: ")
    cursor.execute(f"UPDATE BOOKS SET Title = '{title}', Author= '{author}' WHERE Book_id = '{book_id}'")
    connection.commit()
    print("Record Updated Successfully")

def search_record():
    book_id = input("Enter Book ID to search: ")
    cursor.execute(f"SELECT * FROM BOOKS WHERE Book_id = '{book_id}'")
    result = cursor.fetchone()
    if result:
        print("Book ID: ", result[0])
        print("Title:", result[1])
        print("Author:", result[2])
    else:
        print("No record found")

def show_all_data():
    cursor.execute("SELECT * FROM BOOKS") 
    results = cursor.fetchall()
    for result in results:
        print("Book ID:", result[0])
        print("Title:", result[1])
        print("Author:", result[2])

while True:
    print("\n*** LIBRARY MANAGEMENT SYSTEM ***")
    print("1. Add Record")
    print("2. Delete Record")
    print("3. Update Record")
    print("4. Search Record")
    print("5. Show All Data")
    print("6. Exit")
    choice=int(input("Enter your choice: "))
    if choice == 1:
        add_record()
    elif choice == 2:
        delete_record()
    elif choice == 3:
        update_record()
    elif choice == 4:
        search_record()
    elif choice == 5:
        show_all_data()
    elif choice == 6:
        connection.close()
        break
    else:
        print("Invalid choice, try again")