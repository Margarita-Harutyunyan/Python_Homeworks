def is_leap(y):
    '''Checks if the given year is a leap year or not'''
    if (y % 4 == 0) and (y % 100 != 0) or (y % 400 == 0):
        return True
    return False

def how_many_leaps():
    '''Determines how many leap years there 
        have been between 1600 and a given year'''
    n = int(input('Enter a year here: '))
    count = 0
    if n < 1600:
        r = range(n, 1601)
    else:
        r = range(1600, n + 1)
    for i in r:
        if is_leap(i):
            count += 1
    print(count)
