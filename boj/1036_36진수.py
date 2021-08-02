import sys
input = sys.stdin.readline

def decimal(target):
    ans=0
    for i in range(len(target)):
        if target[i].isdigit():
            ans+=int(target[i])*36**(len(target)-i-1)
        else:
            ans+=(ord(target[i]) - ord('A') + 10 )*36**(len(target)-i-1)
    return ans

n = int(input())
arr=[]
alphabet = [0]*36
for i in range(n):
    arr.append(input().rstrip())
k=int(input())

fst_max = 0
for i in arr:
    fst_max += decimal(i)

for i in range(36):
    target = chr(48+i) if i < 10 else chr(55+i)
    for j in arr:
        for t in range(len(j)):
            if j[t] == target:
                alphabet[i] += (35-i)*(36**(len(j)-t-1))
            
alphabet.sort(reverse=True)

for i in range(k):
    fst_max += alphabet[i]

if fst_max == 0:
    print(0)
else:
    system = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    answer = ''
    while fst_max != 0:
        answer += str(system[fst_max % 36]) #위치로 진법 변환
        fst_max //= 36

    print(answer[::-1])
