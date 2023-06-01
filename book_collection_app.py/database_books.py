#store and retrive books from a csv file

books_file = 'books.txt'


def create_book_table():
    with open(books_file, 'w'):     #'as file' is optional when not using the variable for anything
        pass


def add_book(name, author):
    with open(books_file, 'a') as file:        #'appends' instead of 'writes' to keep current books on the list and add new books
        file.write(f"{name},{author},0\n")
    # books.append({'name': name, 'author': author, 'read': False})
 

def mark_book_read(name):
    books = get_all_books() 
    for book in books:
        if book['name'] == name:
            book['read'] = '1'
    
    _save_books(books)  


def _save_books(books):      #don't call this function
    with open(books_file, 'w') as file:
        for book in books:
            file.write(f"{book['name']},{book['author']},{book['read']}\n")



def get_all_books():
    with open(books_file, 'r') as file:
        lines = [line.strip().split(',') for line in file.readlines()]

    return [

        {'name': line[0], 'author': line[1], 'read': line[2]}
        for line in lines

    ]


def delete_book(name):
    books = get_all_books()        
    books = [book for book in books if book['name'] != name]
    _save_books(books)
 