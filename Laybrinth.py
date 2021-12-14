"""@this challenge is to solve laybrinth probleme 
@1 represent wall
@0 represent path  """

import time

mat = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]


def path( mat) :
    i,j =1,1
    iPlus =0
    jPlus =0
    direct = []
    while i != 10 and j !=10 and i <=11 and j<= 12 :
        if mat[i+1][j] + mat[i][j+1] + mat[i-1][j] + mat[i][j-1] == 4 : 
            mat[i][j] = 0
            i -= iPlus
            j -= jPlus
            
        if mat[i+1][j] == 0 :
            iPlus = 1
            jPlus = 0
            direct.append("E")
        elif mat[i][j+1] ==0 :
            iPlus = 0
            jPlus = 1
            direct.append("S")
        elif mat[i-1][j] == 0 :
            iPlus = -1
            jPlus = 0
            direct.append("W")
        elif mat[i][j-1] == 0 :
            iPlus = 0
            jPlus = -1
            direct.append("N")
        j = j+ jPlus
        i = i+ iPlus
        
        print("i = {} , j = {}".format(i,j))
        
    print(direct)

path(mat)

