def reverse_complement(dna_seq):
    """
    This function takes a DNA string and returns its reverse complement.
    In DNA, 'A' complements 'T', and 'C' complements 'G'.
    
    Args:
    dna_seq (str): A DNA string of length at most 1000 bp.
    
    Returns:
    str: The reverse complement of the input DNA string.
    """
    
    # Define the complement mapping for each base
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    
    # Reverse the DNA sequence and replace each base with its complement
    rev_complement = ''.join(complement[base] for base in reversed(dna_seq))
    
    return rev_complement

# Example usage with a sample dataset
sample_dna = "AAAACCCGGT"
print(reverse_complement(sample_dna))
