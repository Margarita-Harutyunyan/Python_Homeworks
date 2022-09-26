#This program prints an image on the screen
for row in range(9):
    for col in range(5):
        if (col == 0 or col == 4) and (row not in [1, 3, 5, 7]) or (row == 0 or row == 8) and (col > 0 and col < 5):
            print('*', end = '')
        else:
            print(end = ' ')
    print()
