from app import books

user_options = """

Enter one of the following:\n
-'cheapest'
-'best'
-'optimal'
-'next'
-'quit'

Your choice is: 
"""


#sorting books by rating
def print_best_books():
    best_books = sorted(books, key = lambda x: x.rating * -1)[:5]   #sort decending [:5] denotes top five
    # best_books = sorted(books, key = lambda x: x.rating)   #sort ascending (defualt)
    for book in best_books:
        print(book)


def print_cheapest_books():
    cheap_books = sorted(books, key = lambda x: x.price)[:5]    #default sort ascending
    for book in cheap_books:
        print(book)


def best_cheapest_books():
    best_cheap = sorted(books, key = lambda x: (x.rating * -1, x.price))[:5] #sort with tuple for multiple criteria
    for book in best_cheap:
        print(book)


book_generator = (book for book in books)

def get_next_book():
    print(next(book_generator))

user_selection = {

    'cheapest': print_cheapest_books,
    'best': print_best_books,
    'optimal': best_cheapest_books,
    'next': get_next_book,

}


def user_menu():
    user_input = input(user_options)
    while user_input != 'quit':
        if user_input in ('cheapest', 'best', 'optimal', 'next'):
            user_selection[user_input]()
        else:
            print("Unknown slection, please try again with a valid option")

        user_input = input(user_options)

user_menu()


# print(print_best_books())
# print(print_cheapest_books())
# print(best_cheapest_books())
