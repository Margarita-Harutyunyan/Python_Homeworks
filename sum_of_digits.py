def sum_of_digits():
    '''Takes a number as an input
        and prints the sum of its digits'''
    n = input('Enter an ineger number here: ')
    sum = 0
    try:
        num = int(n)
    except:
        print('You did not enter an integer number')
    else:
        while num > 1:
            digit = num % 10
            sum += digit
            num //= 10
        print(sum)
sum_of_digits()
