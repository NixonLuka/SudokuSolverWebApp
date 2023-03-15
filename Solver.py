from Board import Board

#Back Tracking algorithm
def solve(board, rowIndex, columnIndex):
    
    if rowIndex == 9:
        return True
    elif columnIndex == 9:
        return solve(board, rowIndex + 1, 0)
    elif (board.getValue(rowIndex, columnIndex)):     
        return solve(board, rowIndex, columnIndex+1)
    else:
        for value in range(1,10):
            board.setValue(value,rowIndex,columnIndex)
            if(board.isValidMove(value, rowIndex, columnIndex)):
                if solve(board, rowIndex, columnIndex+1): #was solution
                    return True
                else:
                    continue
            else:
                continue
        #if back tracking, we must reset the current value
        board.setValue(0,rowIndex,columnIndex)

        return False
    
def solveCaller(board):
    if (solve(board,0,0)):
        print("Board is solved:")
        board.printBoard()
    else:
        print("The following board is unsolvable:")
        board.printBoard()

def main():
    input = "0 0 0 0 0 1 0 0 0 \
             3 0 0 0 0 7 5 0 2\
             4 0 0 0 5 0 1 9 0\
             0 3 0 5 8 0 0 2 0\
             0 0 8 0 0 0 7 0 0\
             0 1 0 0 9 6 0 3 0\
             0 8 3 0 7 0 0 0 6\
             1 0 7 6 0 0 0 0 4\
             0 0 0 2 0 0 0 0 0"
    board = Board(input)
    solveCaller(board)

if __name__ == "__main__":
    main()