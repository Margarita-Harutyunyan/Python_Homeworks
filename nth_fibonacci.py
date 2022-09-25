def fibonacci():
    '''Takes n number as an input
    and prints the n-th Fibonacci number'''
    n = int(input('Enter a number here: '))
    p = 0
    q = 1
    i = 2
    lst = [p, q]
    while i <= n:
        fibo = p + q
        lst.append(fibo)
        p = q
        q = fibo
        i += 1
    print(lst[n])
