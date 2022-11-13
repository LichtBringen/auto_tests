# a, b = float(input()), float(input())
# S = 0.5 * a * b
# print(S)


# S, V1, V2 = float(input()), float(input()), float(input())
# var = S / (V1 + V2)
# print(var)


# var = float(input())
# if var == 0:
#     print('Обратного числа не существует')
# else:
#     print(var**(-1))


# F = float(input())
# C = (5 / 9) * (F - 32)
# print(C)


# age_dog = float(input())
#
# arr = [i for i in range(1, int(age_dog) + 1)]
# age_hum: float = 0
# for i in arr:
#     if i == 1 or i == 2:
#         age_hum += 10.5
#     elif i > 2:
#         age_hum += 4
# print(age_hum)


# var = float(input())
# a = int(var)
# b = (var - a) * 10
# print(int(b))


# var = float(input())
# a = int(var)
# b = var - a
# print(b)


# arr: list = [int(input()) for i in range(5)]
# print(f'Наименьшее число = {min(arr)} \nНаибольшее число = {max(arr)}')


# arr: list = [int(input()) for i in range(3)]
# arr.sort(), arr.reverse()
# arr = [print(i) for i in arr]


# var = int(input())
# arr: list = [(var % 10**(i+1))//10**i for i in range(3)]
# arr.sort()
#
# a = max(arr)
# b = arr[1]
# c = min(arr)
#
# if (a - c) == b:
#     print('Число интересное')
# else:
#     print('Число неинтересное')


# arr: list = [float(input()) for i in range(5)]
# um: float = 0
# for i in arr:
#     um += abs(i)
# print(um)


# a1, a2, q1, q2 = [int(input()) for i in range(4)]
# ran = abs(a1 - q1) + abs(a2 - q2)
# print(ran)
# arr: list = [len(input()) for i in range(3)]
# arr.sort()
# step = arr[1] - arr[0]
# if step + arr[1] == arr[2]:
#     print('YES')
# else:
#     print('NO')
# print(arr)

# Stadt1, Stadt2, Stadt3 = input(), input(), input()
# arr: list = [Stadt1, Stadt2, Stadt3]
#
# var_min = min(len(Stadt1), len(Stadt2), len(Stadt3))
# var_max = max(len(Stadt1), len(Stadt2), len(Stadt3))
#
# print(var_min, var_max) #dellllllllllll
#
# # arr: list = ['Москва', 'Санкт-Петербург', 'Екатеринбург']
#
#
# log =
# for i in arr:
#     if len(i) == var_min:
#         print(f'{i}')
#     elif len(i) == var_max:
#         print(f'{i}')
# print(arr)

# len(Stadt1), len(Stadt2), len(Stadt3)
# Stadt1, Stadt2, Stadt3

# Москва
# Санкт-Петербург
# Екатеринбург


# wort = input()
# if '@' in wort and '.' in wort:
#     print('YES')
# else:
#     print('NO')

# import math
# X1, X2, X3, X4 = [float(input()) for i in range(4)]
# print(math.sqrt((X1 - X3)**2 + (X2 - X4)**2))


# import math
# R = float(input())
# S = math.pi * R**2
# C = 2 * math.pi * R
# print(S, C, sep='\n')


# import math
# a, b = float(input()), float(input())
#
# f1 = (a + b) / 2
# f2 = math.sqrt(a * b)
# f3 = (2 * a * b) / (a + b)
# f4 = math.sqrt((a**2 + b**2) / 2)
#
# print(f1, f2, f3, f4, sep='\n')


# import math
# x = math.radians(float(input()))
# tr = math.sin(x) + math.cos(x) + math.tan(x)**2
# print(tr)


# import math
# var = float(input())
# print(math.floor(var) + math.ceil(var))


# import math
# a, b, c = [float(input()) for i in range(3)]
#
# D = b**2 - 4 * a * c
#
# if D > 0:
#     x1 = (-b + math.sqrt(D)) / (2 * a)
#     x2 = (-b - math.sqrt(D)) / (2 * a)
#     print(min(x1, x2), max(x1, x2), sep='\n')
# elif D == 0:
#     x = -b / (2 * a)
#     print(x)
# elif D < 0:
#     print('Нет корней')


# import math
# n, a = float(input()), float(input())
# print((n * a**2) / (4 * math.tan(math.pi / n)))

