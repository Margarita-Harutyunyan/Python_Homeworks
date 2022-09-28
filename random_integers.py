import random
def random_integers(num, start, end):
    '''Prints a given number of random integers,
        each between the given range'''
    for i in range(num):
        r = random.randint(start, end)
        print(r)
random_integers(50, 3, 6)
