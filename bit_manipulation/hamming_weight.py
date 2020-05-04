def hamming_weight(n):
    bits = 0
    mask = 1
    for _ in range(32):
        if (n & mask) != 0:
            bits += 1
        mask <<= 1
    return bits
