# Head ends here

def next_move(posr, posc, board):
    # if board[posr][posc] == "d" : 
    #    print("CLEAN")
    
    # kachra = [[0 , 0]]
    
    k = 0
    l = 0
    
    for i in range(5) : 
        if board[i][l] == "d" : 
            print("CLEAN")
            
        for j in range(5) : 
            if board[i][j] == "d" : 
                k = j
            
            if k > l : 
                for a in range(k - l) :
                    print("RIGHT")
                    if board[i][a + k - l] == "d" : 
                        print("CLEAN")
            
            elif k < l : 
                for a in range(l - k) :
                    print("LEFT")
                    if board[i][a + l - k] == "d" : 
                        print("CLEAN")
        
            l = k
        if i != 4 :
            print("DOWN")  

# Tail starts here

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
