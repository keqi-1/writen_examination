
# def test(nums):
#     t = []
#     for i in nums:
#         if (i//5+1) * 5 - i <3 and i >= 38:
#             t.append((i//5+1) * 5)
#         else:
#             t.append(i)
#     print(t)
#
# if __name__ == "__main__":
#     n = int(input())
#     res = []
#     for i in range(n):
#         s = int(input())
#         res.append(s)
#     test(res)

# def test(nums,k):
#     nums.sort()
#     count = 0
#     while nums[0] < k:
#         if len(nums) < 2:
#             nums.append(nums[0])
#         t = nums[0] + 2*nums[1]
#         print(nums,t)
#         nums = nums[2:]
#         tag = 0
#         for i in range(len(nums)):
#             if nums[i] >= t:
#                 nums.insert(i,t)
#                 tag = 1
#                 break
#         if tag == 0:
#             nums.append(t)
#         count += 1
#
#     return count
#
#


def test(N,A):
    nums = [0]*N
    for i in A:
        low = i[0]
        height = i[1]
        t = i[2]
        for j in range(low,height):
            nums[j] += t
    return max(nums)
if __name__ == "__main__":
    s = [int(x) for x in input().split()]
    N,M = s[0],s[1]
    A = []
    for i in range(M):
        s = [int(x) for x in input().split()]
        A.append(s)

    res = test(N,A)
    print(res)




