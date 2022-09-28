def all_divisors(num):
    '''Prints all the divisors of a number,
        not including the number itself'''
    ls = []
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            ls.append(i)
    return ls

def is_perfect(num):
    '''Checks if a number is perfect'''
    if sum(all_divisors(num)) == num:
        return True
    return False
  
def all_perfect_numbers(n):
    '''Finds all the perfect numbers 
        that are less than the given number'''
    ls = []
    for i in range(1, n):
        if is_perfect(i):
            ls.append(i)
    print(ls)
    
all_perfect_numbers(10000)
