import sys
import heapq

str1 = sys.stdin.readline().rstrip() #input 빠르게 str 받기 & 개행문자 제거 
list1 = map(int,sys.stdin.readline().split()) # 여러개 정수를 리스트로 받기

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
