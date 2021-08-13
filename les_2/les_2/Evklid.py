# алгоритм Эвклида (НОД - наибольший общий делитель)

# вариант 1
# def gcd(n,m):
#     while n!=m:
#         if m>n:
#             m -=n
#         else:
#             n -=m
#     return m
# print(gcd(54,30))

# вариант 2
# def gcd(m,n):
#     if n==0:
#         return m
#     return gcd(n, m%n)
# print(gcd(54,30))

# вариант 3
# def gcd(m,n):
#     while n!=0:
#         m,n=n,m%n
#     return m
# print(gcd(54,30))
