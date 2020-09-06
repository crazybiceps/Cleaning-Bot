#!/usr/bin/python

# Head ends here

def next_move(posr, posc, board):
    
    p = 0
    q = 0
    dmin = 0
    dmax = 0
    position = 0
    
    for i in range(5) : 
        count = 0
        for j in range(5) : 
            if board[i][j] == "d" : 
                count += 1
                if count == 1 : 
                    dmax = dmin = j
                elif count > 1 : 
                    dmax = j
                    
        if count > 0 :
            for l in range(dmin , dmax + 1):
                if position < dmin :
                    for k in range(position , dmin , 1) :  
                        print("RIGHT")
                        position = k + 1
                    
                elif position > dmin :
                    for k in range(position , dmin , -1) : 
                        if board[i][k] == "d" : 
                            print("CLEAN")
                            board[i][k] == "-"
                        
                        print("LEFT")
                        position = k - 1
            
                elif position == dmin : 
                    print("CLEAN")
                    board[i][dmin] = "-"
                    if dmin != dmax : 
                        position += 1
                        print("RIGHT")
            
        if i != 4 : 
            print("DOWN")
                    
  
# Tail starts here

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
