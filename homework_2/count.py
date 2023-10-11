from Bio import AlignIO
alignment=AlignIO.read(open("alignment.fa"), 'fasta')
seq1=str(alignment[0].seq)
seq2=str(alignment[1].seq)
matches = sum(nuc1 == nuc2 for nuc1, nuc2 in zip(seq1, seq2))
identity = 100.0 * matches / len(seq1)
print(100 - identity)
