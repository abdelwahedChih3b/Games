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
    while i != 10 and j !=10 :
        
        if mat[i+1][j] == 1 :
            iPlus = 1
            jPlus = 0
            i+=1
        elif mat[i][j+1] == 1 :
            iPlus = 0
            jPlus = 1
        elif mat[i-1][j] == 1 :
            iPlus = -1
            jPlus = 0
        elif mat[i][j-1] == 1 :
            iPlus = 0
            jPlus = -1
        else : print("blocked")
        j += jPlus
        i += iPlus
        if mat[i+1][j] + mat[i][j+1] + mat[i-1][j] + mat[i][j-1] == 3 : 
            mat[i][j] = 0
            i -= iPlus
            j -= jPlus
        print("i = {} , j = {}".format(i,j))
        time.sleep(100)
    print("done")

path(mat)

