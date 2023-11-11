from Bio import SeqIO
from Bio.Seq import Seq

my_dna = Seq("ACGTTT")

# Read the input file in FASTA format
records = list(SeqIO.parse("input.fasta1.py", "fasta"))

# Get the DNA string
dna_string = records[0].seq

# Remove introns
introns = [str(record.seq) for record in records[1:]]
for intron in introns:
    dna_string = dna_string.replace(intron, '')

# Transcribe DNA to RNA
rna_string = dna_string.transcribe()

# Translate RNA to protein
protein_string = rna_string.translate(table="Standard", to_stop=True)

# Print the result
print(protein_string)
