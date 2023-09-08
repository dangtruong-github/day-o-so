import copy
import time

start = time.time()

N = [1, 0]
E = [0, -1]
W = [0, 1]
S = [-1, 0]
MOVES = {"N": N, "E": E, "W": W, "S": S}
INF = 1000000

size = 3
start_board = [[8, 7, 6],
               [5, 4, 3],
               [2, 1, 0]]

state = {}
queue = []

def heuristic(board):
    val = 0
    for i in range(size):
        for j in range(size):
            val += abs(i - (int)(board[i][j] / size)) + abs(j - (int)(board[i][j] % size)) 
    return val

def boardToString(board):
    toString = ""
    for i in range(size):
        for j in range(size):
            toString += chr(board[i][j] + ord('0'))
    return toString

def stringToBoard(str):
    board = []
    for i in range(size):
        board.append([])
        for j in range(size):
            board[i].append(ord(str[i * size + j]) - ord('0'))
    return board

def checkEnd(board):
    for i in range(size):
        for j in range(size):
            if board[i][j] != i * size + j:
                return False
    return True

def bfs():
    queue.append(start_board)
    state[boardToString(start_board)] = ""

    while(len(queue) > 0):
        board = queue.pop(0)
            
        string_board = boardToString(board)
        
        blank = [-1, -1]

        # find blank position
        for i in range(size):
            for j in range(size):
                if board[i][j] == 0:
                    blank = [i, j]
                    break
        
        for sign, move in MOVES.items():
            new_blank = [blank[0] + move[0], blank[1] + move[1]]


            # out of bounds
            if new_blank[0] < 0 or new_blank[0] >= size or new_blank[1] < 0 or new_blank[1] >= size:
                continue

            new_board = copy.deepcopy(board)
            new_board[blank[0]][blank[1]] = new_board[new_blank[0]][new_blank[1]]
            new_board[new_blank[0]][new_blank[1]] = 0

            # visited
            string_new_board = boardToString(new_board)
            if string_new_board in state.keys():
                continue

            queue.append(new_board)
            state[string_new_board] = state[string_board] + sign

        value = len(state[string_board])
        if checkEnd(board):
            print(value, state[string_board])
            break
        print(value, state[string_board], board)
    
def astar():
    
    queue.append(start_board)
    state[boardToString(start_board)] = ""

    while(len(queue) > 0):
        board = queue.pop(0)
            
        string_board = boardToString(board)
        
        blank = [-1, -1]

        # find blank position
        for i in range(size):
            for j in range(size):
                if board[i][j] == 0:
                    blank = [i, j]
                    break

        min_heuristic = INF
        min_board = []
        
        for sign, move in MOVES.items():
            new_blank = [blank[0] + move[0], blank[1] + move[1]]

            # out of bounds
            if new_blank[0] < 0 or new_blank[0] >= size or new_blank[1] < 0 or new_blank[1] >= size:
                continue

            new_board = copy.deepcopy(board)
            new_board[blank[0]][blank[1]] = new_board[new_blank[0]][new_blank[1]]
            new_board[new_blank[0]][new_blank[1]] = 0

            # visited
            string_new_board = boardToString(new_board)
            if string_new_board in state.keys():
                continue

            heuristic_new_board = heuristic(new_board)
            if heuristic_new_board <= min_heuristic:
                min_heuristic = heuristic_new_board
                if heuristic_new_board < min_heuristic:
                    min_board.clear()
                min_board.append(new_board)

            state[string_new_board] = state[string_board] + sign

        for append_board in min_board:
            queue.append(append_board)

        value = len(state[string_board])
        if checkEnd(board):
            print(value, state[string_board])
            break
        print(value, state[string_board], board)

astar()
end = time.time()
print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")