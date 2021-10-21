# def test(nums):
#     res = []
#     for i in nums:
#         tag = 0
#         for j in range(len(res)):
#             if i[0] in res[j] or i[1] in res[j]:
#                 if tag == 0:
#                     id1 = j
#                     tag = 1
#                 elif tag == 1:
#                     id2 = j
#                     tag = 2
#                     break
#         if tag == 0:
#             t = set()
#             t.add(i[0])
#             t.add(i[1])
#             res.append(t)
#         elif tag == 1:
#             t = res[id1]
#             res.pop(id1)
#             t.add(i[0])
#             t.add(i[1])
#             res.append(t)
#         elif tag == 2:
#             t = res[id1].union(res[id2])
#             res.pop(id1)
#             res.pop(id2-1)
#             res.append(t)
#     return res
#
# if __name__ == "__main__":
#     s = [int(i) for i in input().split()]
#     n,m = s[0],s[1]
#     if n < 1:
#         print(0)
#     nums = []
#     for i in range(m):
#         s = [int(i) for i in input().split()]
#         nums.append(s)
#     res = test(nums)
#     tag = 0
#     for i in res:
#         if 1 in i:
#             print(len(i))
#             tag = 1
#     if tag == 0:
#         print(1)







