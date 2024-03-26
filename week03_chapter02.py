a = 7 # a가 7을 참조
b = a
a = a + 24
print(a,b)
print(id(a), id(b))
b = 256
print(a,b)
print(id(a), id(b))
print(type(a), type(b))