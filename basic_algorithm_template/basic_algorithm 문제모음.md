## dfs-backtracking // recursion

15649 n과m

## 이진탐색

10816 숫자 카드 2

## Tree

1967 트리의 지름 ( == 1167 )

## Graph, dfs, bfs

16947 서울 지하철 2호선

## Floyd-Warshall

11404 플로이드

## Dijstra

1753 최단경로

## dp

2293 동전 1, 동전 시리즈,  **12865 평범한 배낭
9251 LCS

## greedy

1931 회의실 배정 => pair<int,int> sort compare function

5397 키로거: deque 2개를 이어서 리스트 하나를 사용할 때보다 시간복잡도 개선

리스트 중간을 건드리면서 시간복잡도 개선이 필요할 때

이차원배열의 최댓값/최솟값 구하기 -> map 사용 max(map(max,dp))


deque | idx | deque

입출력 개선

import sys

input = sys.stdin.readline

sys.stdout.write() #'\n' 
\n\n

bfs 탐색 -> 빈칸을 탐색하여 넓이 파악하기 -> 벽부수기 4

리스트 2개 원소끼리 더하기 dp = [a+b-1 for a,b in zip(dp1,dp2)]
