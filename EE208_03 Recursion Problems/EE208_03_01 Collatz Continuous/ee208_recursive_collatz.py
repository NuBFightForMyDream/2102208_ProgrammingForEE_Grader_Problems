def collatz_count(n: int) -> int:
    count_collatz = 0
    while n != 1 : 
        if n % 2 == 0 : # even number , divide by 2
            n = n // 2
        else : # odd number , multiply by 3 and add 1
            n = 3 * n + 1 
        # add count 
        count_collatz += 1 
            
    return count_collatz


if __name__ == "__main__":
    # You can test anything inside this block and can send it to grader
    # The grader will use only the function that you have implemented
    # !!! DO NOT write anything outside this block
    print(collatz_count(10))
