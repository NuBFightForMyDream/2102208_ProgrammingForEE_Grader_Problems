import numpy as np
def cosine_of_difference(x) :
    
    # This task should use broadcasting method to subtract matrix together
    
    # Step 1 : get horizontal & vertical array from x
    ## Note that shouldn't use Transpose bcz x is 1D array (making it to be 2d array for broadcasting)
    ## so using reshape is better solution 
    x_horizontal_i = x.copy().reshape(1,-1) # row vector -> 1xn 
    x_vertical_j = x.copy().reshape(-1,1) # column vector -> nx1
    
    # Step 2 : transform each matrix to cosine
    cos_xi = np.cos(x_horizontal_i)
    cos_xj = np.cos(x_vertical_j)
    
    return cos_xi - cos_xj # Return the resulting matrix

exec("\n".join(iter(input, "#Exit"))) # Don’t remove this line
