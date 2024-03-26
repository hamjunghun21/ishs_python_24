def print_fx(fx):
    texts = "f(x) = "
    expo = len(fx) - 1

    for i in range(len(fx)):
        coef = fx[i]
        if coef == 0:
            continue
            expo = expo - 1

        if coef >= 0 and i != 0:
            texts = texts + "+"

        texts = texts + str(coef) +"x^" + str(expo) + " "
        expo = expo - 1
    return texts

coefficient = [5, -2, 0, 6]

print(print_fx(coefficient))