# def next(matrix,node,row,col):
#     x = node[0]
#     y = node[1]
#     res =[]
#     if 0<=x+1 and x+1<col and matrix[x+1][y] == 0 :
#         t = [x+1,y]
#         res.append(t)
#     if 0<=x-1 and x-1<col and matrix[x-1][y] == 0 :
#         t = [x-1,y]
#         res.append(t)
#     if 0<=y+1 and y+1<row and matrix[x][y+1] == 0 :
#         t = [x,y+1]
#         res.append(t)
#     if 0<=y-1 and y-1<col and matrix[x][y-1] == 0 :
#         t = [x,y-1]
#         res.append(t)
#     return res
#
#
# def main(matrix):
#     rows = len(matrix)
#     cols = len(matrix[0])
#     count = 0
#     queue = []
#     queue.append([0,0])
#     while queue:
#         l = len(queue)
#         for _ in range(l):
#             count+=1
#             t = queue.pop()
#             next_node = next(matrix, t, rows, cols)
#             for i in next_node:
#                 queue.append(i)
#                 if i == [rows-1,cols-1]:
#                     return count
#     return -1
#
# s = input()
# t = [int(x) for x in s.split()]
# matrix = [t]
# n = len(t)
# for _ in range(n-1):
#     t = [int(x) for x in input().split()]
#     matrix.append(t)
# res = main(matrix)
# print(res)

def test(nums,max_n,n):
    dp = [[0]*(max_n+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,max_n+1):
            dp[i][j] = dp[i-1][j]
            if j>=1:
                dp[i][j] = max(dp[i][j],dp[i-1][j-1]|nums[i-1])
    print(dp[-1][-1])

if __name__ == "__main__":
    n = int(input())
    nums = [int(x) for x in input().split()]
    if n == 0:
        print(-1)
    if n == 1:
        print(nums[0])
    if n <= 30:
        test(nums,n,n)
    else:
        test(nums,30,n)


