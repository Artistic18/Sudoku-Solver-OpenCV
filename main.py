from pre_process import extract as extract_img
from predict import extract_number as extract_sudoku
from solver import solve as solve_sudoku

def board(sudoku):
    for i in range(len(sudoku)):
        if i%3 == 0:
            if i==0:
                print(" ┎─────────┰─────────┰─────────┒")
            else:
                print(" ┠─────────╂─────────╂─────────┨")
        for j in range(len(sudoku[0])):
            if j%3 == 0:
                print(" ┃ ", end=" ")
            if j == 8:
                print(sudoku[i][j] if sudoku[i][j] != 0 else ".", " ┃")
            else:
                print(sudoku[i][j] if sudoku[i][j] != 0 else ".", end=" ")
    print(" ┖─────────┸─────────┸─────────┚")
    
def error_in_board(sudoku):
    print("Do you want to modify any value?")
    print("Please enter [y/n]: ")
    ans = input()
    counter = 1
    if(ans == 'y'):
        while counter > 0:
            print("Please enter the index(i, j) and value : ")
            i, j, n = map(int, input().split())
            sudoku[i][j] = n
            print("Do you want to change any more values?")
            print("Please enter [y/n]: ")
            inp = input()
            if inp == 'y':
                continue
            else:
                break
    print("   Updated Board")
    board(sudoku)
        
    
def main():
    image = extract_img()
    print('Image Extracted')
    print('\nProcessing Digits...')
    
    sudoku = extract_sudoku(image)
    print('\nSuccessfully Extracted Digits')
    
    print("\n\n  Sudoku Board")
    board(sudoku)
    
    error_in_board(sudoku)
       
    result, possible = solve_sudoku(sudoku)
    if possible == 1:
        print("   Solution")
        board(result)
    else:
        print("No solution possible")
    
if __name__ == '__main__':
    main()