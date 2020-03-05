def to_rna(dna_strand):
    resp = ''
    rna = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U'
    }
    for dna in dna_strand:
        resp += rna[dna]
    return resp
