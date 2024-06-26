def print_fx(fx):
    texts = "f(x) = "
    expo = len(fx) - 1

    for i in range(len(fx)):
        coef = fx[i]

        if coef == 0:
            expo = expo -1
            continue

        if coef > 0 and i != 0:
            texts = texts + "+"

        #texts = texts + str(coef) +"x^" + str(expo) + " "
        texts = texts + f"{coef}x^{expo}"
        expo = expo - 1
    return texts

def input_fx(fx, x):
    sum_ = 0
    expo = len(fx) - 1
    for i in range(len(fx)):
        sum_ += fx[i] * (x**expo)
        expo -= 1
    return sum_

def calculat_fx(fx, x):
    expo = len(fx) - 1
    result = 0

    for k in range(len(fx)):
        coef = fx[k]
        result = result + coef * x ** expo
        expo = expo - 1
    return result

coefficient = [5, -2, 0, 6]

print(print_fx(coefficient))
x = int(input("Input x value : "))
print(input_fx(coefficient, x))
print(calculat_fx(coefficient,x))
