# text = input()
# while text != 'КОНЕЦ' and text != 'конец':
#     print(text)
#     text = input()


# text = input()
# count = 0
# while text != 'стоп' and text != 'хватит' and text != 'достаточно':
#     text = input()
#     count += 1
# print(count)


# var = int(input())
# while var % 7 == 0:
#     print(var)
#     var = int(input())


# var = int(input())
# count = 0
# while var >= 0:
#     count += var
#     var = int(input())
# print(count)


# var = int(input())
# count = 0
# while 0 <= var <= 5:
#     if var == 5:
#         count += 1
#     var = int(input())
# print(count)


# var = int(input())
# count = 0
# if var >= 25:
#     count += var // 25
#     var %= 25
#
# if var >= 10:
#     count += var // 10
#     var %= 10
#
# if var >= 5:
#     count += var // 5
#     var %= 5
#
# if var >= 1:
#     count += var // 1
#
# print(count)


# n = int(input())
# while n != 0:
#     count = n % 10
#     print(count)
#     n //= 10


# var = int(input())
# n = len(str(var))
# var_new = 0
# while n != 0:
#     var_new += (var % 10) * 10**(n-1)
#     var //= 10
#     n -= 1
# print(var_new)


# n = int(input())
# var_max = 0
# var_min = n % 10
# while n != 0:
#     b = n % 10
#     if b >= var_max:
#         var_max = b
#     elif b < var_min:
#         var_min = b
#     n //= 10
# print(f'Максимальная цифра равна {var_max}\nМинимальная цифра равна {var_min}')


# сумму его цифр;
# количество цифр в нем;
# произведение его цифр;
# среднее арифметическое его цифр;
# его первую цифру;
# сумму его первой и последней цифры


# n = int(input())
# sum_var = 0
# c = 1
# col = len(str(n))
# a = n // 10**(col - 1)
# b = (n // 10**(col - 1)) + n % 10
# while n != 0:
#     var = n % 10
#     sum_var += var
#     c *= var
#     n //= 10
# print(sum_var, col, c, float(sum_var/col), a, b, sep='\n')


# n = int(input())
# var = n // 10**(len(str(n)) - 2)
# print(var % 10)


# n = int(input())
# tr = True
# while n != 0:
#     a = n % 100
#     b = a % 10
#     if a // 10 != b and a // 10 != 0:
#         print('NO')
#         tr = False
#         break
#     n //= 10
# if tr:
#     print('YES')


# n = int(input())
# var = n % 10
# wort = 'YES'
# while n != 0:
#     if var != n % 10:
#         wort = 'NO'
#     n //= 10
# print(wort)


# n = int(input())
# wort = 'YES'
# while n != 0:
#     a = (n % 100) // 10
#     if a < n % 10 and a != 0:
#         wort = 'NO'
#     n //= 10
# print(wort)


# n = int(input())
# for i in range(1, n + 1):
#     if 5 <= i <= 9:
#         continue
#     if 17 <= i <= 37:
#         continue
#     if 78 <= i <= 87:
#         continue
#     print(i)


# n = int(input())
# for i in range(2, n + 1):
#     if n % i == 0:
#         print(i)
#         break
