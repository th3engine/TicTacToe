from random import randint
import time

print("------ TIC TAC TOE -------\n")


n_players = input("Enter 1 for single player, and 2 for multiplayer: ")


board=[[" "," "," "],
       [" "," "," "],
       [" "," "," "]]


def display_board():
    for row in board:
        for i in row:
            print("|",end=" ")
            print(i,end=" | ")
        print("\n ----------------")

def player_input(player):
    print(f"Player {player+1}: ")
    valid_inputs = False
    while not valid_inputs:
        try:
            xloc = int(input("What x position would you like to play? (0 to 2): "))
            yloc = int(input("What y position would you like to play? (0 to 2): "))
        except ValueError:
            print("Please enter a valid input")
        else:
            if xloc in range(0,3) and yloc in range(0,3):
                if board[xloc][yloc] == " ":
                    add_mark(xloc,yloc)
                    valid_inputs=True
                else:
                    print(f"\nPoint {xloc},{yloc} already Taken. Please enter an empty co-ordinate \n")
                    continue
            else:
                print("Please enter co-ordinates in range [0-2],[0-2] \n")


def computer():
    position_found = False
    while not position_found:
        xloc, yloc = randint(0,2), randint(0,2)
        if board[xloc][yloc] ==" ":
            add_mark(xloc,yloc)
            position_found=True
    
def add_mark(xloc,yloc):
    if player==0:
        board[xloc][yloc] = "X"
    else:
        board[xloc][yloc] = "O"

def check():
    diag = []
    reverse_diag = []
    for i in range(0,3):
        across = board[i][0]
        along = board[0][i]
        if all([item.strip()==across for item in board[i]]) or all([along==board[j][i].strip() for j in range(0,3)]): # checks each row and column to see if the values is equal to the first element in that row/column
            return True
        else:
            diag.append(board[i][i])
            reverse_diag.append(board[i][i%2])
    
    reverse_diag[0] = board[0][2] 
    if all([board[0][0]==item.strip() for item in diag]) or all([board[0][2]==item.strip() for item in reverse_diag]): # checks for diagonal elements
        return True
    else:
        return False
    
def is_full():
    verify=[]
    for row in board:
        verify.extend([item!=" " for item in row])
    return all(verify)

n=0   
while not check():
    display_board()
    if is_full():
        print("\nThe Game Ends With A Draw !!!\n")
        break
    player = n%2
    if n_players == "2" or player==0:
        player_input(player)
    else:
        computer()
        time.sleep(2)
        print("\nComputer (Player 2)")
    n+=1

if check():
    print(f"Player {player+1} wins !!!")
    display_board()




       

            
        


