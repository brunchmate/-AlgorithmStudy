# https://www.acmicpc.net/problem/1507
import sys

input = sys.stdin.readline


def floyd_warshall():
    for i in range(N):
        for j in range(i + 1, N):
            tmp = 1e9
            x = 0
            for k in range(N):
                if i == k or j == k:
                    continue
                if tmp > board[i][k] + board[k][j]:
                    tmp = board[i][k] + board[k][j]
                    x = k
            if tmp < board[i][j]:
                return False
            elif tmp > board[i][j]:
                road[i][j] = j
            elif tmp == board[i][j]:
                road[i][j] = x
    return True


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
road = [[0] * N for _ in range(N)]
ans = 0
if floyd_warshall():
    for a in range(N):
        for b in range(a + 1, N):
            if road[a][b] == b:
                ans += board[a][b]
    print(ans)
else:
    print(-1)

'''
마지막으로 거쳐 가는 점을 찾는다->거쳐 가는 점이 도착지점과 같으면 시작점과 도착점을 잇는 도로가 존재한다.
플로이드 와샬 알고리즘을 역으로 이용 -> 각각의 거쳐가는 지점을 찾기
- 각각의 점들을 거쳐가면서 나오는 최소값보다 주어진 값이 큰 경우는 존재할 수 없다.(모든 쌍의 최솟값이므로)
- 각각의 점들의 최소값과 현재 주어진 값들을 비교해서 만약 주어진 값이 작으면 시작점과 도착점을 바로 잇는 도로가 존재함을 알 수 있다.
- 만약 같은 경우에는 잇는 경우를 선택하는 것이 유리
    도로의 개수가 최소가 되려면 일단 a->b가 있을때 a->k, k->b인 도로가 존재 하면 (a,k),(b,k),(a,b)가 연달아서 해결되므로 도로 2개만 필요.
    하지만 (a,b)라고 하면 또 (a,k)일때 도로가 1개나 2개가 생기고, (b,k)일때 도로가 1개나 2개가 새로 생긴다. -> 최소3개에서 5개의 도로가 필요
'''