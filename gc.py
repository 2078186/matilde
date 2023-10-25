from __future__ import division

#In this exercise I initialize two variables, max_gc and max_id, to keep track of the maximum GC content found and the corresponding sequence ID.
max_gc = 0.0
#the code opens a file named 'rosalind12.py' in which I find the FASTA-formatted DNA sequences. 
with open('rosalind12.py') as file:
    content = file.readlines()
    #The code reads the content of the file line by line using a for loop.
#Inside the loop, it uses enumerate to keep track of the line number and the line content (line).
    for i, line in enumerate(content):
        #When the code encounters a line that starts with '>', it assumes this is an identifier line, which typically contains sequence information.
        #It extracts the sequence ID by removing the '>' character from the line and assigns it to the id variable. This ID identifies the current sequence.
        #If the line does not start with '>', it is considered part of the DNA sequence.
        #The line's content is stripped of leading and trailing whitespace, and then it's appended to the sequence string ('sequence'). This continues until the entire sequence is collected.
        if line.startswith('>'):
            id = line[1:]
            # reset sequence string
            sequence = ''
        else:
            newsequence = line.strip()
            sequence = sequence + newsequence
            # print if last substring or if next substring starts with '>'
            if i==len(content)-1 or content[i+1].startswith('>'):
                #When the loop encounters the last line of a sequence (i.e., the next line starts with '>'), or when it reaches the end of the file, it calculates the GC content of the current sequence.
                #The GC content is calculated using the formula: gc = (count('G') + count('C')) / len(sequence) * 100. This calculates the percentage of GC content in the sequence.
                gc = 100 * (sequence.count('G') + sequence.count('C')) / len(sequence)
                if gc > max_gc:
                #If the calculated GC content (gc) is greater than the previous maximum (max_gc), it updates the max_gc and max_id variables with the new values.
                #This keeps track of the sequence with the highest GC content encountered so far.
                    max_gc = gc
                    max_id = id
#After processing all the lines in the file, the code prints the identifier (max_id) and the maximum GC content (max_gc).
#The code effectively scans through a FASTA file, calculates the GC content for each DNA sequence, and keeps track of the sequence with the highest GC content.It then reports the ID and GC content of that sequence.
print(max_id, end='')
print(max_gc)