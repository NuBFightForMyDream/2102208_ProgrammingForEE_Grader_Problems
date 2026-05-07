import numpy as np
def numpy_conditional(A):
    # Step 1 : get conditioned array 
    negative_num_arr = A[A < 0]
    # Step 2 : fix condition then put back to conditioned array
    A[A<0] = negative_num_arr + 2
    # Step 3 : return array
    return A
    
if __name__ == "__main__":
    # You can test anything inside this block and can send it to grader
    # The grader will use only the function that you have implemented
    # !!! DO NOT write anything outside this block
    A = np.array([-1, 0, 1, -5, 3])
    print(numpy_conditional(A))