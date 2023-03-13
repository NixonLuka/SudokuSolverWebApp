import Board


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
    
    

def main():
    input = " "
    board = Board(input)
    
    solve(board)

if __name__ == "__main__":
    main()