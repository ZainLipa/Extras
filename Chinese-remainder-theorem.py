def chinese_remainder_theorem(n, a):
    """
    Solve a system of linear congruences using the Chinese remainder theorem.
    
    Args:
    n (list): A list of integers representing the moduli of the congruences.
    a (list): A list of integers representing the residues of the congruences.
    
    Returns:
    An integer x that satisfies all the congruences.
    """
    # Compute N as the product of all the moduli.
    N = 1
    for ni in n:
        N *= ni
    
    # Compute the list of Ni values, where Ni = N/ni.
    Ni = [N // ni for ni in n]
    
    # Compute the list of mi values, where mi is the inverse of Ni modulo ni.
    mi = [pow(Ni[i], -1, n[i]) for i in range(len(n))]
    
    # Compute the solution x as the sum of ai*Ni*mi for each i.
    x = 0
    for i in range(len(n)):
        x += a[i] * Ni[i] * mi[i]
    
    # Reduce x modulo N to get the smallest positive integer that satisfies all  congruences.
    return x % N
