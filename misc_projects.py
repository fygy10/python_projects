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

answer = 5      #guessing game with if, elif, and else statements

print("Please guess a number between 1 and 10: ")
guess = int(input())

if guess < answer:
    print("Your guess is too low")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it.") 
    else:
        print("Sorry, you didn't guess it.")
elif guess == 5:
    print("Congrats, that is correct")
else:
    print("Sorry, that guess is too high")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it.")
    else:
        print("Sorry, you didn't guess it.")
          

if guess == answer:     #guess equals answer 
    print("Congratulations, that guess is correct")
else:           #all other possibilities
    if guess < answer:      #guess is too low prompt
        print("Sorry, that guess is too low")
    else:
        print("Please guess lower")     #guess is too high prompt
    guess = int(input())        #offers a second chance to guess
    if guess == answer:     #prompt is second guess is correct
        print("Well done, you guessed it.")
    else:
        print("Sorry, you didn't guess it.")    #prompt if second guess is still wrong


