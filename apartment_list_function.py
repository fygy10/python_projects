apartments = []

menu = ("\nWelcomne to your apartment colleciton app. Please enter 'add' to add a new apartment to the collection, 'review' to review your collection"
        " 'find' to look up the apartments in your collection by category or address, or 'quit' to exit the program.\n")

#this function adds a new apartment to the collection
def add_apartment():
    apartment_steet = input("Please enter the apartment's address (ex. 42 Chandler St.): ")
    apartment_price = input("Please enter the monthyl price of the apartment (ex. $3000): ")
    apartment_neighborhood = input("Please enter the neighborhood of the apartment: ")

    apartments.append({
        
        'street name': apartment_steet,
        'apartment price': apartment_price,
        'apartment neighborhood': apartment_neighborhood

        })

#this function looks up a specific apartment
def find_apartment():
    specific_apartment = input("Narrow your search for an apartment by entering a stree address, neighborhood, or price: ")
    for apartment in apartments:
        if apartment['street name'] == specific_apartment:
            print_apartment(apartment)
        elif apartment['apartment neighborhood'] == specific_apartment:
            print_apartment(apartment)
        elif apartment['apartment price'] == specific_apartment:
            print_apartment(apartment)


#how the printed out apartment collection information appears to the user
def print_apartment(apartment):
    print(f"\nThe apartment on {apartment['street name']} costs {apartment['apartment price']} and is located in the {apartment['apartment neighborhood']} neighborhood")


#this function shows the entire collection of apartments
def review_apartment():
    for apartment in apartments:
        print_apartment(apartment)


user_options = {

    'add': add_apartment,
    'find': find_apartment,
    'review': review_apartment,

}


#this function executes the program
def collections():
    selection = input(menu)
    while selection != "quit":

        if selection in user_options:
            selected_option = user_options[selection]
            selected_option()
        else:
            print("Please select a valid option")
        
        selection = input(menu)

collections()