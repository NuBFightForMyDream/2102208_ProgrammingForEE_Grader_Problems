import numpy as np
def second_max_per_column(A):
    
    ## Step 0 : define min value in array A
    min_val_arr = np.min(A)
    
    # Step 1 : get array of max for each column
    # Step 2 : reshape for 1xn matrix [numpy will calculate n automatically)
    max_in_column_arr = np.max(A , axis = 0).reshape(1,-1) # axis 0 = vertical 
    
    # Step 3 : replace every value found (max in column) with min value  
    A[ max_in_column_arr == A ] = min_val_arr 
    
    # Step 4 : get max again (which they wont appear old max but will be second max instead)
    second_max_in_column_arr = np.max(A , axis = 0)
    
    return second_max_in_column_arr


if __name__ == "__main__":
# You can test anything inside this block and can send it to grader
# The grader will use only the function that you have implemented
# !!! DO NOT write anything outside this block
    A = np.array([
        [7.0, 3.0, 5.0, 5.0],
        [7.0, 1.0, 9.0, 2.0],
        [4.0, 3.0, 9.0, -1.0],
        [0.0, 8.0, 9.0, 5.0]
    ])
    
    print(second_max_per_column(A))
