import sys
import heapq
import math
from collections import deque

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

print( math.ceil(12.2) ) # 13 올림
print( math.floor(12.2) ) # 12 내림
print( math.trunc(12.2) ) # 12 버림

print( round(0.4666 , 2) ) # 0.47 반올림 & 자릿수

"""
2021.8.4
Counting sort와 일반 sort들의 차이 
"""
