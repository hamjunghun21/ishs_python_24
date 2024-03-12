number = int(input("number: "))

cnt = 0
for i in range(2, number):
    if number % i == 0:
        cnt += 1

if cnt == 0:
    print(f"{number} is prime number")
else:
    print(f"{number} is not prime number")