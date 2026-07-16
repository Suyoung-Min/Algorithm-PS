n, k = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.

chairs = [i for i in range(n+1)] # 0 ~ n

chairs_history = [set([i]) for i in range(n+1)]

for _ in range(3):
    for a, b in edges:

        chairs_history[chairs[a]].add(b) # 1번 사람의 기록에 b 번 자리 추가
        chairs_history[chairs[b]].add(a) # 2번 사람의 기록에 a 번 자리 추가

        chairs[a], chairs[b] = chairs[b], chairs[a] 
        # chairs[1] = 1, chairs[2] = 2 
        # 첫번째 의자에 1번 사람, 2번째 의자에 2번 사람
        # 위치 변경
for i in range(1, n+1):
    print(len(chairs_history[i]))