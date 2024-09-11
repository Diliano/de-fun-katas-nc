def dna_pairs(dna_string):
    pairs = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C"
    }
    return [[dna, pairs[dna]] for dna in dna_string if dna in pairs]