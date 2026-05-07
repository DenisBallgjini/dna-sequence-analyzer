def analyze_dna(sequence):
    sequence = sequence.upper()

    valid_bases = {"A", "C", "G", "T"}

    for base in sequence:
        if base not in valid_bases:
            print("Error: Only A, C, G, T allowed.")
            return

    a_count = sequence.count("A")
    c_count = sequence.count("C")
    g_count = sequence.count("G")
    t_count = sequence.count("T")

    total_length = len(sequence)

    gc_content = ((g_count + c_count) / total_length) * 100

    print("\n=== DNA Analysis Results ===")
    print(f"Adenine (A):  {a_count}")
    print(f"Cytosine (C): {c_count}")
    print(f"Guanine (G):  {g_count}")
    print(f"Thymine (T):  {t_count}")

    print(f"\nTotal Length: {total_length} bases")
    print(f"GC Content:   {gc_content:.2f}%")


dna = input("Enter DNA sequence: ")
analyze_dna(dna)
