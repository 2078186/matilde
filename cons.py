#import the necessary libraries: Biopython for handling sequences and NumPy for working with arrays.
from Bio import SeqIO
import numpy as np
np.set_printoptions(threshold=np.inf)

sequence_name, sequence_string = [], []
#read data from a file named "cons27.py" in FASTA format. It parses the sequences and stores the sequence names and strings in separate lists.
with open ("cons27.py",'r') as fasta:
    for seq_record  in SeqIO.parse(fasta,'fasta'):
        sequence_name.append(str(seq_record.name))
        sequence_string.append(str(seq_record.seq))
#calculate the length of the sequences and stores it in seq_len.
seq_len = len(sequence_string)
str_len = len(sequence_string[0])
#define a list of DNA symbols: ["A", "C", "G", "T"].
symbol = ["A", "C", "G", "T"]
#initialize an empty consensus string and a NumPy array for the profile matrix.
consensus_string = ""
profile_matrix = np.zeros(shape=(4, str_len), dtype=int)
#iterate through each position in the sequences (columns).
#for each position, extract the symbols from all sequences at that position and find the most common symbol.
#the most common symbol is added to the consensus string.
#also count the occurrences of each symbol at that position and update the profile matrix.
for c in range(str_len):
    position_symbol = [s[c] for s in sequence_string]
    most_common_symbol = max(position_symbol, key=position_symbol.count)
    consensus_string += most_common_symbol
    for r in range(len(symbol)):
        profile_matrix[r][c] = position_symbol.count(symbol[r])
#this code effectively generates a consensus sequence and a profile matrix based on the provided DNA sequences and prints the results.
#the profile matrix provides information about the frequency of each symbol at each position in the sequences.
print(consensus_string)
for i in range(len(symbol)):
    print("{}: {}".format(symbol[i], " ".join([str(j) for j in profile_matrix[i]])))

