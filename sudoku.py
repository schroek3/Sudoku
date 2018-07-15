#Ken Schroeder
#08.27.2016
#Hot summer day
#Home, 2225 SE 35th Pl
#Python Sudoku solver
#sudoku.py

'''
Sudoku Solver

How to use: 
	1. Create a CSV of Sudoku data, putting 0's in place of blanks
	2. From terminal, run python sudoku.py
	3. Voila!
Possible Improvements:
	1. A Sudoku puzzle creater?
	2. Allow a user to find the answer to one particular square, rather than all
	3. A little better UI, at the moment this is just a solver
'''

#*******************************************************************************
# imports
import csv
#******************************************************************************

# global variables
board = [[0 for x in range(9)] for y in range(9)]
quit = False
sudokuFile = "sudokuFile.txt"
#sudokuFile = "EasyTest.txt"
placements = 0

#*******************************************************************************
# functions

#------------------------------------------------------------------------------
# initializeBoard(File)
# takes a csv and turns it into the initial board
#------------------------------------------------------------------------------
def importBoard(sudokuFile):
	global board
	with open(sudokuFile,'rb') as f:
		reader = csv.reader(f)
		theRows = list(reader)
		for i in range(0,9):
			board[i] = map(int,theRows[i])
	f.close()
	print "Board Created."

#------------------------------------------------------------------------------
# printBoard(void)
# prints the board, putting in places every third row or column
#------------------------------------------------------------------------------
def printBoard():
	print "Printing board."
	# declare global board variable
	global board

	#place spacers at rows 3 and 6
	for r in range(0,9):
		if r in [3, 6]:
			print '------+-------+------'
		#place spacers at columns 3 and 6
		for c in range(0,9):
			if c in [3, 6]:
				print '|',
			printSquare(r,c)
		print

#------------------------------------------------------------------------------
# printSquare(int, int)
# prints value in the board at a particular row/column
#------------------------------------------------------------------------------
def printSquare(row,column):
	if(board[row][column] > 0):
		print board[row][column],
	else:
		print '.',

#------------------------------------------------------------------------------
# solve(row, column)
# recursively call function to solve the board
# place each number at a square, moving on to the next column
#------------------------------------------------------------------------------
def solve(row,col):
	#declare global variable board
	global board
	global placements
	#when you reach the end of a column, move back across like a typewriter
	if(col == 9):
		col = 0
		row += 1
		#if you've finished row 8, you've solved the puzzle!
		if(row == 9):
			return True
	#skip a square if a value is already in it
	if(board[row][col] != 0):
		placements += 1
		return solve(row,col+1)
	#try placing numbers, from 1-9
	for value in range (1,10):
		placements += 1
		if isLegal(row,col,value):
			board[row][col] = value
			if solve(row,col+1):
				return True
	#if you reach here, you've failed to place any number, so undo placements
	board[row][col] = 0
	return False

#------------------------------------------------------------------------------
# isLegal(int,int,int)
# checks if a placement of a value is legal
# checks rows, columns, boxes
#------------------------------------------------------------------------------
def isLegal(row,col,value):
	if not isLegalRow(row,col,value):
		return False
	if not isLegalCol(row,col,value):
		return False
	if not isLegalBox(row,col,value):
		return False
	return True
	
#------------------------------------------------------------------------------
# isLegalRow(int, int, int)
# determines if value is already in a row
#------------------------------------------------------------------------------
def isLegalRow(row,col,value):
		for i in range(0,9):
			if(board[i][col] == value):
				return False
		return True

#------------------------------------------------------------------------------
# isLegalCol(int, int, int)
# determines if value is already in a col
#------------------------------------------------------------------------------
def isLegalCol(row,col,value):
		for j in range(0,9):
			if(board[row][j] == value):
				return False
		return True

#------------------------------------------------------------------------------
# isLegalBox(int, int, int)
# determines if value is already in a box
#------------------------------------------------------------------------------
def isLegalBox(row,col,value):
	boxRowOffset = int(row/3) * 3
	boxColOffset = int(col/3) * 3
	for k in range(0,3):
		for m in range(0,3):
			if(value == board[boxRowOffset+k][boxColOffset+m]):
				return False
	return True


#*******************************************************************************
# main
importBoard(sudokuFile)
printBoard()
solve(0,0)
printBoard()
print "This puzzle took " + str(placements) + " moves."