def solve():
    import heapq

    Q = int(input())

    fcmd = list(map(int, input().split()))

    N, M = fcmd[1], fcmd[2]
    farr = fcmd[3:]
    """
    상태관리 총 4개
    light - (id, L)
    left - (id, lid)
    right - (id, rid)
    Between-Max-Heap - (-Bi, 왼쪽좌표, lid, rid)
        -> Lazy Delete 적용, 꺼낼 때 right[lid] == rid 인지로 판단
        -> 왼쪽좌표를 2번째에 넣어 동점 시 좌표 작은 쌍이 먼저 나오게 함
    맨 왼쪽이면 id = 0, 맨 오른쪽 끝 id = -1 로 관리
    """

    """
    처음 입력일 때 id 범위 1 ~ M 오름차순
    """

    lpos = {i+1:farr[i] for i in range(len(farr))}
    lpos[0] = 0
    lpos[-1] = N

    left = {i:i-1 for i in range(1, M+1)}
    left[-1] = M

    right = {i:i+1 for i in range(M)}
    right[M] = -1

    BMHeap = [(-(lpos[i+1] - lpos[i]), lpos[i], i, i+1) for i in range(1, M)]

    heapq.heapify(BMHeap)

    lnum = M
    next_lid = M+1
    out = []

    for _ in range(Q-1):

        cmd = list(map(int, input().split()))

        # 가로등 추가
        if cmd[0] == 200:
            '''
            1. Heap 꼭대기를 꺼내지 말고 확인만
            2. right[lid] == rid 이면 유효, 아니면 pop - Lazy Delete
            3. 동점 처리는 튜플 2번째(왼쪽 좌표)가 대신 해준다
            4. 유효한 것을 찾으면 pop 하고 그 사이에 설치
            5. 나눠진 두 구간을 BMHeap 에 넣기
            '''

            slid, srid = None, None

            while BMHeap:
                Bi, lx, lid, rid = BMHeap[0]

                # 검증된 원소인지
                if right.get(lid) == rid:
                    slid, srid = lid, rid
                    heapq.heappop(BMHeap)   # 이 구간은 곧 둘로 쪼개짐
                    break

                heapq.heappop(BMHeap)

            if slid is None:    # 가로등이 1개 이하 (방어)
                continue

            right[slid] = next_lid
            left[srid] = next_lid
            lpos[next_lid] = -(-(lpos[slid] + lpos[srid]) // 2)
            right[next_lid] = srid
            left[next_lid] = slid

            heapq.heappush(BMHeap, (-(lpos[next_lid] - lpos[slid]), lpos[slid], slid, next_lid))
            heapq.heappush(BMHeap, (-(lpos[srid] - lpos[next_lid]), lpos[next_lid], next_lid, srid))

            next_lid += 1
            lnum += 1

        # 가로등 제거
        elif cmd[0] == 300:
            '''
            시간복잡도 - O( log n )
            딕셔너리 삭제 + 합쳐진 구간 push
            '''
            tid = cmd[1]

            tid_left = left[tid]
            tid_right = right[tid]

            right[tid_left] = tid_right
            left[tid_right] = tid_left

            del lpos[tid]
            del left[tid]
            del right[tid]

            # 두 간격이 하나로 합쳐짐 (끝 구간은 제외)
            if tid_left != 0 and tid_right != -1:
                heapq.heappush(BMHeap,
                    (-(lpos[tid_right] - lpos[tid_left]), lpos[tid_left], tid_left, tid_right))

            lnum -= 1

        # 최소 전력 계산
        else:
            '''
            시간복잡도 O( log n ) 분할상환
            답 = max( 왼쪽 끝 구간, 오른쪽 끝 구간, 가로등 사이 최대 간격 )
            끝 구간은 힙에 없으므로 센티넬 링크로 O(1) 조회
            '''

            first = right[0]  # 맨 왼쪽 가로등 id
            last = left[-1]   # 맨 오른쪽 가로등 id

            max_dist = max((lpos[first] - 1) * 2, (N - lpos[last]) * 2)

            # Lazy Delete - 유효한 최대 간격 확인 (꺼내지 않고 peek)
            while BMHeap:
                Bi, lx, lid, rid = BMHeap[0]

                # 검증된 원소인지
                if right.get(lid) == rid:
                    if -Bi > max_dist:
                        max_dist = -Bi
                    break

                heapq.heappop(BMHeap)

            out.append(max_dist)

    print("\n".join(map(str, out)))

solve()