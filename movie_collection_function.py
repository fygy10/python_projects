#empty list that movies are added to (in lieu of a database)
movies = []

#the menu prompt for users to choose a selection/action
menu = ("\nWould you like to review your movie collection, add a movie, remove a movie, or end the program? "
                  "Your options are: 'review', 'add', 'find', 'quit': \n")


#information needed to add a movie and how it is stored as a dictionary
def add_movie():
    title = input("What is the title of the movie: ")
    director = input("What is the director of the movie: ")
    release_year = input("What is the release year of the movie: ")
    # release_year = int(release_year)
    movies.append({

        'title': title,
        'director': director,
        'year': release_year,

        })
        
    
#the process for reviewing movies
def review_movie():
    for movie in movies:
        print_movie(movie)

#how movies are printed when review; related to the fucntion immediately above this
def print_movie(movie):
    print(f"Title: {movie['title']}")
    print(f"Director: {movie['director']}")
    print(f"Release Year: {movie['year']}")


#the process for finding movies
def find_movie():
    search_movie = (input("Which movie do you want to find in your collection? "))
    for movie in movies:
        if movie['title'] == search_movie:
            print_movie(movie)


#user options dictionary instead of a long list of if-else statements
user_options = {

    "add": add_movie,
    "review": review_movie,
    "find": find_movie,

}


#the main function that is called when the program is activated
def user_menu():
    selection = input(menu)
    while selection != "quit":

        if selection in user_options:
            selected_option = user_options[selection]
            selected_option() 

        else:
            print("Unknown selection, please try again")

        selection = input(menu)


user_menu()


# #the five minute version of the more complete fucntion above
# movies = []

# user_options = input("Would you like to review your movie collection, add a movie, remove a movie, or end the program? "
#                   "Your options are: 'review', 'add', 'quit': ")


# #what data for each movie to store: title, director, release year
# #movie storage: add movies to a list with append
# while user_options != "quit":

#     if user_options == "review":
#         print(movies)

#         user_options = input("Would you like to review your movie collection, add a movie, remove a movie, or end the program? "
#                   "Your options are: review, add, remove, quit: ")


#     elif user_options == "add":
#         title = input("What is the title of the movie: ")
#         director = input("What is the director of the movie: ")
#         release_year = input("What is the release year of the movie: ")
#         release_year = int(release_year)
#         movies.append({

#         'title': title,
#         'director': director,
#         'year': release_year,

#         })
        
#         user_options = input("Would you like to review your movie collection, add a movie, remove a movie, or end the program? "
#                   "Your options are: review, add, remove, quit: ")

#     elif user_options == "review":
#         print(movies)
#         user_options = input("Would you like to review your movie collection, add a movie, remove a movie, or end the program? "
#                   "Your options are: review, add, remove, quit: ")


#     else:
#         print("Program terminated successfully")
#         user_options = input("Would you like to review your movie collection, add a movie, remove a movie, or end the program? "
#                   "Your options are: review, add, remove, quit: ")

#     # print(movies)       #testing user inputs being properly recorded

#     print(user_options)