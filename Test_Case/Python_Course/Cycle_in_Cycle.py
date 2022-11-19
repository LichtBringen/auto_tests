# n = int(input())
#
# for i in range(n):
#     for j in range(3):
#         print(n, end=' ')
#     print()


# n = int(input())
#
# for i in range(1, n + 1):
#     for j in range(5):
#         print(i, end=' ')
#     print()


# n = int(input())
#
# for i in range(1, n + 1):
#     for j in range(1, 10):
#         print(f'{i} + {j} = {i + j}')
#     print()


# n = int(input())
#
# for i in range(1, n // 2 + 1):
#     if i <= n // 2:
#         print('*' * i)
# for i in range(n // 2 + 1, 0, -1):
#     print('*' * i)


# n = int(input())
#
# for i in range(1, n + 1):
#     for _ in range(i):
#         print(i, end='')
#     print()

# count = 0
# for n in range(1, 14):
#     for k in range(1, 13):
#         for m in range(1, 12):
#             if 28 * n + 30 * k + 31 * m == 365:
#                 count += 1
#                 print('n =', n, 'k =', k, 'm =', m)
# print(count)


# b, k, t, al = 10, 5, 0.5, 100
# count = 0
# for i in range(1, al // b + 1):
#     for j in range(1, al // k + 1):
#         for z in range(1, int(al // t + 1)):
#             if 10 * i + 5 * j + 0.5 * z == 100 and i + j + z == 100:
#                 count += 1
#                 print(i, j, z)


# for a in range(1, 151):
#     for b in range(1, 151):
#         for c in range(1, 151):
#             for d in range(1, 151):
#                 for e in range(1, 151):
#                     if a**5 + b**5 + c**5 + d**5 == e**5:
#                         print(a, b, c, d, e, a + b + c + d + e)


# n = int(input())
# count = 1
# for i in range(1, n + 1):
#     for j in range(i):
#         print(count, end=' ')
#         count += 1
#     print()


# n = int(input())
#
# for i in range(1, n + 1):
#     print(i, end='')
#     for j in range(1, i + 1):
#         if i % j == 0:
#             print('+', end='')
#     print()


# n = int(input())
# digit = 0
#
# while n != 0:
#     digit += n % 10
#     n //= 10
#
#     if digit > 9 and n == 0:
#         n, digit = digit, n
#
# print(digit)


# n = int(input())
# result = 0
# for i in range(1, n + 1):
#     temp = 1
#     for j in range(1, i + 1):
#         temp *= j
#     result += temp
# print(result)


# a, b = int(input()), int(input())
#
# for i in range(a, b + 1):
#     temp = 0
#     for j in range(1, i + 1):
#         if i % j == 0:
#             temp += 1
#     if temp == 2:
#         print(i)


# m, p, n = int(input()), int(input()), int(input())
# print(1, m)
# for i in range(2, n + 1):
#     m += float(m * p / 100)
#     print(i, m)


# p = [x ** 5 for x in range(151)]
# pw = set(p)
# for a in range(1, 151):
#     for b in range(a, 151):
#         for c in range(b, 151):
#             for d in range(c, 151):
#                 s = p[a] + p[b] + p[c] + p[d]
#                 if s in pw:
#                     print(a, b, c, d, p.index(s))
#                     print(a + b + c + d + p.index(s))


# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end=' ')
#         if j == i:
#             for k in range(i - 1, 0, -1):
#                 print(k, end=' ')
#     print()


# a, b = int(input()), int(input())
# score = 0
# count = 0
# for i in range(a, b + 1):
#     temp = 0
#     for j in range(1, i + 1):
#         if i % j == 0:
#             temp += j
#     if score <= temp:
#         score = temp
#         count = i
# print(count, score)



