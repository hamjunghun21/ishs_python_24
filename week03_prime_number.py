number = int(input("number: "))

is_prime_number = True # Change variable name from cnt to is_prime_number for readability.
if number < 2:
    is_prime_number = False
else:
    i = 2
    while i*i <= number: # bug fix
        if number % i == 0:
            is_prime_number = False # Calculate with boolean operator instead of addition operation
            break # The loop ends when the first divisor is found.
        #print(i, end = " ")
        i += 1 # Increment i by 1
if is_prime_number: # Remove comparison operators
    print(f"{number} is prime number")
else:
    print(f"{number} is not prime number")