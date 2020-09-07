def next_move(posr, posc, board) :
    
    count = 0
    for i in range(len(board[0])) :
        
        if board[posr][i] == "d" : 
            count += 1
            psn = i 
            break
            
    if count > 0 : 
        if psn >= posc : 
            if board[posr][posc] == "d" :
                print("CLEAN")
            else :
                print("RIGHT")
                posc = posc + 1
        
        else :
            if board[posr][posc] == "d":
                print("CLEAN")
            else :
                print("LEFT")
                posc = posc - 1
    
    else :
        if posr != 4 :
            posr = posr + 1
            print("DOWN")
 
# Tail starts here

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
