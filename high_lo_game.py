low = 1
high = 1000

print("Please think of a number between {} and {}" .format(low, high))
input("Press Enter to start...")

guesses = 1

while low != high:
    guess = low + (high - low) // 2         # // is integer division
    high_low = input("My guess is {}, should I guess higher or lower? "
    "Enter 'higher', 'lower', or 'correct'. ".format(guess)).casefold()

    if high_low == "higher":
        low = guess + 1
    elif high_low == "lower":
        high = guess - 1
    elif high_low == "correct":
        print("I guessed correctly with {} guesses".format(guesses))
        break
    else:
        print("Please enter a correct option")
    
    guesses += 1 
else:
    print("You were thinking of the number {}".format(low))
    print("It took {} guesses" .format(guesses))