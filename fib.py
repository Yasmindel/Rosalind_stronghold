import sys
sys.path.append('../')
import rosalind_utils

# Cache for previously computed Fibonacci values
prefib = {}

def fib_helper(n, k):
    if (n, k) in prefib:
        return prefib[(n, k)]
    if n == 1 or n == 2:
        prefib[(n, k)] = 1
    else:
        prefib[(n, k)] = fib_helper(n - 1, k) + k * fib_helper(n - 2, k)
    return prefib[(n, k)]

def fib():
    # Using the input directly instead of reading from a file
    n, k = 5, 3  # Directly setting the values for n and k
    print(fib_helper(n, k))

# Run the function
fib()
