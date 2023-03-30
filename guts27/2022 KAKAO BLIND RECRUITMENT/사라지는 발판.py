from collections import Counter
def Aturn(board,aloc,bloc,anum,bnum):
    global result1,result2
    dx,dy = [-1,0,1,0],[0,1,0,-1]
    x,y = aloc
    if board[x][y] == 0:
        result2.append(anum + bnum)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= len(board) or ny < 0 or ny >= len(board[0]) or board[nx][ny] == 0:
            result2.append(anum + bnum)
        else:
            board[x][y] =0 
            Bturn(board,[nx,ny],bloc,anum+1,bnum)
            board[x][y] =1


def Bturn(board,aloc,bloc,anum,bnum):
    global result1,result2
    dx,dy = [-1,0,1,0],[0,1,0,-1]
    x,y = bloc
    if board[x][y] == 0:
        result1.append(anum + bnum)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
            
        if nx < 0 or nx >= len(board) or ny < 0 or ny >= len(board[0]) or board[nx][ny] == 0:
            result1.append(anum + bnum)
        else:
            board[x][y] = 0
            Aturn(board,aloc,[nx,ny],anum,bnum+1)
            board[x][y] =1
            
def solution(board, aloc, bloc):
    answer = -1
    global result1,result2
    result1,result2 = [],[]
    Aturn(board,aloc,bloc,0,0)
    
    counter1 = dict(Counter(result1))
    counter2 = dict(Counter(result2))
    
    print(result1,result2,len(result1),len(result2))
    print(counter1,counter2)
    if len(result1) < len(result2):
        #print('here2') - A패뱀
        mkey = max(counter2,key=counter2.get) 
        mvalue = counter2[mkey]    
        
        for key,value in counter2.items():
            if mvalue == value and mkey < key:
                mkey = key
                
    else:
        mkey = max(counter1,key=counter1.get) 
        mvalue = counter1[mkey]    
        
        for key,value in counter1.items():
            if mvalue == value and mkey < key:
                mkey = key
        
        print('here')
    print(counter1,counter2)
    return mkey
