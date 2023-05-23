print("\nWelcome to the Prime Number Finder.\n")

min_range = input("Please enter a minimum range of integers: ")
min_range = int(min_range)
max_range = input("Please enter a maximum range of integers: ")
max_range = int(max_range)

for i in range(min_range, max_range):
    for n in range(2, i):
        if i % n == 0:
            print(f"{i} is not a prime number; {i} equals {n} * {i//n}")
            break
    else:
        print(f"{i} is a prime number.")