import random
arra = [random.randint(0, 88) for i in range(10)]
print(arra)
z = (int(input("Введите порядковый номер числа")))
arra[z] = z
print(arra)
