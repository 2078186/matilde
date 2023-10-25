#define a function prot(string) that translates a given RNA sequence into a protein sequence using the standard genetic code.
#The input RNA sequence is divided into codons (groups of three nucleotides), and each codon is translated into an amino acid using the provided genetic code.
#The translation continues until a stop codon ('*') is encountered.
def prot(string):#this function performs the translation of the input RNA sequence.
    #as I've said the pattern dictionary contains the genetic code, mapping RNA codons to their corresponding amino acids.
    #For example, it maps "UUU" to "F" (Phenylalanine), "CUU" to "L" (Leucine), "AUG" to "M" (Methionine), and so on. Stop codons, represented by "*", signal the end of translation.
    pattern = {"UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V",
           "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V",
           "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V",
           "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V",
           "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A",
           "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
           "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
           "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
           "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
           "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
           "UAA": "*", "CAA": "Q", "AAA": "K", "GAA": "E",
           "UAG": "*", "CAG": "Q", "AAG": "K", "GAG": "E",
           "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
           "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
           "UGA": "*", "CGA": "R", "AGA": "R", "GGA": "G",
           "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"}
    #rst is initialized as an empty string to store the translated protein sequence.
    #the input string is divided into codons by iterating through it in steps of 3 characters.
    #for each codon, the corresponding amino acid is obtained from the pattern dictionary, and it's added to the rst.
    #translation continues until a stop codon ('*') is encountered in the rst sequence.
    rst = ''.join([pattern[string[i:i+3]] for i in range(0, len(string), 3)])
    return rst[:rst.index("*")]


if __name__ == "__main__":
    with open("prot1.py", 'r') as file:
        string = file.readline().strip()
    print(prot(string)) #finally the code prints the translated protein sequence.