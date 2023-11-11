from Bio import SeqIO

def hamming_distance(s1, s2):
    return sum([1 if s1[i]!=s2[i] else 0 for i in range(len(s1))])
#I use the error_correct function to identify and to correct errors in the DNA sequences. Then I:
#Initialize empty lists for storing correct and incorrect reads.
#Define a reverse_pattern dictionary to facilitate reverse complement transformations of sequences.
#Loop through each sequence in the input list of reads (reads).
#For each sequence, I create a reverse complement (reverse_r) by reversing the sequence and replacing each nucleotide with its complement.
#Then I check if the current sequence or its reverse complement occurs at least twice in the list of reads. If it does, consider it as a correct read and add it to the correct_reads list.
#If not, it's marked as an incorrect read and added to the incorrect_reads list.
#For each incorrect read (ir) in the incorrect_reads list, I compare it to each correct read (cr) in the correct_reads list and the reverse complement of each correct read (reverse_cr).
def error_correct(reads):
    corrections = []
    correct_reads, incorrect_reads = [], []
    reverse_pattern={"A": "T", "T": "A", "C": "G", "G": "C"}

    for r in reads:
        reverse_r = "".join([reverse_pattern[i] for i in r[::-1]])
        if reads.count(r) + reads.count(reverse_r) >= 2:
            correct_reads.append(r)
        else:
            incorrect_reads.append(r)
#If the Hamming distance between the incorrect read and a correct read (or its reverse complement) is equal to 1, I consider it a potential correction. Then I add the pair (incorrect read, corrected read) to the corrections list.
#The function returns the list of corrections.
    for ir in incorrect_reads:
        for cr in correct_reads:
            reverse_cr = "".join([reverse_pattern[i] for i in cr[::-1]])
            if hamming_distance(ir, cr) == 1:
                corrections.append((ir, cr))
                break
            elif hamming_distance(ir, reverse_cr) == 1:
                corrections.append((ir, reverse_cr))
                break

    return corrections

if __name__ == "__main__":
   
    sequence_name, sequence_string = [], []
    with open ("input18.py",'r') as fasta:
        for sequence_record in SeqIO.parse(fasta,'fasta'):
            sequence_name.append(str(sequence_record.name))
            sequence_string.append(str(sequence_record.seq))
    
    corrections =error_correct (sequence_string)
    for ir, cr in corrections:
        print("{}->{}".format(ir, cr))
        #print the corrected sequences, displaying the incorrect sequences and their corresponding corrected sequences.