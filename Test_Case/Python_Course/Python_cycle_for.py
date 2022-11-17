# for i in range(10):
#     print('Python is awesome!')


# wort, var = input(), int(input())
# for i in range(var):
#     print(wort)


# for i in range(6):
#     for j in range(3):
#         print('A', end='')
#     print()
# for i in range(5):
#     for j in range(4):
#         print('B', end='')
#     print()
# print('E')
# for i in range(9):
#     for j in range(5):
#         print('T', end='')
#     print()
# print('G')


# n = int(input())
# for i in range(n):
#     for j in range(19):
#         print('*', end='')
#     print()


# n = int(input())
# for i in range(n):
#     for j in range(n - i):
#         print('*', end='')
#     print()


# n, m = int(input()), int(input())
#
# if n < m:
#     for i in range(n, m + 1):
#         print(i)
# elif m < n:
#     for i in range(n, m - 1, -1):
#         print(i)
# elif n == m:
#     print(m)


# n, m = int(input()), int(input())
# if n < m:
#     for i in range(n, m + 1):
#         if i % 2 != 0:
#             print(i)
# elif m < n:
#     for i in range(n, m -1, -1):
#         if i % 2 != 0:
#             print(i)


# n, m = int(input()), int(input())
# for i in range(n, m + 1):
#     if i % 17 == 0 or (i % 3 == 0 and i % 5 == 0) or i % 10 == 9:
#         print(i)


# n = int(input())
# for i in range(1, 11):
#     print(f'{n} x {i} = {n * i}')


# a, b = int(input()), int(input())
# num = 0
# for i in range(a, b + 1):
#     if i**3 % 10 == 4 or i**3 % 10 == 9:
#         num += 1
# print(num)


# n = int(input())
# summ = 0
# for i in range(n):
#     summ += int(input())
# print(summ)


# import math
# n = int(input())
# counter = 0
# for i in range(1, n + 1):
#     counter += 1 / i
# print(counter - math.log(n))


# n = int(input())
# counter = 0
# for i in range(1, n + 1):
#     if i**2 % 10 == 2 or i**2 % 10 == 5 or i**2 % 10 == 8:
#         counter += i
# print(counter)


# import math
# n = int(input())
# print(math.factorial(n))


# n = int(input())
# counter = 1
# for i in range(2, n + 1):
#     counter *= i
# print(counter)


# counter = 1
# for i in range(10):
#     n = int(input())
#     if n != 0:
#         counter *= n
# print(counter)


# n = int(input())
# counter = 0
# for i in range(1, n + 1):
#     if n % i == 0:
#         counter += i
# print(counter)


# n = int(input())
# counter = 0
# for i in range(1, n + 1):
#     if i % 2 == 0:
#         counter -= i
#     else:
#         counter += i
# print(counter)


# n = int(input())
# arr: list = []
# for i in range(n):
#     var = int(input())
#     arr.append(var)
# arr.sort()
# print(arr.pop())
# print(max(arr))


# fl = True
# for i in range(10):
#     n = int(input())
#     if n % 2 != 0:
#         fl = False
# if fl:
#     print('YES')
# else:
#     print('NO')


# n = int(input())
# count1 = 0
# count2 = 0
# summ = 1
# print(1)
# for i in range(n - 1):
#     count1 = count2
#     count2 = summ
#     summ = count1 + count2
#     print(summ)
