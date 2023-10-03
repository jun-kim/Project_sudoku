#print_menu is supposed to print menu for the user. This is totally wrong use of the function.

def print_menu(sudoku):
  return 0

#instruction: Follow the instruction. You haven't done anything I put here. You just copy pasted other's code. Follow the instruction.
def read(sudoku): # turns sudoku readable (into rows)
  final = []
  counter = 9
  for num in sudoku.replace(" ",""):
    if counter == 9:
      final.append([])
      counter = 0
    final[-1].append(num)
    counter += 1
  # after tests implement if statement to measure length of final
  return final

# 3
def change(x,y,n,sudoku):
  newsudoku = read(sudoku)
  newsudoku[y][x] = n
  return newsudoku

def findnextcell(sudoku,x,y):
  pass # define this to find the next cell we need to solve in the sudoku

def valid(sudoku,x,y,num):
  rows = []
  columns = []
  boxes = []
  pass # define this to see if the sudoku is valid by collecting rows columns and boxes 

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

# 2
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

# 1
sudoku = input("SUDOKU\nInput conditions:\n1) Start from the top left cell, moving right\n2) Use a space to represent the end of a row\n3) Indicate unknown values with a 0\nExample: 120456709 987600321...\nSudoku: ")
# use this sudoku format ^
"1) initial array - numbers with x for empty cell. ex) 1 12345678x"
"2) display the array. Ex) 2 then display 123 | 456 | 78x"
"3) enter a number in the array. Ex) 3 0 0 5. Then display will show 523 | 456 | 78x"

#who's calling print_menu?
def print_menu(cmd,sudoku):
  if cmd == "1":
    return format(sudoku)
  elif cmd == "2":
    return change(int(input("x: ")),int(input("y: ")),int(input("n: ")),sudoku)

def display(sudoku):
  counter = 3
  sudoku = read(sudoku)
  for row in sudoku:
    if counter == 3:
      print("----------------")
      counter = 0
    print("{}{}{} | {}{}{} | {}{}{}".format(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]))
    counter += 1
#where is user interaction?
#we need user interaction to update it dynamically
#this is a dynamic UI app that can update it whenever user inputs.

display(sudoku)
#instruction:
#1 . print the menu for sudoku user interface
#2 . print out a simple sudoku array. EX) 323 456 789
#                                         987 654 321 
#3 . change the array value using the menu. So use the menu to update a value. input 0 0 3 makes 1 -> 3
#4 . print menu prints updated sudoku array (regardless of correct or not)
