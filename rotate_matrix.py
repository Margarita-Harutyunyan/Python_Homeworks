x=[[1,2,3,4],
   [5,6,7,8],
   [9,10,11,12],
   [13,14,15,16]]

ls = [[x[i][j] for j in range(len(x[0])-1, -1, -1)] for i in range(len(x)-1, -1, -1)]
for row in ls:
    print(row)
