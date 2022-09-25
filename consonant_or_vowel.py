def consonant_or_vowel():
    '''Takes a character as an input,
        checks and prints
        whether the character is a vowel or a consonant'''
    c = input('Enter a character here: ')
    if len(c) > 1:
        print('Too many characters')
        return -1
    try:
        c = int(c)
    except:
        if c in ['a', 'e', 'i', 'o', 'u', 'y']:
            print(f'{c} is a vowel')
        else:
            print(f'{c} is a consonant')
    else:
        print('You entered a number')
