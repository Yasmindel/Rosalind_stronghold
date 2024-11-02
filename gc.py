import sys

# Simulated rosalind_utils for demonstration purposes
def gc_content(seq):
    """Calculate GC content of a DNA sequence."""
    g_count = seq.count('G')
    c_count = seq.count('C')
    total_count = len(seq)
    return (g_count + c_count) / total_count if total_count > 0 else 0

def read_fasta(fasta_str):
    """Read sequences from a FASTA formatted string."""
    records = []
    for entry in fasta_str.strip().split('>')[1:]:
        lines = entry.splitlines()
        desc = lines[0]
        seq = ''.join(lines[1:])
        records.append((desc, seq))
    return records

def gc():
    # Your input data
    fasta_input = """>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT"""

    records = read_fasta(fasta_input)
    gc_contents = [(desc, gc_content(seq)) for desc, seq in records]
    max_gc_content = max(gc_contents, key=lambda x: x[1])
    
    print(max_gc_content[0])
    print(max_gc_content[1] * 100)

# Run the function
gc()
