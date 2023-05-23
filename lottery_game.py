import random

lottery_numbers = [random.randint(1,99) for _ in range(5)]
# print(lottery_numbers)        #inclued for testing purposes

who_player_one = input("Who is Player One: ")
who_player_two = input("Who is Player Two: ")
player_one_numbers = {random.randint(1,99) for _ in range(5)}
# print(player_one_numbers)     #inclued for testing purposes
player_two_numbers = {random.randint(1,99) for _ in range(5)}
# print(player_two_numbers)     #inclued for testing purposes

players = [
    {
        'name': who_player_one,
        'numbers': [player_one_numbers]
    },
    {
        'name': who_player_two,
        'numbers': [player_two_numbers]
    }
]


name_one = players[0]["name"]
numbers_one = player_one_numbers.intersection(lottery_numbers)
print(f"Player {name_one} has {len(numbers_one)} numbers matched.")
 
name_two = players[1]["name"]
numbers_two = player_two_numbers.intersection(lottery_numbers)
print(f"Player {name_two} has {len(numbers_two)} numbers matched.")