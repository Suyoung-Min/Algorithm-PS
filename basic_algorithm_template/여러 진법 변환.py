fst_max= 0 ## target
if fst_max == 0:
    print(0)
else:
    system = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    answer = ''
    while fst_max != 0:
        answer += str(system[fst_max % 36]) #위치로 진법 변환
        fst_max //= 36

    print(answer[::-1])
############################## 타겟이 0일 때는 answer에 추가되지 않음으로 예외처리 필요


def decimal(target):
    ans=0
    for i in range(len(target)):
        if target[i].isdigit():
            ans+=int(target[i])*36**(len(target)-i-1)
        else:
            ans+=(ord(target[i]) - ord('A') + 10 )*36**(len(target)-i-1)
    return ans
################################ 36진법을 10진법으로 변환하는 함수
