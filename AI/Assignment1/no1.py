from queue import Queue

# Check if path is valid
def valid(n, maze, x, y, visited):
    return x >= 0 and y >= 0 and x < n and y < n and maze[x][y] == 1 and not visited[x][y]

# BFS Algorithm to find a path
def BFSpathfind(maze, start, finish):
    length = len(maze)
    visited = [[False for _ in range(length)] for _ in range(length)]

    # Define move by coordinate index (up, down, left, right)
    moveX = [-1, 1, 0, 0]
    moveY = [0, 0, -1, 1]

    # Create queue for BFS
    queue = Queue()
    queue.put(start)

    # Store the path
    path = {}
    found = False

    while not queue.empty():
        current = queue.get()
        x, y = current

        if current == finish:
            found = True
            break

        for i in range(4):
            movex = x + moveX[i]
            movey = y + moveY[i]

            if valid(length, maze, movex, movey, visited):
                queue.put((movex, movey))
                visited[movex][movey] = True
                path[(movex, movey)] = current

    if found:
        x, y = finish
        while (x, y) != start:
            maze[x][y] = '|'
            # x, y = path[(x, y)]
            nx, ny = path[(x, y)]
            if nx == x: # horizontal movement
                maze[x][y] = '-'
            else: # vertical movement
                maze[x][y] = '|'
            x, y = nx, ny

        maze[start[0]][start[1]] = 'S'
        maze[finish[0]][finish[1]] = 'G'

        for row in maze:
            for cell in row:
                print(cell, end=' ')
            print()
    else:
        return "Path doesn't exist"



maze = [
    [1, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1]
]

s = (0, 0)
g = (2, 4)

BFSpathfind(maze, s, g)
