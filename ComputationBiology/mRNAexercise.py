def validate_dna(dna_seq):
    seqm = dna_seq.upper()
    print(seqm)

    valid = seqm.count("A") + seqm.count("T") + seqm.count("C") + seqm.count("G")
    if valid == len(seqm):
        print("VALID")
        return True
    else:
        print("INVALID")
        return False
    
def convertDna(dna_seq):
    complement = ""
    complement_pairs = {"A":"T", "T":"A", "C":"G", "G":"C"}

    for i in dna_seq.upper():
        complement += complement_pairs[i]

    return complement

def convertComplement(complement_seq):
    mRNA = ""
    pairs = {"T":"U"}

    for i in complement_seq:
        if i in pairs:
            mRNA += pairs[i]
        else:
            mRNA += i

    return mRNA

def convertAminoAcid(mRNA):
    AminoAcid = ''
    geneticCode = {
        'UUU': 'Phe (F)', 'UUC': 'Phe (F)', 'UUA': 'Leu (L)', 'UUG': 'Leu (L)',
        'UCU': 'Ser (S)', 'UCC': 'Ser (S)', 'UCA': 'Ser (S)', 'UCG': 'Ser (S)',
        'UAU': 'Tyr (Y)', 'UAC': 'Tyr (Y)', 'UAA': 'STOP', 'UAG': 'STOP',
        'UGU': 'Cys (C)', 'UGC': 'Cys (C)', 'UGA': 'STOP', 'UGG': 'Trp (W)',
        'CUU': 'Leu (L)', 'CUC': 'Leu (L)', 'CUA': 'Leu (L)', 'CUG': 'Leu (L)',
        'CCU': 'Pro (P)', 'CCC': 'Pro (P)', 'CCA': 'Pro (P)', 'CCG': 'Pro (P)',
        'CAU': 'His (H)', 'CAC': 'His (H)', 'CAA': 'Gln (Q)', 'CAG': 'Gln (Q)',
        'CGU': 'Arg (R)', 'CGC': 'Arg (R)', 'CGA': 'Arg (R)', 'CGG': 'Arg (R)',
        'AUU': 'Ile (I)', 'AUC': 'Ile (I)', 'AUA': 'Ile (I)', 'AUG': 'Met (M)',
        'ACU': 'Thr (T)', 'ACC': 'Thr (T)', 'ACA': 'Thr (T)', 'ACG': 'Thr (T)',
        'AAU': 'Asn (N)', 'AAC': 'Asn (N)', 'AAA': 'Lys (K)', 'AAG': 'Lys (K)',
        'AGU': 'Ser (S)', 'AGC': 'Ser (S)', 'AGA': 'Arg (R)', 'AGG': 'Arg (R)',
        'GUU': 'Val (V)', 'GUC': 'Val (V)', 'GUA': 'Val (V)', 'GUG': 'Val (V)',
        'GCU': 'Ala (A)', 'GCC': 'Ala (A)', 'GCA': 'Ala (A)', 'GCG': 'Ala (A)',
        'GAU': 'Asp (D)', 'GAC': 'Asp (D)', 'GAA': 'Glu (E)', 'GAG': 'Glu (E)',
        'GGU': 'Gly (G)', 'GGC': 'Gly (G)', 'GGA': 'Gly (G)', 'GGG': 'Gly (G)'
        }
    
        # Split the input into codons (triplets)
    codons = [mRNA[i:i+3] for i in range(0, len(mRNA), 3)]

    for codon in codons:
            # Check if the codon exists in the geneticCode dictionary
        if codon in geneticCode:
            amino_acid = geneticCode[codon]
            # Check if it's a STOP codon
            if amino_acid == 'STOP':
                amino_acid = "*"
                break  # STOP codon indicates the end of translation
            AminoAcid += amino_acid
            AminoAcid += " - "

    return AminoAcid

# print(convertAminoAcid("AUGUAGACAUCGGA"))

inputSequence = "atgcaaatggtaa"
validate_result = validate_dna(inputSequence)
if validate_result == True:
    complementSequence = convertDna(inputSequence)
    print("Complement Sequence:", complementSequence)

    mRNASequence = convertComplement(complementSequence)
    print("mRNA Sequence:", mRNASequence)

    aminoAcidSequence = convertAminoAcid(mRNASequence)
    print("Amino Acid Sequence:", aminoAcidSequence)

# ---------------------------------------------------------------
# --------------------------NUMBER 2-----------------------------
# ---------------------------------------------------------------
print("\n----------------------------------------------------\n")

codonMapping = {
    'A': ['GCU', 'GCC', 'GCA', 'GCG'],
    'R': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
    'N': ['AAU', 'AAC'],
    'D': ['GAU', 'GAC'],
    'C': ['UGU', 'UGC'],
    'Q': ['CAA', 'CAG'],
    'E': ['GAA', 'GAG'],
    'G': ['GGU', 'GGC', 'GGA', 'GGG'],
    'H': ['CAU', 'CAC'],
    'I': ['AUU', 'AUC', 'AUA'],
    'L': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'],
    'K': ['AAA', 'AAG'],
    'M': ['AUG'],
    'F': ['UUU', 'UUC'],
    'P': ['CCU', 'CCC', 'CCA', 'CCG'],
    'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],
    'T': ['ACU', 'ACC', 'ACA', 'ACG'],
    'W': ['UGG'],
    'Y': ['UAU', 'UAC'],
    'V': ['GUU', 'GUC', 'GUA', 'GUG'],
    '*': ['UAA', 'UAG', 'UGA']
}

def translateTomRNA(aminoAcidSeq):
    sequence = ''
    for char in aminoAcidSeq:
        if char.isalpha():
            sequence += char.upper()
    # return sequence
    rnaSequence = ""
    for i in sequence:
        rnaSequence += codonMapping[i][0]
    return rnaSequence

def calculateFrequency(sequence):
    dictionary = {}

    for i in range(0,len(sequence),3):
        codon = sequence[i:i +3].upper()
        if codon in dictionary:
            dictionary[codon]+=1
        else:
            dictionary[codon] = 1

    return dictionary

inputSequence2 = "n_A-N"
convertmRNA = translateTomRNA(inputSequence2)
print("mRNA:",convertmRNA)
frequencyDict = calculateFrequency(convertmRNA)
print("Codon Frequency:", frequencyDict)
