def even_or_odd():
    '''Takes a number input, 
        checks and prints whether
        the number is even or odd'''
    while True:
        n = input('Enter a number here: ')
        if n == 'stop': break
        try:
            num = int(n)
        except:
            print('You did not enter a number correctly')
        else:
            if num % 2 == 0:
                print(f'{num} is an even number')
            else:
                print(f'{num} is an odd number')
