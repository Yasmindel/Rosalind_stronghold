def count_dna_bases(s):
    """
    This function takes a DNA string s and counts the occurrences of each base: 'A', 'C', 'G', and 'T'.
    The result is printed as four integers, separated by spaces.
    
    Args:
    s (str): A DNA string of length at most 1000 nt.
    
    Returns:
    None: The result is printed directly.
    """
    
    # Count occurrences of each base in the string
    a_count = s.count('A')
    c_count = s.count('C')
    g_count = s.count('G')
    t_count = s.count('T')
    
    # Print the counts in the desired format
    print(a_count, c_count, g_count, t_count)

# Example usage with a sample dataset
sample_dna = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
count_dna_bases(sample_dna)
