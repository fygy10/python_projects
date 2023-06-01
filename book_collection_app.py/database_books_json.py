#store and retrive books from a json file
import json

books_file = 'books.json'


def create_book_table():
    with open(books_file, 'w') as file:     
        json.dump([], file)     #initialized to an empty list to avoid error


def add_book(name, author):
    books = get_all_books()
    books.append({'name': name, 'author': author, 'read': False})
    _save_books(books)
 

def mark_book_read(name):
    books = get_all_books() 
    for book in books:
        if book['name'] == name:
            book['read'] = True
    
    _save_books(books)  


def _save_books(books):      #don't call this function
    with open(books_file, 'w') as file:
        json.dump(books, file)



def get_all_books():
    with open(books_file, 'r') as file:
        return json.load(file)


def delete_book(name):
    books = get_all_books()        
    books = [book for book in books if book['name'] != name]
    _save_books(books)