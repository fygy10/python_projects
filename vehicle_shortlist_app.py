vehicles = []

main_menu = ("\nWelcome to your Favorite Vehicle app. Please choose from one of the following options: " 
             "\n-Type 'add to add a vehicle\n-Type 'find' to find a vehicle on your list by category\n-Type 'review' to review your favorites and share.")


def add_vehicle():
    make_vehicle = input("Please enter make of the  vehicle: ")
    year_vehicle = input("Please enter year of the vehicle: ")
    type_vehicle = input("Please enter type of vehicle: ")
    cost_vehicle = input("Please enter cost of the vehicle: ")

    vehicles.append({

        'make_vehicle': make_vehicle,
        'year_vehicle': year_vehicle,
        'type_vehicle': type_vehicle,
        'cost_vehicle': cost_vehicle

    })

def review_vehicles():
    for vehicle in vehicles:
        print_vehicle(vehicle)


def print_vehicle(vehicle):
    print(f"The vehicle is a {vehicle['make_vehicle']}, the model is {vehicle['model']}, the cost is {vehicle['cost']}, and the year is {vehicle['year']}")


def find_vehicle():
    specific_category = input("Would you like to sort by cost, make, model, or year? ")
    for vehicle in vehicles:
        if specific_category == vehicles['cost']:
            print_vehicle(vehicle)            
        elif specific_category == vehicles['model']:
            print_vehicle(vehicle)
        elif specific_category == vehicles['year']:
            print_vehicle(vehicle)
        elif specific_category == vehicles['make']:
            print_vehicle(vehicle)

user_options = {

    'add': add_vehicle,
    'find': find_vehicle,
    'review': review_vehicles

}


def view_vehciles():
    selection = input(main_menu)

    while selection != "quit":
        if selection in user_options:
            selected_option = user_options[selection]
            selected_option()

        else:
            print("Please select a valid option")

        selection = input(main_menu)

view_vehciles()