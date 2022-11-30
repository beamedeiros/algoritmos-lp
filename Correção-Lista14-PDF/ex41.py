def comum(seq1, seq2):
    res = []
    for x in seq2:
        if x in seq2:
            res.append(x)
    return res
