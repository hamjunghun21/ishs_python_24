number = int(input("number: "))

cnt = 0
for i in range(1, number+1):
    if number % i == 0:
        cnt += 1

if cnt == 2:
    print(f"{number} is prime number")
else:
    print(f"{number} is not prime number")