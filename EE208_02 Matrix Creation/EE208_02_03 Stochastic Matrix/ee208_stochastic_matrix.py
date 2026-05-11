import numpy as np 
def stochastic_matrix(n):
    
    ## Condition of stochastic matrix
    # 1. all member in matrix must be positive
    # 2. each column sum must be 1
    # 3. 80% must not be zero
    
    # Step 1 : generate randomed matrix nxn
    randomed_matrix = np.random.rand(n,n)
    
    # Step 2 : get summation of each column with np.sum
    column_summation = np.sum(randomed_matrix , axis = 0) # axis 0 = vertical
    
    # Step 3 : normalize value with column_summation
    normalized_matrix = randomed_matrix / column_summation

    # return normalized matrix    
    return normalized_matrix # Return the stochastic matrix A

exec("\n".join(iter(input, "#Exit"))) # Don’t remove this line