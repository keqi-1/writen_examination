import sys


# n = int(input())
# str = input()
# if n < 2:
#     print(0)
# count = 0
# a_num = 0
# for i in range(n):
#     if "a" not in str[0:i] and "c" not in str[i:]:
#         break
#     if str[i] == "a":
#         a_num += 1
#     if str[i] == "c":
#         count += a_num
# print(count)

def get_input():
    s = input()
    nums = s.split()
    n = int(nums[0])
    m = int(nums[1])
    lines = []
    line_set = set()
    for i in range(n):
        line = input()
        line = line.split()
        t = set()
        for j in range(int(line[0])):
            t.add(line[j+1])
            line_set.add((line[j+1]))
        lines.append((t))
    return lines,line_set,n,m

def one(matrix,lines,n,):
    for i in range(n):
        for j in range(i+1,n):
            t = lines[i].intersection(lines[j])
            if t:
                matrix[i][j],matrix[j][i] = 1,1
    return matrix

def main():
    lines,line_set,n,m = get_input()
    matrix = [[0]*n for i in range(n)]
    one(matrix,lines,n)
    return matrix
m = main()
for i in range(len(m)):
    s = [str(x) for x in m[i]]
    s_new = " ".join(s)
    print(s_new)






# str = input()
# for line in sys.stdin:
#     line = line.strip()
#     res = line.split(",")
#     res_new = [int(x) for x in res]
#     t = " ".join(res_new)

#
# def check(s):
#     n = len(s)
#     if n <= 2:
#         return True
#     p1 = s[0]
#     p2 = s[1]
#     for i in range(2,n):
#         if p1!=p2 and p1 == s[i]:
#             return False
#         p1 = p2
#         p2 = s[i]
#     return True
#
# def pre(n):
#     res = []
#     for i in range(n+1):
#         s = ""
#         a = i
#         b = n-i
#         while a:
#             s+="a"
#             a -= 1
#         while b:
#             s+="b"
#             b-=1
#         res.append(s)
#     return  res
# def test(s):
#     def dfs(c,id):
#         if id == n-1:
#             res.append("".join(c))
#         else:
#             for j in range(id,n):
#                 if j == id or c[j]!=c[id]:
#                     t = c[:]
#                     t[id],t[j] = t[j],t[id]
#                     dfs(t,id+1)
#     n = len(s)
#     if n == 1:
#         lis = [s]
#     else:
#         res = []
#         c = list(s)
#         dfs(c,0)
#         lis = list(set(res))
#     return lis
#
# def main():
#     n = int(input())
#     count = 0
#     l = pre(n)
#     for i in l:
#         s = test(i)
#         t = len(s)
#         for j in s:
#             if not check(j):
#                 t -= 1
#         count += t
#     t = count%998244353
#     print(t)
# main()