# def test(k,nums):
#     res =[]
#     for i in nums:
#         if i in res:
#             res.remove(i)
#         else:
#             res.append(i)
#     r = len(res)
#     return r
#
# if __name__ == "__main__":
#     k = int(input())
#     nums = input().split()
#     print(test(k,nums))

def test(nums):
    l = len(nums)
    dp1 = [1]*l
    dp2 = [1]*l
    dp1[0] = 1
    dp2[0] = 1
    for i in range(1,l):
        print("-----",nums[i],"-----")
        for j in range(i-1,-1,-1):
            print(nums[j],nums[i]%nums[j],nums[i]//nums[j],dp2[j])
            if nums[i]%nums[j] == 0 and nums[i]//nums[j] == dp2[j]:
                dp1[i] = dp1[j]+1
                dp2[i] = dp2[j]
                break
        if dp1[i] == 1:
            dp1[i] = dp1[j]+1
            dp2[i] = nums[i]
        print(dp1,dp2)
    return(max(dp1))


if __name__ == "__main__":
    k = int(input())
    nums = [int(x) for x in input().split()]
    print(test(nums))
# test([1,3,2,5,4,2,8,6,16,9])
# 1 2 3 4 1 6 8 5 1 16 4 2 8 32