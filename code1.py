def count_bits(n):
    p = 0
    n = bin(n)
    for el in n:
        if el == '1':
            p+=1
    return p

print(count_bits(1234))
