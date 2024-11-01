def transcribe_rna(dna_seq):
    """
    This function takes a DNA string and returns its transcribed RNA string.
    In RNA, 'T' is replaced by 'U'.
    
    Args:
    dna_seq (str): A DNA string of length at most 1000 nt.
    
    Returns:
    str: The transcribed RNA string.
    """
    
    # Replace 'T' with 'U' to transcribe the RNA sequence
    rna_seq = dna_seq.replace('T', 'U')
    return rna_seq

# Example usage with a sample dataset
sample_dna = "GATGGAACTTGACTACGTAAATT"
print(transcribe_rna(sample_dna))
