def find(nums,t):
    low = 0
    height = len(nums)-1
    while low <= height:
        mid = (low+height)//2
        if nums[mid] > t:
            height = mid-1
        elif nums[mid] < t:
            low = mid+1
        else:
            return mid
    return -1

def get_index(nums,target):
    nums.sort()
    n = len(nums)
    for i in range(n):
        if nums[i] > target:
            break
        else:
            t = target-nums[i]
            index = find(nums[i:],t)
            if index != -1:
                return i,index+i
    return -1



nums = [2,2,11,15]
target = 4
print(get_index(nums,target))