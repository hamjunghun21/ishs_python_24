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

base, exponent = map(int,input("i:").split())
print(f"{base}^{exponent} = {base**exponent}")
print(f"{base}^{exponent} = {pow(base, exponent)}") #built in fuction
print(f"{base}^{exponent} = {power(base, exponent)}") #custom fuction
