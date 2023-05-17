import random

name = input("Please enter your name: ")    #name and age function with input from user that generates a rude output using int and if else statement
age = int(input("How old are you {0}? ".format(name)))

months = int(input("Can you guess how many months have 31 days? "))

if months != 7:
    print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6}, and {7}"
        .format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))   #multiple replacement fields within the string
else:
    print("Correct!")

s = "Strings are awesome!"
print("Length of s = %d" % len(s)) #length
print("The first occurrence of the letter a = %d" % s.index("a")) #an "a" at 8th character
print("a occurs %d times" % s.count("a")) # Number of a's should be 2
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end
print("String in uppercase: %s" % s.upper()) # Convert everything to uppercase
print("String in lowercase: %s" % s.lower()) # Convert everything to lowercase

shopping_list = ["milk", "eggs", "pasta", "bread", "cheese", "lettuce"]     #a list (sequence of items to sort through)

for item in shopping_list:      #for loop printing out items to buy from a list
    # if item != "milk":          #excludes milk from the list
    if item == "milk":
        continue   #continues code while skippping key word
        #break      #stops code
    print("Buy " + item)

#index list
item_to_find = "bread"     #what am I looking to find in a variable
found_at = None         #'if I find nothing' in a variable

if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)
if found_at is not None:
    print("The item is found at position '{}' on the list. " .format(found_at))
else:
    print("{} is not found on the list".format(item_to_find))

highest = 1000        #manually set an upper limit and attach it to a variable
answer = random.randint(1, highest)      #use of random number generator
# print(answer) #used only for testing
guess = 0       #initialize to any number entered
print("Please guess a number between 1 and {}: " .format(highest))

while guess != answer:     #while loop to allow for multiple guesses until the guess is correct (equals to the answer variable)
    guess = int(input())
    if guess == 0:
        print("Game terminated")
        break
    if guess == answer:
        print("Congratulations, that guess is correct")
    elif guess < answer:      #guess is too low prompt 
        print("Sorry, that guess is too low; please guess higher.")
    else:
        print("Sorry, that guess is too high; please guess lower.")