from Bio import SeqIO
# shortest_seq(seq): This function finds the shortest sequence among the given DNA sequences.
#shared_motif(seq): This function finds the longest shared motif among the DNA sequences.
def shortest_seq(seq):
    #The shortest_seq(seq) function is used to identify the shortest sequence among the given DNA sequences.
    #It iterates through the sequences and keeps track of the shortest sequence by comparing their lengths.
    min_len = 10000
    shortest_seq = ''
    for i in seq.keys():
        if len(seq[i]) < min_len:
            min_len = len(seq[i])
            shortest_seq = seq[i]
    return shortest_seq

def shared_motif(seq):
    #The shared_motif(seq) function is responsible for finding the longest shared motif among the sequences. It follows these steps:
    #It calls the shortest_seq(seq) function to find the shortest sequence in the collection.
    #It initializes a set called motif to store potential shared motifs.
    #It iterates through all possible substrings of the shortest sequence and adds them to the motif set.
    #For each sequence in the collection, it iteratively updates the motif set by removing substrings that are not present in the current sequence. This operation filters out substrings that are not shared among all sequences.
    #After processing all sequences, it identifies the longest substring in the motif set and assigns it to the variable longest_motif.
    s_sequence = shortest_seq(seq)
    motif = set()
    for i in range(len(s_sequence)):
        for j in range(i+1,len(s_sequence)+1):
            motif.add(s_sequence[i:j])
    for s in seq.values():
        update_motif = list(motif)
        for m in update_motif:
            if m not in s:
                motif.remove(m)
    n = 0
    longest_motif = ''
    for i in motif:
        if len(i) > n:
            longest_motif = i
            n = len(i)
    return longest_motif

if __name__ == "__main__":
   
    sequence_name, sequence_string = [], []
    with open ("lcsm7.py",'r') as fasta:
        for seq_record  in SeqIO.parse(fasta,'fasta'):
            sequence_name.append(str(seq_record.name))
            sequence_string.append(str(seq_record.seq))
    seq = {sequence_name[i]:sequence_string[i] for i in range(len(sequence_name))}
    print(shared_motif(seq))
    # I identify the shortest sequence in the input DNA sequences and then I find the longest shared motif that is present in all the sequences.