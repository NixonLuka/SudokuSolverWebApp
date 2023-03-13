import sys

class Board():

    def __init__(self, input):
        input.strip()
        if (len(input) != 81):
            sys.exit("Error in input, board does not have 81 values")

        self.board = []

        for i in range(0,9):
            row = input[i*9:(i+1)*9]
            self.board.append(row)

    def getValue(self,rowIndex, columnIndex):
        return self.board[rowIndex][columnIndex]

    def setValue(self, value, rowIndex, columnIndex):
        self.board[rowIndex][columnIndex] = value

    def isValidMove(self,value, rowIndex, columnIndex):
        return (self.validRow(rowIndex,value) and self.validColumn(columnIndex,value) and self.validSquare(rowIndex,columnIndex,value))

    def validRow(self, rowIndex, value):  
        return (self.board[rowIndex].count(value) == 1)

    def validColumn(self, columnIndex, value):
        column = []
        for i in range(0,9):
            column.append(self.board[i][columnIndex])
        return column.count(value) == 1

    #use indeces to find which square its in, add all values of the square to a list, and check that the value occurs once
    def validSquare(self, rowIndex, columnIndex,value):
        square = []
        rowLowerBound = rowIndex - (rowIndex % 3)
        columnLowerBound = columnIndex - (columnIndex % 3)
        for i in range(rowLowerBound, rowLowerBound+3):
            for j in range(columnLowerBound, columnLowerBound+3):
                square.append(self.board[i][j])
        return square.count(value) == 1
        
