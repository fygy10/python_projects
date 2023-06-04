#tracking books read and recording them
import database_books_sql_cm
# import database_books_json  #using json for database
# import database_books_csv #using csv for database
# import database_books_sql #using sql for database (without context manager)

user_menu = """ 

Welcome to the Boostore App!\n
Enter an option from the list below:
 -'add' to add a book
 -'list' to list all books
 -'read' to mark a book as read
 -'delete' to delete a book
 -'exit' to exit the program

Your choice: 
"""

def add_book():
    name = input("What is the name of the book? ")
    author = input("What is the author of the book? ")
    database_books_sql_cm.add_book(name, author)

def list_books():
    books = database_books_sql_cm.get_all_books()
    for book in books:
        read = 'Yes' if book['read'] else 'No'   
        # read = 'Yes' if book['read'] == '1' else 'No'    #this line if using csv database
        print(f"{book['name']} by {book['author']}; Already read?: {read}")

def delete_book():
    name = input("Which book do you want to delete? ")
    database_books_sql_cm.delete_book(name) 

def read_book():
    name = input("What book did you read? ")
    database_books_sql_cm.mark_book_read(name)

user_options = {

    'add': add_book,
    'list': list_books,
    'read': read_book,
    'delete': delete_book,

}

def menu(): 
    database_books_sql_cm.create_book_table()  #list books when empty database
    user_input = input(user_menu)
    while user_input != 'exit':
        if user_input in user_options:
            selected_option = user_options[user_input]
            selected_option()
        
        else:
            print("Unknown slection, please try again with a valid option")

        user_input = input(user_menu)

menu()