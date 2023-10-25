#I use aa_mass dictionary to associate each amino acid symbol with its corresponding molecular mass in Daltons (Da). 
#This information is based on the average molecular weights of the individual amino acids.
aa_mass = {
        "A":71.03711, "C":103.00919, "D":115.02694, "E":129.04259, "F":147.06841,
        "G":57.02146, "H":137.05891, "I":113.08406, "K":128.09496, "L":113.08406,
        "M":131.04049, "N":114.04293, "P":97.05276, "Q":128.05858, "R":156.10111,
        "S":87.03203, "T":101.04768, "V":99.06841, "W":186.07931, "Y":163.06333}

with open("prtm11.py", "r") as file:
    p = file.readline().strip()
    #I calculate the molecular weight of the protein sequence by iterating through each amino acid in the sequence and looking up its mass in the aa_mass dictionary. 
    #The weight has been calculated as the sum of the masses of individual amino acids in the sequence.
    #I use a list comprehension to loop through each character (i) in the protein sequence (p).
    #For each amino acid symbol, the code looks up its mass in the aa_mass dictionary and collects these masses in a list.
    #Then I use the sum function to add up the individual masses, resulting in the total molecular weight of the protein sequence.
    #The calculated molecular weight is stored in the variable weight.
    weight = sum([aa_mass[i] for i in p])
    print(weight)
    #the result represents the total molecular weight of the protein sequence.