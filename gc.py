def read_fasta(filename):
    """
    Reads a file in FASTA format and returns a list of tuples with description and sequence.
    
    Args:
    filename (str): The name of the file containing FASTA formatted data.
    
    Returns:
    list: A list of tuples where each tuple contains (description, sequence).
    """
    with open(filename, 'r') as file:
        sequences = {}
        current_label = ""
        
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                current_label = line[1:]
                sequences[current_label] = []
            else:
                sequences[current_label].append(line)
        
        # Join sequence lines and return the data
        return [(label, ''.join(seq)) for label, seq in sequences.items()]

def gc_content(sequence):
    """
    Calculates the GC content of a DNA sequence.
    
    Args:
    sequence (str): The DNA sequence.
    
    Returns:
    float: The GC content as a percentage of the total sequence length.
    """
    gc_count = sequence.count('G') + sequence.count('C')
    return (gc_count / len(sequence)) * 100

def gc():
    # Read the sequences from the file
    fasta_records = read_fasta("rosalind_gc.txt")
    
    # Calculate GC content for each sequence
    gc_contents = [(desc, gc_content(seq)) for desc, seq in fasta_records]
    
    # Find the sequence with the highest GC content
    max_gc = max(gc_contents, key=lambda x: x[1])
    
    # Print the ID and the GC content (formatted to 6 decimal places)
    print(max_gc[0])
    print(f"{max_gc[1]:.6f}")

# Uncomment the line below to run the function if needed
gc())
