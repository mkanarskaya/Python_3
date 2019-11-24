import math
print(math.factorial(1000))
print((2 ** 25 + 1) / 2)
print([i for i in range(10**6) if i % 2 == 0 and not(i % 7 == 0) and str(i)[0:3] == "793"])
print(str(input("Введите строку: ")) [::-1])
print([i*2 if i % 2 else i for i in [1, 4, 6, 3, 8, 0]])
