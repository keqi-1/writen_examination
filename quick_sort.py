import sys
def test(nums,begin,end):
    low = begin
    height = end
    tag = nums[low]
    while low < height:
        while low < height and nums[height] > tag:
            height -= 1
        nums[low] = nums[height]
        while low < height and nums[low] < tag:
            low += 1
        nums[height] = nums[low]
        nums[low] = tag
    if low > begin:
        test(nums,begin,low-1)
    if low < end:
        test(nums,low+1,end)
    return nums


def quick_sort(nums):
    begin = 0
    end = len(nums)-1
    nums = test(nums,begin,end)
    return nums

nums = [2,4,6,3,5,7]
res = quick_sort(nums)
print(res)
print('Hello,World!');