import sys
# input = sys.stdin.readline
# import heapq

# for _ in range(int(input())):
#     m = int(input())
#     maxq = []
#     minq = []
#     q = [True]*m
#     for i in range(m):
#         command = input().split()

#         if command[0] == 'I':
#             heapq.heappush(maxq,(int(command[1]),i))
#             heapq.heappush(minq,(-int(command[1]),i))
#         elif command[0] == 'D' and command[1] == '-1':
#             if len(minq) and q[maxq[0][1]]:
#                 heapq.heappop(maxq)
#                 q[maxq[0][1]] = False
#         else:
#             if len(maxq) and q[minq[0][1]]:
#                 heapq.heappop(minq)
#                 q[minq[0][1]] = False

#     ans = 0
#     if len(q):
#         maxq = list(maxq)
#         print(maxq[-1],' ',maxq[0])
#     else:
#         print('EMPTY')
