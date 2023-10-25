def mrna(protein):
    #the codons dictionary maps each amino acid to a list of codons that can code for that amino acid.
    #It accounts for the degeneracy of the genetic code, where multiple codons can specify the same amino acid.
    codons = {'F': ['UUU', 'UUC'],
              'L': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'],
              'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],
              'Y': ['UAU', 'UAC'],
              '*': ['UAA', 'UAG', 'UGA'],
              'C': ['UGU', 'UGC'],
              'W': ['UGG'],
              'P': ['CCU', 'CCC', 'CCA', 'CCG'],
              'H': ['CAU', 'CAC'],
              'Q': ['CAA', 'CAG'],
              'R': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
              'V': ['GUU', 'GUC', 'GUA', 'GUG'],
              'A': ['GCU', 'GCC', 'GCA', 'GCG'],
              'D': ['GAU', 'GAC'],
              'E': ['GAA', 'GAG'],
              'G': ['GGU', 'GGC', 'GGA', 'GGG'],
              'I': ['AUU', 'AUC', 'AUA'],
              'M': ['AUG'],
              'T': ['ACU', 'ACC', 'ACA', 'ACG'],
              'N': ['AAU', 'AAC'],
              'K': ['AAA', 'AAG']}
    #The mrna(protein) function calculates the number of different RNA sequences that can code for the given protein sequence. 
    #It does this by considering the possible codons for each amino acid in the protein.
    #So, I initializes a variable number to 1, which will be used to keep track of the total number of possible RNA sequences.
    #Then I iterate through each amino acid in the input protein sequence.
    #For each amino acid, multiply number by the number of codons that can code for that amino acid. This accounts for the degeneracy of the genetic code.
    #After processing all amino acids, multiply number by the number of stop codons ('*') since the protein sequence should end with a stop codon.
    #Finally, calculate the result modulo 1,000,000 ( number % 1,000,000) to prevent very large numbers and returns this value.
    number = 1
    for aa in protein:
        number = number * len(codons[aa])
    number = number*len(codons["*"])
    return number % 1000000


if __name__ == "__main__":
    with open("mrna12.py", 'r') as file:
        protein = file.readline().strip()
        number = mrna(protein)
        print(number)
        #the result represents the number of different RNA sequences that can code for the given protein sequence while considering codon degeneracy and is taken modulo 1,000,000.