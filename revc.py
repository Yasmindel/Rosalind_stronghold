def reverse_complement(dna):
    """Returns the reverse complement of a DNA sequence."""
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    reversed_dna = dna[::-1]  # Reverse the DNA sequence
    return ''.join(complement[base] for base in reversed_dna)  # Create the complement

def revc():
    # Predefined dataset as per your input
    dna = "AAAACCCGGT"  # The specified DNA sequence
    print(reverse_complement(dna))
    
if __name__ == "__main__":
    revc()
