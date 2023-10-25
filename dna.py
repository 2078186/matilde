sequence='TTGTTGCTAGAGGCTTGCGGTGGTCTTATTTAGGGGCCACAGCCGTTAGTACCCTCCCACTCCACTGAATTGCGTCCAGGAGGTGCTATGGAGATACGTCCGCCCCGTGTGAGGAGTAAAAAACCACTCACGATCAAAATACTGAAGTGGCAGATCATTCGGATGGTTGCCCTTCCATAGGATAAAGAGGGGTGTAACCATCATGGTCTGCCATAGCAGTTAAATTAAACAATTTACACCTGATAAATGGTTCCTTGATACTTGAATACGCGATAGAAATGAAATAACGTTCGGCATCAGTGGCAGCAGAAACCCTAGCCGGCTAGGAGTAATGATCATGACGCATGTGTATGCTCGACCTCAAGGGGCGCAATACACAAGTAGGCGTACAAGGATTGGACATTTATGCAGCATAAGGGTACTATTACTGACTTCAAACCCGCTCCCGGTCATCCTACACACGACCGCTTTTTACATGCGCAGTGAGATAATACCATGAATTTACCCTTATTACTGCCGAATTTTCGCCCATTGGGGATACATCGCATTGGCAGTAATGTACCCTGGGAAAAGTTCGGCTACGTGGCGGCGCCCAGCCGGACACCGCGGTTATGCGCCACGGCTCCCACCTCCCCAATTTCCCACTCAAAACGGCGATGTATAGCCTCTATTCCGTGCCGAGTGGGTCTAATCGGGTTAATTCATTTATATTCGAGGGGCCTCTGGCCTATCGGTGCGTTTCGGAGAGGTAGCTTAAAAGTTAGAGTAACACATTCCGTGGGATTGGGTCACTGTGGGCTACGATATACAATAGTCCCCAGTGGCTGAAGACGGAAGGACTCTGATCGTGTTGACACGCAACACAATACCGAATGCGTCCATTTTTAGACACAAATAGCTCTTGACGAGCCATCCCCCGTAGTACAGGAAA'
#initialize four variables, a, g, c, and t, to zero. These variables will be used to keep track of the counts of each symbol 'A', 'G', 'C', and 'T' in the DNA string.
a = 0
g = 0
c = 0
t = 0
#use a for loop to iterate through each character (symbol) in the sequence string.
for symbol in sequence:
#Inside the loop, check each character (symbol) using conditional statements (if-elif-else) to determine which symbol it is. Depending on the symbol, you increment the respective counter. This is how the counts are updated during each iteration of the loop.
#If the current symbol is 'A', the a counter is incremented.
#If the current symbol is 'G', the g counter is incremented.
#If the current symbol is 'C', the c counter is incremented.
#If the current symbol is not 'A', 'G', or 'C' (which means it's 'T' in this case), the t counter is incremented.
    if symbol == 'A':
        a = a+1
    elif symbol == 'G':
        g = g+1
    elif symbol == 'C':
        c = c+1
    else:
        t = t+1
#After the loop has iterated through the entire sequence string, print the counts of 'A', 'C', 'T', and 'G' in the desired format. Use the str() function to convert the counts to strings and concatenate them with spaces to create a single string that represents the counts in the required format.
#str(a): Converts the count of 'A' to a string.
#str(c): Converts the count of 'C' to a string.
#str(t): Converts the count of 'T' to a string.
#str(g): Converts the count of 'G' to a string.
#Then, concatenate these strings using the + operator and add spaces to format them as "A C T G."
print (str(a)+ ' ' + str(c) + ' ' + str(t) + ' ' +str(g))
#The results will represent the counts of 'A', 'C', 'T', and 'G' in the DNA sequence, respectively.
