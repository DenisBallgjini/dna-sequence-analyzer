def analyze_dna(sequence):
    sequence = sequence.upper()

    valid_bases = {"A", "C", "G", "T"}

    for base in sequence:
        if base not in valid_bases:
            print("Error: Only A, C, G, T allowed.")
            return

    print("A:", sequence.count("A"))
    print("C:", sequence.count("C"))
    print("G:", sequence.count("G"))
    print("T:", sequence.count("T"))
    print("Total length:", len(sequence))


dna = input("Enter DNA sequence: ")
analyze_dna(dna)
