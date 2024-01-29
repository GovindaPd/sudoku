import random
M = 9
#hint: you must leave at least 17 numbers for a 9x9 sudoku)
def fen_to_sdk(your_sdk):
    """this function convert user string representation of sudoku to 9*9 matrix
    of list represetation. like fen represetation of sudoku here 0 means not
    filled box and any other symbol(including space) means next row.
    fen => '945310144 134560001 945310144 134560001 945310144 134560001 945310144 134560001 945310144'
    """
    sdk = []
    row = []
    for i in your_sdk:
        if i in "0123456789":
            row.append(int(i)); 
        else:
            sdk.append(row)
            row = []
    return sdk;

def print_sdk(sdk):
    print("||=====|=====|=====||=====|=====|=====||=====|=====|=====||");
    for indx, r in enumerate(sdk,1):
        print("||",end="")
        for i, c in enumerate(r,1):
            print(" ",c," ",end="")
            if i%3 == 0:
                print("||",end='')
            else:
                print("|",end='')
            if i%9 == 0:
                print()
                print("||-----|-----|-----||-----|-----|-----||-----|-----|-----||");
        if indx%3 == 0:
            print("||=====|=====|=====||=====|=====|=====||=====|=====|=====||");

def check_num_can_be_fill(sdk,row,col,num):
    for x in range(9):
        if sdk[row][x] == num:
            return False
        
    for x in range(9):
        if sdk[x][col] == num:
            return False
    startRow = row - row%3
    startCol = col - col%3
    for i in range(3):
        for j in range(3):
            if sdk[i+startRow][j+startCol] == num:
                return False
    return True

def fill_sudoku(sdk,row=0,col=0):
    if row == M-1 and col == M:
        return True
    if col == M:
        row += 1
        col = 0
    if sdk[row][col] > 0:   #check box is alread filled if then go next box 
        return fill_sudoku(sdk,row,col+1)

    for num in range(1,M+1,1):
        if check_num_can_be_fill(sdk,row,col,num):
            sdk[row][col] = num
            if fill_sudoku(sdk,row,col+1):
                return True
        sdk[row][col] = 0
    return False

    
def create_empty_sudoku():
    numbers = [1,2,3,4,5,6,7,8,9]
    rand_row = random.randint(0,8)
    random.shuffle(numbers)
    sdk = [[0 for i in range(9)] for j in range(9)]
    sdk[rand_row] = numbers
    return sdk

def create_sudoku_puzle(sdk):
    n = random.randint(25,35)
    not_remove_boxes = []
    indexes = []
    for i in range(M):
        for j in range(M):
            indexes.append((i,j))
            
    while len(not_remove_boxes)<=n:
        num = random.choice(indexes)
        if num not in not_remove_boxes:
            not_remove_boxes.append(num)

    sdk_board = [[0 for i in range(9)] for j in range(9)]
    for r,c in not_remove_boxes:
        sdk_board[r][c] = sdk[r][c]
        
    return sdk_board     

if __name__== '__main__':
    #create sudoku and display before solved and after solved    
    sdk = create_empty_sudoku()
    fill_sudoku(sdk)
    solution = sdk
    
    print("FILL SUDOKO BOARD :??? ")
    sdk_board = create_sudoku_puzle(sdk)
    print_sdk(sdk_board)

    print("\n Solution of Sudoku :)) ")
    print_sdk(solution)

    #solve your own sudoku (pass you sudoku in fill_sudoku() function
    #if (fill_sudoku(sdk_board,0,0)):
    #    print("\nSolution of your Sudoku :)) ")
    #    print_sdk(sdk_board)
    #else:
    #    print("Solution Does not exist :(")
