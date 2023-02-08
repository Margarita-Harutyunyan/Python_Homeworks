x=[[1,2,3,4],
   [5,6,7,8],
   [9,10,11,12],
   [13,14,15,16]]

ls = [[x[i][j] for i in range(len(x))] for j in range(len(x))]
for row in ls:
    print(row)
