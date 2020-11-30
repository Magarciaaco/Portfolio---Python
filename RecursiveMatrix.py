# Coded by: Miguel Angel Garcia Acosta
# Contact: MAGA.DevCS@Gmail.com
# --------------------------
# MATRIX RECURSIVE REPLACER:
# --------------------------
# ----- ----- ----- ----- --
# ------------------------------------------------------------------------------------------------
# Problem: Given a Matrix A: n x n | Randomly generated, a sub matrix V: 2 x 2 in A: will be
#          required to be replaced by a matrix W: 2 x 2 recursively until there is no sub matrix
#          V: in A:.
# ------------------------------------------------------------------------------------------------

# ----- ----- ----- IMPORTS ----- ----- ----- #
from random import randint as RANDOM
import matplotlib.pyplot as PLOT
import numpy as NP
# ----- ----- ----- IMPORTS ----- ----- ----- #
#
# __Random_Matrix__( int n )
# Creates a n x n random number matrix:
#
# start __Random_Matrix__
def __Random_Matrix__(n):
    Mat = [[ 0 for i in range(n)] for j in range(n)]
    k = 0
    for i in range(n):
        for j in range(n):
            k = RANDOM(0, 1)
            Mat[i][j] = k
    return Mat
# end __Random_Matrix__
#
# start __Matrix_Swap__
# Swaps sub matrix A with sub matrix B in M
def __Matrix_Swap__(B, M, i, j):
    print('swap A with B')
    M[i][j] =     B[0][0]
    M[i][j + 1] = B[0][1]
    M[i + 1][j] = B[1][0]
    M[i + 1][j + 1] = B[1][1]
    print('swap ' + str(i) + " x " + str(j))
    return M
# end __Matrix_Swap__
#
# start __Sub_Matrix__
# Returns a Boolean type that confirms that there is a Sub Matrix N in Matrix M; M is a 6 x 6 matrix | N is a 2 x 2 Matrix
def __Sub_Matrix__(N, M, i, j):
    if ( M[i][j] == N[0][0] ):
        if ( M[i][j + 1] == N[0][1] ):
            if ( M[i + 1][j] == N[1][0] ):
                if ( M[i + 1][j + 1] == N[1][1] ):
                    return True
    
    return False
# end __Sub_Matrix__
#
# __Matrix_Replace__(int[][] A, int[][] B)
# Search and replace sub-Matrix A with sub-Matrix B -- Recursively until there is no sub-matrix B
#
# start __Matrix_Replace__
def __Matrix_Replace__(A, B, M, i, j):
    # BASE CASE: if index M[i][j] == M[ k_i - 1 ] [ k_j - 1 ] return M (Recursive Operations are Finished)
    if ( i >= len(M) - 2 & j >= len(M) - 2 ):
        print(NP.matrix(M))
        return M
    # Sub Matrix A in M -- if true, then replace
    if (__Sub_Matrix__(A, M, i, j)):
        M = __Matrix_Swap__(B, M, i, j)

    if (i < len(M) - 2 & j >= len(M) - 2):
        __Matrix_Replace__(A, B, M, i + 1, 0)
    else:
        __Matrix_Replace__(A, B, M, i, j + 1)

#
# end __Matrix_Replace__
#
# START
#
# 1) DEFINE AND INITIALIZE RANDOM GENERATED n x n ARRAYS:
#       A: n = 6
#       V: 2 x 2
#       W: 2 x 2
# 1): START
A = __Random_Matrix__(6)
V = __Random_Matrix__(2)
W = __Random_Matrix__(2)
# 1): END
#
# DISPLAY MATRIX A:
print("Matrix A:")
print(NP.matrix(A))
# DISPLAY MATRIX V:
print("Matrix V:")
print(NP.matrix(V))
# DISPLAY MATRIX W:
print("Matrix W:")
print(NP.matrix(W))
#
# 2) RECURSIVELY SEARCH MATRIX V IN A, AND REPLACE V WITH W
# 
# 2): START
#
print("Matrix A:")
A = __Matrix_Replace__(V, W, A, 0, 0)
# 2): END
#
# END
