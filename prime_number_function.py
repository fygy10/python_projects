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


#updated prime number function with a generator function
def prime_generator(bound):
    for n in range(2, bound):   # n starts from 2 to bound
        for i in range(2, n):   # check if there is a number x (1<x<n) that can divide n
            if n % i == 0:  # as long as we can find any such x, then n is not prime
                break
        else:   # if no such x is found after exhausting all 1<x<n
            yield n     # generate this prime

g = prime_generator(10)


#prime number class generator
class PrimeGenerator:
    def __init__(self, stop):
        self.stop = stop
        self.start = 2
 
    def __next__(self):
        for n in range(self.start, self.stop):  # always search from current start (inclusive) to stop (exclusive)
            for x in range(2, n):
                if n % x == 0:      # not prime
                    break
            else:   # n is prime, because we've gone through the entire loop without having a non-prime situation
                self.start = n + 1  # next time we need to start from n + 1, otherwise we will be trapped on n
                return n    # return n for this round
        raise StopIteration()  # this is what tells Python we've reached the end of the generator