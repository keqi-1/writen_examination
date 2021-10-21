
def change_num(nums):
    t = list(nums)
    t.sort()
    count = 0
    i = 0
    while nums != t :
        if nums[i] == t[i]:
            i += 1
            continue
        else:
            index = nums[i:].index(t[i])+i
            print(index,t[i],nums,t)
            nums[i],nums[index] = nums[index],nums[i]
            count += 1
            i += 1
    print(count)
    return count

nums = [2,5,3,1]
change_num(nums)

import math
#
# def walk(nums,A,n,m):
#     x_ = 0
#     y_ = 0
#     for i in range(len(nums)):
#         for j in range(len(nums[0])):
#             if nums[i][j] == "R":
#                 x_ = i
#                 y_ = j
#     x = x_
#     y = y_
#     tag = [1,1,-1,-1]
#     y_tag = 0
#     x_tag = -1
#     y_ri = 1
#     x_ri = 0
#     y_li = 1
#     x_li = 2
#     for i in range(len(A)):
#         if A[i] == "Turn right":
#             x_tag += tag[x_ri]
#             y_tag += tag[y_ri]
#             x_ri = (x_ri+1)%4
#             y_ri = (y_ri+1)%4
#         elif A[i] == 'Turn left':
#             x_tag += tag[x_li]
#             y_tag += tag[y_li]
#             print(tag[x_li],tag[y_li])
#             x_li = (x_li+1)%4
#             y_li = (y_li+1)%4
#         else:
#             for j in range(A[i]):
#                 x_t = x + x_tag
#                 y_t = y + y_tag
#                 if x_t >= n or y + y_t >= m:
#                     continue
#                 elif nums[x_t][y_t] != 'O':
#                     x = x_t
#                     y = y_t
#                 else:
#                     continue
#         print(A[i],x,y,x_tag,y_tag)
#     print(x_,y_,x,y)
#     return x-x_ ,y-y_
#
# if __name__ == "__main__":
#     s = input().split()
#     n = int(s[0])
#     m = int(s[1])
#     nums = []
#     for i in range(n):
#         s = input()
#         t = []
#         for j in range(m):
#             t.append(s[j])
#         nums.append(t)
#     l = int(input())
#     A = []
#     while l-1:
#         s = input()
#         if 'Forward' in s:
#             s = int(s.split()[1])
#             A.append(s)
#             l -= 1
#         else:
#             A.append(s)
#             l -= 1
#     print(nums, A,n,m)
#     x,y = walk(nums, A,n,m)
#     print(x,y)