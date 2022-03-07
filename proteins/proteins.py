from Bio import SeqIO
import pandas as pd
from collections import Counter


prot = SeqIO.read("P43681.fasta", "fasta")
print(f"""

    Protein length: {len(prot)}
    {Counter(prot.seq.__str__())}
""")