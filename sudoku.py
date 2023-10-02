#print_menu is supposed to print menu for the user. This is totally wrong use of the function.

def print_menu(sudoku): # turns 
  final = [[]]
  counter = 0
  for i in sudoku:
    if counter == 9:
      final.append([])
      counter = 0
    final[-1].append(i)
    counter += 1
  return final

def change(x,y,n,sudoku):
  newsudoku = print_menu(sudoku)
  newsudoku[y][x] = n
  return newsudoku

def findnextcell(sudoku,x,y):
  pass # define this to find the next cell we need to solve in the sudoku

def valid(sudoku,x,y,num):
  rows = []
  columns = []
  boxes = []
  pass # define this to see if the sudoku is valid by collecting rows columns and boxes 

#don't copy paste other's code. We are trying to make it from scratch. Not copy paste sudoku code.
def solve(sudoku, x=0, y=0): # x and y are coordinates; they start as zero, but they will change value as we work through the sudoku
  x,y = findnextcell(sudoku, x, y)
  if x == "correct":
    return True # the sudoku is solved
  for num in range(1,10):
    if valid(sudoku,x,y,num): # num is the guess
      sudoku[x][y] = num
      if solve(sudoku, x, y) is True: 
        return True # continue solving the rest of the sudoku
      else:
        sudoku[x][y] = 0 # undo the cell to try again with a new value
  return False

def format(sudoku): # sudoku variable is the solved sudoku which is a list of lists (rows)
  final = ""
  counter = 0
  for row in sudoku:
    for cell in row:
      if counter == 2:
        final += str(cell)+" " 
        counter = 0
      else:
        final += str(cell)
      counter += 1
    final = final[:-1]
    final += "\n"
  return final

def convert():
  pass # use this function to turn sudoku input into something readable by solve function

sudoku = input("SUDOKU\nInput conditions:\n1) Start from the top left cell, moving right\n2) Use a space to represent the end of a row\n3) Indicate unknown values with a 0\nExample: 120456709 987600321...\nSudoku: ")
# use this sudoku format ^

#instruction: Follow the instruction. You haven't done anything I put here. You just copy pasted other's code. Follow the instruction.
#1 . print the menu for sudoku user interface
#2 . print out a simple sudoku array. EX) 323 456 789
#                                         987 654 321 
#3 . change the array value using the menu. So use the menu to update a value. input 0 0 3 makes 1 -> 3
#4 . print menu prints updated sudoku array (regardless of correct or not)
