#Sudoku is a number-placement puzzle.
#The objective is to fill a 9 × 9 grid
#with numbers in such a way that each column,
#each row, and each of the nine 3 × 3 sub-grids
#that compose the grid all contain all
#of the numbers from 1 to 9 one time.

#Implement an algorithm that will check whether
#the given grid of numbers represents a valid
#Sudoku puzzle according to the layout rules
#described above. Note that the puzzle represented
#by grid does not have to be solvable.

def sudoku2(grid):
    n = len(grid)
    row = []
    column = []
    block = []

    for j in grid:
        for i in range(0,n):
          if j[i] != '.':
            row.append(j[i])
            row = sorted(row)
            for i in range(0,len(row)-1):
              if row[i] == row[i+1]:
                return False
        print ("row: " + str(row))
        row = []

    for k in range(0,9):
      for j in grid:
          for i in range(k,n):
            if j[i] != '.':
              column.append(j[i])
              column = sorted(column)
            break
      for i in range(0,len(column)-1):
              if column[i] == column[i+1]:
                return False
      print ("column: " + str(column))
      column = []

    for l in range(0,n,3):
      for k in range(0,n,3):
          for j in range(k,k+3):
            for i in range(l,l+3):
              if grid[j][i] != '.':
                block.append(grid[j][i])
                block = sorted(block)
          print ("block: " + str(block))
          for i in range(0,len(block)-1):
            if block[i] == block[i+1]:
              return False
          block = []
    return True
