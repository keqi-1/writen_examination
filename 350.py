def test(nums):
    tag = 0
    count = 0
    n = len(nums)
    dp = [0] * n
    for i in range(n):
        if nums[i] > nums[i-1]:
            if tag == 1 or tag == 0:
                dp[i] = dp[i-1] + 1
                tag = 1
            elif count == 0:
                tag = 1
                count += 1
                dp[i] = dp[i-1] + 1
            else:
                tag = 1
                count = 0
                dp[i] = 1
        elif nums[i] < nums[i-1]:
            if tag == -1 or tag == 0:
                dp[i] = dp[i-1] + 1
                tag = -1
            elif count == 0:
                tag = -1
                count += 1
                dp[i] = dp[i-1] + 1
            else:
                tag = -1
                count = 0
                dp[i] = 1
        else:
            dp[i] = 1
            count = 0
            tag = 0
    return max(dp)



def yeah(nums):
    x = nums.index(min(nums))
    low = 1
    height = len(nums)-2
    count = 0
    if height < 2:
        return 0
    while low < x:
        while nums[low] >= nums[low-1]:
            nums[low] -= 1
            count += 1
        print(nums)
        low += 1
    while height > x:
        while nums[height] >= nums[height+1]:
            nums[height] -= 1
            count += 1
        print(nums)
        height -= 1
    return count

if __name__ == "__main__":
    s = input()
    nums = [int(x) for x in input().split()]
    res = yeah(nums)
    print(res)