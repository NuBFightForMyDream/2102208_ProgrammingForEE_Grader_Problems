import numpy as np
def vandermonde_matrix(t):
    ## This matrix is square from matrix t as row
    
    ## Step 1 : Define nxn matrix as result
    n = t.shape[0] # n = matrix size = #row = #col
    
    ## using np.tile to copy 1 row to be same as first row in exponent_matrix
    
    ## Step 2 : define base matrix for doing operation later
    ## transpose / reshape to vertical (nx1) then tile horizontally 
    base_matrix = np.tile(t.reshape(-1,1) , (1 , n) )
        # tile matrix with vertical (#shape time) and horizontal (1 time)
    
    ## Step 3 : define exponent base (tile vertically)
    exponent_matrix = np.tile(np.arange(0 , n , 1) , (n , 1))
    
    ## return operated matrix
    vandermonde = base_matrix ** exponent_matrix # element-wise operation
    return vandermonde # Return the resulting matrix

exec("\n".join(iter(input, "#Exit"))) # Don’t remove this line
