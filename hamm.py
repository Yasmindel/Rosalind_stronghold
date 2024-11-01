def hamming_distance(s, t):
    """Calculate the Hamming distance between two strings."""
    return sum(1 for na, nb in zip(s, t) if na != nb)

def hamm():
    # Sample input directly
    s = "GAGCCTACTAACGGGAT"  # First DNA string
    t = "CATCGTAATGACGGCCT"  # Second DNA string
    
    # Output the Hamming distance
    print(hamming_distance(s, t))

# Run the function
hamm()
