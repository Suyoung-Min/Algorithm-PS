board=[None]*8
for i in range(8):
   board[i]=input()
a=0
for i in range(8):
   for j in range(i%2,8,2):
      if (i+j)%2 == 0 and board[i][j] == 'F':
         a+=1
print(a)
