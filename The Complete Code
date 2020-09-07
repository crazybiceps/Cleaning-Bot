def next_move(posr, posc, board):
    dmin  = 0
    dmax  = 0
    psn   = 0
    
    for i in range(len(board)) :
        path = []
        count = 0
        for j in range(len(board[0])) :
            if board[i][j] == "d" : 
                count += 1
            
                if count == 1 : 
                    dmin = dmax = j
            
                elif count > 1 :
                    dmax = j
                        
        if dmin >= psn :
            path = [x for x in range(psn , dmax + 1)]
            
        elif psn > dmin :
            path = [x for x in range(psn , dmin , -1)]
            for k in range(dmin , dmax + 1) : 
                path.append(k)
        
        psn = path[-1]
                
        for k in range(len(path)) :
            if board[i][path[k]] == "d" :
                print("CLEAN")
                board[i][path[k]] = "-"
            
            if len(path) > 1 : 
                if path[k] != path[-1] :
                    if path[k+1] > path[k] : 
                        print("RIGHT")
                    else : 
                        print("LEFT")
        
        if i != 4 :
            print("DOWN")
 
# Tail starts here

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
