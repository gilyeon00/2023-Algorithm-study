import sys
from collections import defaultdict

input = sys.stdin.readline
N = int(input())

arr = [ [0] * N for _ in range(N) ]
likedict = defaultdict(list)
result = 0
 
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for _ in range(N*N):
    _input = list(map(int, input().split()))
    likedict[_input[0]] = _input[1:]
    
    max_x = 0
    max_y = 0
    max_like = -1
    max_empty = -1
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                likecnt = 0
                emptycnt = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < N and 0 <= ny < N:
                        if arr[nx][ny] in _input:
                            likecnt += 1
                        if arr[nx][ny] == 0:
                            emptycnt += 1
                            
                if max_like < likecnt or (max_like == likecnt and max_empty < emptycnt):
                    max_x = i
                    max_y = j
                    max_like = likecnt
                    max_empty = emptycnt
                    
    arr[max_x][max_y] = _input[0]
    
for i in range(N):
    for j in range(N):
        cnt = 0
        likes = likedict[arr[i][j]]
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] in likes:
                    cnt += 1
        if cnt != 0:
            result += 10 ** (cnt - 1)
            
print(result)