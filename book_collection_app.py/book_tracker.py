#tracking books read and recording them
import database_books
# import database_books_json  #using json for database; need to change when function are calling from


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
    database_books.add_book(name, author)
    # database_books_json.add_book(name, author)


def list_books():
    # books = database_books_json.get_all_books()
    books = database_books.get_all_books()
    for book in books:
        read = 'Yes' if book['read'] == '1' else 'No'   #csv databse line
        # read = 'Yes' if book['read'] else 'No'    #this line if using json database instead of csv
        print(f"{book['name']} by {book['author']}; Already read?: {read}")

    # for book in database_books.books:
    #     read = 'Yes' if book['read'] else 'No'
    #     print(f"{book['name']} by {book['author']}; Read Status: {read}")

def delete_book():
    name = input("Which book do you want to delete? ")
    database_books.delete_book(name) 
    # database_books_json.delete_book(name) 

def read_book():
    name = input("What book did you read? ")
    database_books.mark_book_read(name)
    # database_books_json.mark_book_read(name)

    # for book in database_books.books:     #can add author for more granularity if two books with the same title
    #     if book['name'] == name:
    #         book['read'] = True

user_options = {

    'add': add_book,
    'list': list_books,
    'read': read_book,
    'delete': delete_book,

}

def menu(): 
    # database_books_json.create_book_table()  #list books when empty database
    database_books.create_book_table()  #list books when empty database
    user_input = input(user_menu)
    while user_input != 'exit':
        if user_input in user_options:
            selected_option = user_options[user_input]
            selected_option()
        
        else:
            print("Unknown slection, please try again with a valid option")

        user_input = input(user_menu)

menu()