def read_sequences(filename):
    f=open(filename)
    lines=f.readlines()
    lines[-1]+="\n"
    lines.append(">")
    f.close()
    seqs=[]
    myseq=""
    for i in lines[1:]:
        if i[0]==">":
            seqs.append(myseq)
            myseq=""
        else:
            myseq+=i[:-1]
    return seqs

#I use the read_sequences function to read sequences from the file "tran3.py." The code assumes there are two sequences in the rosalind file.
#It assigns the first sequence to s1 and the second sequence to s2.
seqs=read_sequences("tran3.py")
s1=seqs[0]
s2=seqs[1]
#define lists pur and pyr to represent purine (A, G) and pyrimidine (C, T) bases, respectively.
pur=["A","G"]
pyr=["C","T"]
#The nuc dictionary maps each nucleotide (A, G, C, T) to its corresponding category (purine or pyrimidine).
nuc={"A":"pur","G":"pur","C":"pyr","T":"pyr"}

transition=0.
transversion=0.
#initialize variables transition and transversion to keep track of the number of transitions and transversions, respectively.
#iterate through the positions of s1 and s2 and compare the corresponding nucleotides.
#if the nucleotides are different, check whether they are a transition or a transversion based on the nuc dictionary. 
#If they belong to the same category (both purines or both pyrimidines), it's a transition; otherwise, it's a transversion.
#update the transition and transversion counts accordingly.
#Calculate and Printing the Transition/Transversion Ratio.
for i in range(0,len(s1)):
    n1=s1[i]
    n2=s2[i]
    if n1!=n2:
        if nuc[n1]==nuc[n2]:
            transition+=1
        else: transversion+=1

print (transition/transversion)
