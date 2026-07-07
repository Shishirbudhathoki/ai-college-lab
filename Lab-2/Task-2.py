from heapq import heappush, heappop

goal = (
    (1,2,3),
    (4,5,6),
    (7,8,0)
)

start = (
    (5,8,2),
    (1,0,3),
    (4,7,6)
)

def misplaced_tile(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] !=0 and state[i][j] != goal[i][j]:
                count = count + 1
    return count

# Goal Positions for Manhattan Distance
goal_pos = {}
for i in range(3):
    for j in range(3):
        goal_pos[goal[i][j]] = (i, j)

# Manhattan Distance Heuristic (h2)
def manhattan_distance(state):
    distance = 0

    for i in range(3):
        for j in range(3):

            tile = state[i][j]

            if tile != 0:
                goal_i, goal_j = goal_pos[tile]
                distance += abs(i - goal_i) + abs(j - goal_j)

    return distance

# Combined Heuristic (h1 + h2)
def combined_heuristic(state):
    return misplaced_tile(state) + manhattan_distance(state)


def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i,j
            
def get_neighbors(state):
    x,y = find_blank(state)
    moves = [(-1,0),(1,0),(0,-1),(0,1)]

    neighbours = []
    for dx, dy in moves:
        nx = x + dx
        ny = y + dy
        if 0<= nx < 3 and 0 <= ny < 3:
            board = [list(row) for row in state]
            board[x][y], board[nx][ny] = board[nx][ny],board[x][y]
            neighbours.append(tuple(map(tuple,board)))
    return neighbours


def reconstruct(parent,current):
    path = []
    while current is not None:
        path.append(current)
        current=parent[current]
    return path[::-1]

def astar(start,heuristic):
    pq = []
    heappush(pq, (heuristic(start),0,start))
    parent = {start: None}
    g_cost = {start: 0}
    expanded = 0
    while pq:
        f,g,current = heappop(pq)
        expanded = expanded + 1
        if current == goal:
            return reconstruct(parent,current),expanded
        for neighbor in get_neighbors(current):
            new_g = g + 1
            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                f_cost = new_g + heuristic(neighbor)

                heappush(
                    pq,
                    (f_cost, new_g, neighbor)
                )
                parent[neighbor] = current
    return None, expanded


print("Using h3: Combined Heuristic (h1 + h2)\n")
path, expanded = astar(start, combined_heuristic)
if(path):
    for step in path:
        for row in step:
            print(row)
        print()

print("Moves =",len(path)-1) 
print("Nodes expaned = ",expanded)

