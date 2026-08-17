def solve():
    import heapq

    '''
    명령
    100 - 초기화 
    200 - 선박 추가
    300 - 파워 교체
    400 - 공격
    '''
    T = int(input())
    powers, reload = dict(), dict()
    SBHeap = [] # 공격준비 Max Heap
    ReHeap = [] # 재장전 Min Heap
    reloadset = set()

    for t in range(T):
        cmd = list(map(int, input().split()))

        while ReHeap:
            endtime, id = heapq.heappop(ReHeap)

            if endtime <= t:
                # 리로드셋 에서 id 제거
                reloadset.remove(id)
                heapq.heappush(SBHeap, (-powers[id], id))
            else:
                heapq.heappush(ReHeap, (endtime, id))
                break

        # 초기화부터
        if cmd[0] == 100:
            for i in range(2, len(cmd), 3):
                id, p, r = cmd[i:i+3]

                powers[id], reload[id] = p, r
                heapq.heappush(SBHeap, (-p, id))

        elif cmd[0] == 200:
            id, p, r = cmd[1:]

            powers[id], reload[id] = p, r
            heapq.heappush(SBHeap, (-p, id))

        elif cmd[0] == 300:
            id, p = cmd[1:]

            powers[id] = p
            # 이미 재장전 시퀀스에 있다면 넣지 않는다
            if id not in reloadset:
                heapq.heappush(SBHeap, (-p, id))
        else: # 공격 명령!
            attack_ships = []
            damage_sum = 0
            # 공격횟수가 5회 아래거나 SBHeap 이 남아있으면
            while len(attack_ships) < 5 and SBHeap:
                p, id = heapq.heappop(SBHeap)

                # 함포 업데이트했는지 검증
                if powers[id] == -p:
                    # 기준 공격력 내림차순, id 오름차순 -> p 는 마이너스 그대로
                    attack_ships.append((p, id))
                    # 피해량 계산은 양수로
                    damage_sum -= p

                    # 공격한 배들은 바로 재장전 시퀀스
                    heapq.heappush(ReHeap, (t + reload[id], id))
                    # 재장전set 에 id 추가
                    reloadset.add(id)

            print(f"{damage_sum} {len(attack_ships)} {' '.join([str(x[1]) for x in attack_ships])}")


solve()