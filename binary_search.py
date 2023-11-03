import random

def binarySearch(number, low, high):

    while low <= high:
        selection = low + (high - low) // 2

        if selection == number:
            return selection
        
        elif selection < number:
            low = selection + 1

        else:
            high = selection - 1

print(binarySearch(random.randint(1,500),1,500))