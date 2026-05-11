import numpy as np
def triangular_system(n):
    """
    A =
        2 0.5 0.5 0.5
        -0.5 2 0.5 0.5
        -0.5 -0.5 2 0.5
        -0.5 -0.5 -0.5 2
    """
    
    # Note : we'll use np.diag() for diagonal line and
    ## we'll use np.triu/l() for upper/lower triangular
    ## but , np.tril/u(matrix , k) -> for k = 0 will include diagonal
    ## so in this case we'll use k = +-1 for not including value in diagonal line
        
    # Step 1 : Define ndarray with nxn matrix 
    new_matrix = np.zeros((n,n)) # shape nxn

    # Step 2 : Define matrix then concat all matrix 
    diag_matrix = 2 * np.eye(n) # diagonal value = 2
    
    ## Note that upper & lower matrix will generate nxn matrix 
    upper_tri_matrix = np.triu(0.5 * np.ones((n,n)) , k = 1) # upper triangular value = 0.5
    lower_tri_matrix = np.tril(-0.5 * np.ones((n,n)) , k = -1) # lower triangular value = -0.5
    
    # Step 3 : Add all matrix together
    new_matrix += (diag_matrix + upper_tri_matrix + lower_tri_matrix)
    # Return the resulting matrix
    return new_matrix


exec("\n".join(iter(input, "#Exit"))) # Don’t remove this line