import random

y = [random.randint(0, 9) for i in range(10)]
print(y)

z = int(input("Введите число : "))
b = y.index(z)
print("число " + str(z) + 'находится в списке под номером ' + str(b))
