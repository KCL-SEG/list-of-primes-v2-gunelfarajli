"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes < 1:
        raise ValueError(" The number must be positive.")
    val = 2
    num_list = []

    while len(num_list) < number_of_primes:
        if is_prime(val):
            num_list.append(val)
        val+=1
    
    return num_list

def is_prime(value):
    is_Prime = True
    new_val = int(value**0.5)
    if value < 2:
        is_Prime = False
    for i in range(2, (new_val +1)):
        if value % i == 0:
            is_Prime = False
    
    return is_Prime