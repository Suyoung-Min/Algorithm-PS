import sys
import heapq

str1 = sys.stdin.readline().rstrip() #input 빠르게 받기

heap=[]
heapq.heappush(heap,10)
heapq.heappush(heap,1)
heapq.heappush(heap,3)
heapq.heappush(heap,4)
print(heap)
print(heapq.heappop(heap))
"""
min-heap library heapq
target 은 list 형태로 저장
"""
