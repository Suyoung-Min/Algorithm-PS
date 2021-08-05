arr=[int(input()) for _ in range(9)]
diff = sum(arr)-100
flag = False
for i in range(8):
    for j in range(i+1,9):
        if arr[i]+arr[j]==diff:
            del arr[j]
            del arr[i]
            flag = True
            break
    if flag:
        break
print(*arr,sep='\n')

"""
이중 for문 break 할 때 break 두 번 써야하므로 flag 설정 필수
"""
