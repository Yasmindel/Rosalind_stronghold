
fib_cache = {}

def fib_helper(n, k):
    """
    Recursively calculates the number of rabbit pairs using dynamic programming.
    
    Args:
    n (int): The number of months.
    k (int): The number of rabbit pairs produced by each reproduction-age pair.
    
    Returns:
    int: The total number of rabbit pairs after n months.
    """
    
    # If result already exists in cache, return it
    if (n, k) in fib_cache:
        return fib_cache[(n, k)]
    
  
    if n == 1 or n == 2:
        fib_cache[(n, k)] = 1
    else:
        # Recurrence relation: F(n) = F(n-1) + k * F(n-2)
        fib_cache[(n, k)] = fib_helper(n-1, k) + k * fib_helper(n-2, k)
    
    return fib_cache[(n, k)]

def fib():
    """
    Reads the input data, computes the result using fib_helper function, and prints it.
    """
    with open("rosalind_fib.txt") as file:
        n, k = map(int, file.read().split())
    result = fib_helper(n, k)
    print(result)

# Uncomment the line below to run the function if needed
# fib()
