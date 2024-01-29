from random import randint, shuffle, choice
def check_num_can_be_fill(sdk,row,col,num):
    """ this method check weather given number can be filled in particuler position in sudoku
    by checking row, column, and 3*3 matrix of sudoku if number is not alreay present
    then return True else return False."""
    #check number is not present in particuler row
    for x in range(9):
        if sdk[row][x] == num:
            return False
    #check number is not present in particuler column
    for x in range(9):
        if sdk[x][col] == num:
            return False
    #check number is not present in particuler 3*3 matrix
    startRow = row - row%3
    startCol = col - col%3
    for i in range(3):
        for j in range(3):
            if sdk[i+startRow][j+startCol] == num:
                return False
    return True

def fill_sudoku(sdk,row=0,col=0):
    #below conditions are for continue to fill numbers to sudoku
    if row == 9-1 and col == 9:
        return True
    if col == 9:
        row += 1
        col = 0
    if sdk[row][col] > 0:   #check box is alread filled if then go next box 
        return fill_sudoku(sdk,row,col+1)
    for num in range(1,9+1,1):
        if check_num_can_be_fill(sdk,row,col,num):
            sdk[row][col] = num
            if fill_sudoku(sdk,row,col+1):
                return True
        sdk[row][col] = 0
    return False
    
def create_empty_sudoku():
    """this function will create sudoku of 9*9 with default value to each box is '0' and
    any one random row (with shuffle number from 1 to 9 filled) it will help to
    create a random sudoku"""

    numbers = [1,2,3,4,5,6,7,8,9]
    rand_row = randint(0,8)
    shuffle(numbers)
    sdk = [[0 for i in range(9)] for j in range(9)]
    sdk[rand_row] = numbers
    return sdk

def create_sudoku_puzle(sdk):
    """this function will remove random postions from solved sudoku and generate sudoku game.
    minimum at least 18 number shuold be filled in any sudoku to be have a solution"""

    n = randint(25,35)  #number of boxes at least filled randomly(25,35)
    not_remove_boxes = []
    indexes = []
    for i in range(9):
        for j in range(9):
            indexes.append((i,j))
            
    while len(not_remove_boxes)<=n:
        num = choice(indexes)
        if num not in not_remove_boxes:
            not_remove_boxes.append(num)

    sdk_board = [[0 for i in range(9)] for j in range(9)]
    for r,c in not_remove_boxes:
        sdk_board[r][c] = sdk[r][c]

    return sdk_board