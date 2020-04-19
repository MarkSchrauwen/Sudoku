sudoku = [[8,0,7,0,6,3,0,0,0],[0,1,0,0,2,0,0,0,8],[0,0,0,7,4,0,9,0,6],[0,3,0,0,0,0,0,0,0],[6,0,0,5,0,0,0,0,0],[0,0,8,0,0,0,0,3,1],[0,0,0,0,0,2,0,5,0],[0,4,0,0,0,0,0,0,9],[3,8,0,0,0,0,4,0,0]]

def find_empty(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row,col
    return None

def check(board,num,pos):
    # horizontal
    for col in range(9): #horizontal check
        if board[pos[0]][col] == num and col != pos[1]:
            return False
        else:
            for row in range(9): # vertical check
                if board[row][pos[1]] == num and row != pos[0]:
                    return False
                else: # check in square
                    srow = pos[0]//3
                    scol = pos[1]//3
                    for i in range(srow*3,srow*3+3):
                        for j in range(scol*3,scol*3+3):
                            if board[i][j] == num and not (i == srow and j == scol):
                                return False
    return True

def solve(board):
    if not find_empty(board):
        return True
    else:
        pos = find_empty(board)
        for num in range(1,10):
            if check(board,num, pos):
                board[pos[0]][pos[1]]= num
                if solve(board):
                    return True
                board[pos[0]][pos[1]] = 0
        return False

solve(sudoku)
for i in range(9):
    print (sudoku[i])
