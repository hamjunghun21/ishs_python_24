start = int(input("start number: "))
end = int(input("end number: "))

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