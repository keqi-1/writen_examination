def max_sub(s):
    stack = []
    max_len = 0
    for i in range(len(s)):
        if s[i] not in stack:
            stack.append(s[i])
        else:
            while s[i] in stack:
                stack.pop(-1)
        max_len = max(max_len,len(stack))
    return max_len


def queue_sort(nums):
    zero = []
    one = []
    two = []
    for i in nums:
        if i == "0":
            zero.append(0)
        elif i == "1":
            one.append(1)
        elif i == "2":
            two.append(2)
    res = zero + one + two
    print(res,zero ,one ,two)
    return res


def water(n):
    nums = [100,50,20,10,5,1]
    count= 0
    while n>0:
        for i in range(6):
            if n >= nums[i]:
                n -= nums[i]
                count+=1
                break
            else:
                continue
    return count
