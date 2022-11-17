# a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
#
# if b1 < a2 or b2 < a1:
#     print('пустое множество')
# elif a1 <= a2 and b1 <= b2 and a2 < b1:
#     print(f'{a2} {b1}')
# elif a2 <= a1 and b2 <= b1 and a1 < b2:
#     print(f'{a1} {b2}')
# elif a1 == a2 and b1 == b2:
#     print(f'{a1} {b1}')
# elif a1 < a2 and b1 < b2 and a2 == b1:
#     print(f'{a2}')
# elif a1 > a2 and b1 > b2 and a1 == b2:
#     print(f'{a1}')
# elif a1 < a2 and b2 < b1:
#     print(f'{a2} {b2}')
# elif a1 > a2 and b2 > b1:
#     print(f'{a1} {b1}')


# date = int(input())
# var = date % 100
#
# if var == 0:
#     print('YES')
# else:
#     print('NO')


# a1, a2, b1, b2 = int(input()), int(input()), int(input()), int(input())
# farbe1, farbe2 = '', ''
#
# if (a1 % 2 == 0 and a2 % 2 == 0) or (a1 % 2 != 0 and a2 % 2 != 0):
#     farbe1 = 'white'
# elif (a1 % 2 != 0 and a2 % 2 == 0) or (a1 % 2 == 0 and a2 % 2 != 0):
#     farbe1 = 'black'
#
# if (b1 % 2 == 0 and b2 % 2 == 0) or (b1 % 2 != 0 and b2 % 2 != 0):
#     farbe2 = 'white'
# elif (b1 % 2 != 0 and b2 % 2 == 0) or (b1 % 2 == 0 and b2 % 2 != 0):
#     farbe2 = 'black'
#
# if farbe1 == farbe2:
#     print('YES')
# else:
#     print('NO')


# age = int(input())
# pol = input()
#
# if (10 <= age <= 15) and pol == 'f':
#     print('YES')
# else:
#     print('NO')


# var = int(input())
# dick: dict = {'1': 'I', '2': 'II', '3': 'III', '4': 'IV', '5': 'V', '6': 'VI', '7': 'VII', '8': 'VIII', '9': 'IX', '10': 'X'}
#
# if 1 <= var <= 10:
#     print(dick[str(var)])
# else:
#     print('ошибка')


# var = int(input())
#
# if var % 2 != 0 or (var % 2 == 0 and 6 <= var <= 20):
#     print('YES')
# elif (var % 2 == 0 and 2 <= var <= 5) or (var % 2 == 0 and var > 20):
#     print('NO')
# a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
#
# arr: list = []
# SUM1 = a1 + b1
# sum2 = a2 + b2
#
# if SUM1 == sum2:
#     print('YES')
# else:
#     if a1 == 1 or b1 == 1:
#         pass
#     elif a1 == b1:
#         a1 = b1 = 1
#     elif a1 > b1:
#         a1 = (a1 - b1) + 1
#         b1 = 1
#     else:
#         b1 = (b1 - a1) + 1
#         a1 = 1
#
#     while True:
#         sum1 = a1 + b1
#
#         if sum1 == SUM1 or (sum1 == sum2 and a1 != a2):
#             a1 += 1
#             b1 += 1
#             continue
#
#         arr.append(sum1)
#
#         a1 += 1
#         b1 += 1
#         if a1 > 8 or b1 > 8:
#             break
#
#     if sum2 in arr:
#         print('YES')
#     else:
#         print('NO')


# a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
#
# if (a1 + 1 == a2 or a1 - 1 == a2) and (b1 + 2 == b2 or b1 - 2 == b2):
#     print('YES')
# elif (a1 + 2 == a2 or a1 - 2 == a2) and (b1 + 1 == b2 or b1 - 1 == b2):
#     print('YES')
# else:
#     print('NO')

# a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
#
# if (a1 - b1) ** 2 == (a2 - b2) ** 2:
#     print("1 YES")
# elif a1 == a2 or b1 == b2:
#     print('2 YES')
# else:
#     print("NO")


# a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
#
# arr: list = []
# SUM1 = a1 + b1
# sum2 = a2 + b2
#
# if SUM1 == sum2:
#     print('YES')
# elif a1 == a2 or b1 == b2:
#     print('YES')
# else:
#     if a1 == 1 or b1 == 1:
#         pass
#     elif a1 == b1:
#         a1 = b1 = 1
#     elif a1 > b1:
#         a1 = (a1 - b1) + 1
#         b1 = 1
#     else:
#         b1 = (b1 - a1) + 1
#         a1 = 1
#
#     while True:
#         sum1 = a1 + b1
#
#         if sum1 == SUM1 or (sum1 == sum2 and a1 != a2):
#             a1 += 1
#             b1 += 1
#             continue
#
#         arr.append(sum1)
#
#         a1 += 1
#         b1 += 1
#         if a1 > 8 or b1 > 8:
#             break
#
#     if sum2 in arr:
#         print('YES')
#     else:
#         print('NO')
