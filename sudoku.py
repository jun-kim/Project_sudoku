def print_menu(sudoku):
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

def grab(sudoku):
  rows = []
  columns = []
  boxes = []
  return rows

print("sudoku is here")

sudoku = input("Sudoku (mark unknown with X): ")
print(grab("12345678"))

#instruction:
#1 . print the menu for sudoku user interface
#2 . print out a simple sudoku array. EX) 323 456 789
#                                         987 654 321 
#3 . change the array value using the menu. So use the menu to update a value. input 0 0 3 makes 1 -> 3
#4 . print menu prints updated sudoku array (regardless of correct or not)

print(change(int(input("x:")),int(input("y:")),input("n:"),input("sudoku:")))
