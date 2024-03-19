def is_prime_number(k) -> bool:
    """
    Prime number decision function
    :param k: positive integer
    :return: True if k is prime number, False otherwise
    """
    if k < 2:
        return False
    else:
        i = 2
        while i*i <= k: # reduce loop operation
            if k % i == 0:
                return False # Calculate with boolean operator instead of addition operation
            i += 1 # Increment i by 1
        return True


start, end = list(map(int, input("start number and end number: ").split()))

for k in range(start, end + 1):
    if is_prime_number(k):
        print(k, end = " ")