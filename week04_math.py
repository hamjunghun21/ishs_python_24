def is_prime_number(n) -> bool:
    """
    Prime number decision function
    :param n: positive integer
    :return: True if k is prime number, False otherwise
    """
    if n < 2:
        return False
    else:
        i = 2
        while i*i <= n: # reduce loop operation
            if n % i == 0:
                return False # Calculate with boolean operator instead of addition operation
            i += 1 # Increment i by 1
        return True

def power(b, e) -> int:
    """
    Power function
    :param b: base number
    :param e: exponent number
    :return: power result value
    """
    result = 1
    for _ in range(e):
        result = result * b
    return result

while True:
    menu = int(input("1) prime number 2) power 3) divmod 4) quit :")) #ValueError: invalid literal for int() with base 10: '에헤'
    if menu == 1:
        start, end = list(map(int, input("start number and end number: ").split()))
        for k in range(start, end + 1):
            if is_prime_number(k):
                print(k, end=" ")
    elif menu == 2:
        base, exponent = map(int, input("i:").split())
        print(f"{base}^{exponent} = {power(base, exponent)}")
    elif menu == 3:
        dividend, divisor = map(int, input("Input dividend & divisor number: ").split())
        print(f"{dividend} // {divisor} = {divmod(dividend, divisor)[0]}")
        print(f"{dividend} % {divisor} = {divmod(dividend, divisor)[1]}")
    elif menu == 4:
        print("exit progress")
        exit() #or break()
    else:
        print("Please choose from the menu")