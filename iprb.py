def iprb():
    # Use the specified input values directly
    k, m, n = 2, 2, 2  # Input: 2 2 2

    return 1.0 - (n/2*(n-1) + n*m/2 + m/2*(m-1) / 4) /((k+m+n)*(k+m+n-1)/2)

a = iprb()
print(a)
