def findPattern(pattern, seq):
    length = len(pattern)
    n = len(seq)
    result = []
    
    for i in range(n-length+1):
        j = 0

        while (j < length):
            if (seq[i+j]!= pattern[j]):
                break
            j += 1

        if (j == length):
            result.append(i)

    print("BIMBIMBAMBAM = ", result)

dna = "ATGAACACGAATAAGAA" #A-T-G-C
pattern = "GAA"

findPattern(pattern, dna)
