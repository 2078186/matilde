from Bio import SeqIO

def reverse_complement(s):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return ''.join(complement[base] for base in reversed(s))

def find_reverse_palindromes(dna_string):
    #The find_reverse_palindromes function takes a DNA string and finds reverse palindromes of lengths ranging from 4 to 12.
    #It iterates through the DNA string and, for each starting position i and length length, checks if the substring is a palindrome by comparing it to its reverse complement.
    #If a reverse palindrome is found, the starting position and length are appended to the results list.
    results = []
    for i in range(len(dna_string)):
        for length in range(4, 13):
            if i + length <= len(dna_string):
                substring = dna_string[i:i+length]
                if substring == reverse_complement(substring):
                    results.append((i + 1, length))
    return results

if __name__ == "__main__":
    # Read the input from a FASTA file
    fasta_file = "revp1.py"
    sequence = str(SeqIO.read(fasta_file, "fasta").seq)

    # Find reverse palindromes and print the results
    palindromes = find_reverse_palindromes(sequence)
    for position, length in palindromes:
        print(f"{position} {length}")
