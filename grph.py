from Bio import SeqIO


data = "input.fasta5.py"
n = 3

#the input data is stored in a file named "input.fasta5.py."
#initialize two empty lists, sequence_name and sequence_string, to store the names and DNA sequences from the FASTA file, respectively.
sequence_name, sequence_string = [], []
with open (data) as fasta:
    for sequence_record  in SeqIO.parse(fasta,'fasta'):
        sequence_name.append(str(sequence_record.name))
        sequence_string .append(str(sequence_record.seq))
#I use two nested loops to compare each pair of sequences in the input data.
#Then I check if the last n characters of the i-th sequence (sequence_string[i]) match the first n characters of the j-th sequence (sequence_string[j]). This is done by slicing the sequences and comparing the slices.
#If a match is found (there's an overlapping subsequence of length n), the code prints the names of the sequences that match ( sequence_name[i] and sequence_name[j]).

for i in range(len(sequence_string)):
    for j in range(len(sequence_string)):
        if i != j:
            if sequence_string[i][-n:] == sequence_string[j][:n]:
                print(sequence_name[i], sequence_name[j])