#1:Gets five numbers and joins them with a plus sign
i = 0
string = ''
while i < 5:
    n = input('Enter a number: ')
    string += n + '+'
    i += 1
string = string[:-1]
print(string)

#3:Finds all palindromic numbers between 100 and 1000
def is_palindrome(n):
    rev = 0
    tmp = n
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10
    return tmp == rev

ls = [i for i in range(100, 1000) if is_palindrome(i)]
print(ls)

#4:Uses a list comp to find the gaps between consecutive entries
L = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
G = [(L[i+1] - L[i]) for i in range(len(L) - 1)]
print(f'The list of gaps: {G}')

max = G[0]
count = 0
for g in G:
    if max < g:
        max = g
    if g == 2:
        count += 1
percent = (count / len(G)) * 100
print(f'Maximum gap size: {max}')
print(f'Percentage of gaps with size 2: {round(percent, 2)} %') 

#5:Returns product prices according to names
def names_and_prices():
    d = {}
    while True:
        name = input('Enter a product name: ')
        price = input('Enter the price: ')
        d.update({name : price})
        if name == '' or price == '': break
    while True:
        Name = input('Enter a product name to know the price: ')
        keys = d.keys()
        if Name in keys:
            print(f'The price is {d[Name]}')
        else:
            print('The product is not available')
        if Name == '': break
    return -1

#6:Checks a dictionary
di = [{'name':'Todd', 'phone':'555-1414', 'email':'todd@mail.net'}, 
      {'name':'Helga', 'phone':'555-1618', 'email':'helga@mail.net'},
      {'name':'Princess', 'phone':'555-3141', 'email':''}, 
      {'name':'LJ', 'phone':'555-2718', 'email':'lj@mail.net'}]

def dict_check(d):
    numbers = [d[i]['name'] for i in range(len(d)) if d[i]['phone'][-1] == '8']
    emails = [d[i]['name'] for i in range(len(d)) if d[i]['email'] == '']
    print(f'The users whose phone number ends in an 8: {numbers}')
    print(f'The users who do not have an email address: {emails}')
dict_check(di) 
