import sys
sys.path.append('../')
import rosalind_utils

def prot():
    # Use the specified input instead of reading from a file
    mrna = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"  # Specified mRNA sequence
    print(rosalind_utils.translate(mrna))

if __name__ == "__main__":
    prot()
