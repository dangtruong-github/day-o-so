import copy
import time
import sys

orig_stdout = sys.stdout
f = open('out.txt', 'w')
sys.stdout = f
start = time.time()

N = [1, 0]
E = [0, -1]
W = [0, 1]
S = [-1, 0]
MOVES = {"N": N, "E": E, "W": W, "S": S}
INF = 1000000

SIZE = 3
SIZE_SQUARED = SIZE ** 2
FINAL_STATE = tuple(range(SIZE_SQUARED))
start_board = tuple([8, 7, 6, 5, 4, 3, 2, 1, 0])

state = {}
queue = []

def heuristic(board):
    val = 0
    for i in range(SIZE_SQUARED):
        val += abs((int)(i / SIZE) - (int)(board[i] / SIZE)) + abs((int)(i % SIZE) - (int)(board[i] % SIZE)) 
    return val

def checkEnd(board):
    return tuple(board) == FINAL_STATE

def swap(board, fromPos, toPos):
    board = list(board)
    board[fromPos], board[toPos] = board[toPos], board[fromPos]
    return tuple(board)

def show(board):
    print("************")
    for i in range(SIZE):
        for j in range(SIZE):
            print(board[i * SIZE + j], end = " ")
        print()
    print("************")

def bfs():
    queue.append(start_board)
    state[start_board] = ""
    board = start_board

    while len(queue) > 0 and board != FINAL_STATE:
        board = queue.pop(0)
        
        blank = -1

        # find blank position
        for i in range(SIZE_SQUARED):
            if board[i] == 0:
                blank = i
                break
    
        for sign, move in MOVES.items():
            new_blank = [(int)(blank / SIZE) + move[0], (int)(blank % SIZE) + move[1]]

            # out of bounds
            if new_blank[0] < 0 or new_blank[0] >= SIZE or new_blank[1] < 0 or new_blank[1] >= SIZE:
                continue

            new_board = swap(board, blank, blank + move[0] * SIZE + move[1])

            # visited
            if state.get(new_board) == None:
                queue.append(new_board)
                state[new_board] = state[board] + sign

        #value = len(state[tuple(board)])
        #print(value, state[tuple(board)], board)
    
    print(len(state[board]), state[board], board)
   
def astar():
    queue.append(start_board)
    state[start_board] = ""
    board = start_board

    while len(queue) > 0 and board != FINAL_STATE:
        board = queue.pop(0)
        
        blank = -1

        # find blank position
        for i in range(SIZE_SQUARED):
            if board[i] == 0:
                blank = i
                break
        
        min_heuristic = INF
        min_board = []
    
        for sign, move in MOVES.items():
            new_blank = [(int)(blank / SIZE) + move[0], (int)(blank % SIZE) + move[1]]

            # out of bounds
            if new_blank[0] < 0 or new_blank[0] >= SIZE or new_blank[1] < 0 or new_blank[1] >= SIZE:
                continue

            new_board = swap(board, blank, blank + move[0] * SIZE + move[1])

            # visited
            if state.get(new_board) == None:
                state[new_board] = state[board] + sign
                heuristic_new_board = heuristic(new_board)
                if heuristic_new_board <= min_heuristic:
                    min_heuristic = heuristic_new_board
                    if heuristic_new_board < min_heuristic:
                        min_board.clear()
                    min_board.append(new_board)

        for append_board in min_board:
            queue.append(append_board)
            #print(len(state[append_board]), state[append_board], heuristic_new_board, show(append_board))
        #value = len(state[tuple(board)])
        #print(value, state[tuple(board)], board)
    
    print(len(state[board]), state[board], board)

astar()
end = time.time()
print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")

sys.stdout = orig_stdout
f.close()