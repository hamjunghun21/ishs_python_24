dividend, divisor = map(int,input("Input dividend & divisor number: ").split())

print(f"{dividend} // {divisor} = {dividend // divisor}")
print(f"{dividend} % {divisor} = {dividend % divisor}")

print(divmod(dividend, divisor)) #return tuple

print(f"{dividend} // {divisor} = {divmod(dividend, divisor)[0]}")
print(f"{dividend} % {divisor} = {divmod(dividend, divisor)[1]}")

