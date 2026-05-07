import numpy as np

def softmax(A): # Note : Row-wise !!!
    # Ex : [1 2 3] = [e1 / e1+e2+e3 , e2 / e1+e2+e3 , e3 / e1+e2+e3]
    
    # Step 1 : make array to be exponential
    exponent_A = np.exp(A)
    
    # Step 2 : find degree of total exponent 
    cumulative_exponent = np.sum(np.exp(A) , axis = 1).reshape(-1,1) # axis 1 = vertical 
        ## reshape cumulative_exponent to nx1 matrix
    
    
    # Step 3 : find probability with P = e^current / e^horizontal_total
    softmax_prob = exponent_A / cumulative_exponent
    return softmax_prob

if __name__ == "__main__":
    # You can test anything inside this block and can send it to grader
    # The grader will use only the function that you have implemented
    # !!! DO NOT write anything outside this block
    A = np.array([[1.0, 2.0, 3.0],
                  [4.0, 5.0, 6.0]])
    print(softmax(A))