# 나이트의 이동
# 매 칸마다 나이트가 이동할 수 있는 경우는 최대 8가지의 경우
# 8 가지의 경우중, 하나를 선택해서 이동했을 때, 
# 1. dfs -> 해당 칸에서 또 이동할 수 있는 경우들을 탐색 -> 무한 탐색 (비적절)
# 2. bfs -> 나머지 7가지의 경우들을 다시 탐색 (적절)

# 나이트가 이동할 수 있는 0 ~ l-1 사이의 위치 
def knight_move(r, c, l, moves, visited):
    can_moves = [
        [r-1, c-2], [r-2, c-1], [r-1, c+2], [r-2, c+1],
        [r+1, c-2], [r+2, c-1], [r+1, c+2], [r+2, c+1]
    ]
    for m in can_moves:
        nr, nc = m
        if 0 <= nr < l and 0 <= nc < l and not visited[nr][nc]:
            visited[nr][nc] = True
            moves.append([nr, nc])

def checking(curpoint, endpoint):
    return curpoint[0] == endpoint[0] and curpoint[1] == endpoint[1]

def bfs(l, points, end_point, count, visited):
    moves = []
    for cur_point in points:
        knight_move(cur_point[0], cur_point[1], l, moves, visited)

    for move in moves:
        if checking(move, end_point):
            return count

    return bfs(l, moves, end_point, count+1, visited)

T = int(input())

for test_case in range(T):
    I = int(input())
    cur_r, cur_c = map(int, input().split())
    end_r, end_c = map(int, input().split())
    result = 0

    if (cur_r == end_r) and (cur_c == end_c):
        result = 0
    else:
        visited = [[False] * I for _ in range(I)]
        visited[cur_r][cur_c] = True  # 시작점 방문 처리
        result = bfs(I, [[cur_r, cur_c]], [end_r, end_c], 1, visited)

    print(result)
