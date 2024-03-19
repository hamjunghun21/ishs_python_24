def is_prime_number(n) -> bool:
    """
    Prime number decision function
    :param n: positive integer
    :return: True if n is prime number, False otherwise
    """
    pass


start, end = list(map(int, input("start number and end number: ").split()))

for k in range(start, end+1):
    is_prime_number = True # Change variable name from cnt to is_prime_number for readability.
    if k < 2:
        is_prime_number = False
    else:
        i = 2
        while i*i <= k:
            if k % i == 0:
                is_prime_number = False # Calculate with boolean operator instead of addition operation
                break # The loop ends when the first divisor is found.
            #print(i, end = " ")
            i += 1 # Increment i by 1
        if is_prime_number: print(k, end = " ")