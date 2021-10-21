def test(nums):
    n = len(nums)
    dp = [0]*n
    dp[0] = 1
    for i in range(n):
        for j in range(i,-1,-1):
            if nums[j] > nums[i]:
                dp[i] = dp[j] + 1
                break
    print(max(dp))

if __name__ == "__main__":
    s = input()
    l = [int(x) for x in input().split()]
    test(l)