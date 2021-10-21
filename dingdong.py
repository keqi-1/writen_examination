# def min_path(matrix):
#     m = len(matrix)
#     n = len(matrix[0])
#     dp = [[0]* n for _ in range(m)]
#     dp[0][0] = matrix[0][0]
#     for i in range(n):
#         for j in range(m):
#             if i == 0 and j == 0:
#                 continue
#             if j-1>=0 and i-1 >= 0:
#                 dp[i][j] = min(dp[i-1][j],dp[i][j-1])+matrix[i][j]
#             elif i-1>=0:
#                 dp[i][j] = dp[i-1][j] + matrix[i][j]
#             elif j-1>=0:
#                 dp[i][j] = dp[i][j-1] + matrix[i][j]
#     return dp[m-1][n-1]
#
#
# if __name__ == "__main__":
#     s = input().split()
#     n,m = int(s[0]),int(s[1])
#     matrix = []
#     for i in range(n):
#         s = [int(x) for x in input().split()]
#         matrix.append(s)
#     res = min_path(matrix)
#     print(res)
#
# def feibonaqi(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         res = (feibonaqi(n-1) + feibonaqi(n-2))%(1e9+7)
#         return res
# res = feibonaqi(5)
# print(res)




