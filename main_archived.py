from commons import *

class Board:
    def __init__(self, size, board):
        self.size = size
        self.board = []
        for i in range(size):
            self.board.append([])
            for j in range(size):
                self.board[i].append(board[i * size + j])


class Board:

    def __init__(self, board, blank = -1):
        self.blank = blank
        if blank < 0:
            for i in range(size):
                for j in range(size):
                    if board[i][j] == 0:
                        self.blank = i*size + j
                        break
        self.board = board

    def bfs(self):
        pass

    def astar(self):
        pass
    
    
