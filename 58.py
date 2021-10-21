# class Solution:
#     def rec(self, results):
#         n = len(results)
#         t = set()
#         for i in range(n):
#             for j in range(len(results[i])):
#                 t.add(results[i][j])
#         t = list(t)
#         t.sort(reverse=True)
#         return t

#
class Solution:
    def canarrive(self, matrix, i, j, used):
        n = len(matrix)
        m = len(matrix[0])
        t = []
        if i - 1 >= 0 and matrix[i - 1][j] == 1 and used[i - 1][j] == 0:
            t.append([i - 1, j])
        if j - 1 >= 0 and matrix[i][j - 1] == 1 and used[i][j - 1] == 0:
            t.append([i, j - 1])
        if j + 1 < n and matrix[i][j + 1] == 1 and used[i][j + 1] == 0:
            t.append([i, j + 1])
        if i + 1 < m and matrix[i + 1][j] == 1 and used[i + 1][j] == 0:
            t.append([i + 1, j])
        return t

    def dfs(self, matrix, start, end, used):
        i, j = start[0], start[1]
        i_, j_ = end[0], end[1]
        used[i][j] = 1
        if i == i_ and j == j_:
            return 1
        else:
            res = 0
            t = self.canarrive(matrix, i, j, used)
            if t == []:
                return 0
            for i in t:
                res += self.dfs(self, matrix, i, end, used)
        return res

    def pathAvailable(self,matrix,starts,ends):
        n = len(matrix)
        m = len(matrix[0])
        used = [[0] * m for _ in range(n)]
        l = len(starts)
        res = []
        for i in range(l):
            t = self.dfs(self, matrix, starts[i], ends[i], used)
            if t == 0:
                res.append(False)
            else:
                res.append(True)
        return res

    matrix = [ [1,1,1,1], [0,0,0,0], [1,1,1,1], [1,1,0,1] ]
    starts = [[0,0],[0,1],[2,0]]
    ends = [[0,3],[2,2],[3,3]]
    res = pathAvailable(matrix, starts, ends)
    print(res)