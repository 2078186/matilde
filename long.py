def calculate_overlap(string1, string2):
    #This function calculates the maximum overlap between two input strings, string1 and string2. 
    #It does so by comparing suffixes of string1 with prefixes of string2 and finding the longest matching overlap. The function returns the length of this maximum overlap.
    max_overlap = 0
    for i in range(1, min(len(string1), len(string2)) + 1):
        if string1[-i:] == string2[:i]:
            max_overlap = i
    return max_overlap

def find_shortest_superstring(strings):
    #This function finds the shortest superstring containing all input DNA strings from the strings list.
    #It uses a greedy algorithm to iteratively merge the two strings with the maximum overlap until only one superstring remains.
    while len(strings) > 1:
        max_overlap = 0
        pair_to_merge = (0, 1)
        
        for i in range(len(strings)):
            for j in range(i + 1, len(strings)):
                overlap = calculate_overlap(strings[i], strings[j])
                if overlap > max_overlap:
                    max_overlap = overlap
                    pair_to_merge = (i, j)
        
        # Merge the two strings with the maximum overlap
        i, j = pair_to_merge
        merged_string = strings[i] + strings[j][max_overlap:]
        strings = strings[:i] + strings[i+1:j] + strings[j+1:]
        strings.append(merged_string)

    return strings[0]

# Read input DNA strings from FASTA format
def read_fasta(file_path):
    sequences = []
    with open(file_path, 'r') as file:
        current_sequence = ''
        for line in file:
            if line.startswith('>'):
                if current_sequence:
                    sequences.append(current_sequence)
                current_sequence = ''
            else:
                current_sequence += line.strip()
        if current_sequence:
            sequences.append(current_sequence)
    return sequences

# Read the input from a file
input_file = "input3.py"
sequences = read_fasta(input_file)

# Find the shortest superstring
shortest_superstring = find_shortest_superstring(sequences)

# Write the result to an output file
output_file = "output.txt"
with open(output_file, 'w') as file:
    file.write(shortest_superstring)

