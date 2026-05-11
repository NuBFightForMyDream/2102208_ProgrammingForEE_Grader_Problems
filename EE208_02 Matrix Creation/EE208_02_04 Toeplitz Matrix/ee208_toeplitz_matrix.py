import numpy as np 
def toeplitz_matrix(n):
    ## This matrix is like Diagonal Triangular matrix but like stair
    
    ## Step 1 : create nxn matrix for diffrence of exponent
    ## define zeros array 
    exponent_difference = np.zeros((n,n))
    ## define array from range 1-n
    num_range_horizontal_i = np.arange(1,n+1,1).reshape(1,n)
    num_range_vertical_j = num_range_horizontal_i.copy().reshape(-1,1)
    ## broadcast then subtract
    exponent_difference = abs(num_range_horizontal_i - num_range_vertical_j)

    # Step 2 : define value from function of toeplitz
    ## exponent value first
    toeplitz = (-0.5) ** exponent_difference
    ## fill diagonal using np.fill_diagonal
    np.fill_diagonal(toeplitz , 2)
    
    ## return matrix
    return toeplitz
    
exec("\n".join(iter(input, "#Exit"))) # Don’t remove this line
