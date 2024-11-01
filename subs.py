def subs(s, t):
    positions = []
    
    # Search for all occurrences of the substring t in s
    idx = s.find(t)  # Find the first occurrence of t in s
    while idx != -1:
        positions.append(idx + 1)  # Store 1-based index
        idx = s.find(t, idx + 1)  # Continue searching from the next position
    
    # Print all positions in a single line
    print(' '.join(map(str, positions)))

# Directly inputting the strings
s = "GATATATGCATATACTT"
t = "ATAT"
subs(s, t))
