import re
import tracemalloc

# def validateDNA(pattern, seq):
#     if re.match(pattern,seq):
#         return True
#     else:
#         return False
    
dna = "actggacta"
tracemalloc.start()
result = re.search("{^CAGTcagt]+$", dna)
print (result)
print(tracemalloc.get_traced_memory())
tracemalloc.stop()

if result:
    print("MATCH")
else:
    print("T_T")

