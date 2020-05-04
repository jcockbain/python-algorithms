def find_complement(n):
    todo, bit = n, 1
    while todo:
        n = n ^ bit
        bit = bit << 1
        todo = todo >> 1
    return n
