def subs():
    # Predefined dataset as per your input
    s = "GATATATGCATATACTT"  # The main string
    t = "ATAT"               # The substring to search for
    
    idx = -1
    results = []
    while True:
        try:
            idx = s.index(t, idx + 1)  # Find the next occurrence of t in s
            results.append(idx + 1)     # Store the 1-based index
        except ValueError:
            break

    print(' '.join(map(str, results)))  # Print all found indices as a single line

if __name__ == "__main__":
    subs()
