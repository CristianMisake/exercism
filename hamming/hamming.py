def distance(strand_a, strand_b):
    if len(strand_a) == len(strand_b):
        cont = 0
        for i in range(len(strand_a)):
            if strand_a[i] != strand_b[i]:
                cont += 1
        return cont
    else:
        raise ValueError('Los valores no concuerdan')
