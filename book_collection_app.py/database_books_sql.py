#store and retrive books from a sqlite database
import sqlite3

def create_book_table():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    #creates a table with columns, the type of data in the columns, and the main data column
    cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)') 

    connection.commit()
    connection.close()


def add_book(name, author):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    # cursor.execute(f'INSERT INTO books VALUES("{name}", "{author}", 0)')    #not recommended 
    #inserts inputted data into the table
    cursor.execute('INSERT INTO books VALUES(?, ?, 0)', (name, author))

    connection.commit()
    connection.close()
 

def mark_book_read(name):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    #updates the book read status in place in the table
    cursor.execute('UPDATE books SET read = 1 WHERE name = ?', (name,))
    
    connection.commit()
    connection.close()

def get_all_books():   
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    #selects the enitre table
    cursor.execute('SELECT * FROM books')
    #selects all of the rows (name, author, read); list comprehnsion for a dictionary to make output format in script (book_tracker.py)
    books = [{'name': row[0], 'author': row[1], 'read': row [2]} for row in cursor.fetchall()]

    connection.commit()
    connection.close()

    return books


def delete_book(name):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    #deletes the books from the table in place
    cursor.execute('DELETE FROM books WHERE name = ?', (name,))

    connection.commit()
    connection.close()