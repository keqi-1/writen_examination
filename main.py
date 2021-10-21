#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param arr float浮点型一维数组 非空无序数组
# @return float浮点型
#
import math


class Solution:
    def quicksort(self, arr, low, height, mid):
        if arr == None or low > height:
            print("return0")
            return 0
        left = low
        right = height
        # t = math.random(low,height)
        # tag = arr[t]
        t = arr[left]
        while (left < right):
            while arr[right] >= t and left < right:
                right -= 1
            arr[left] = arr[right]
            while arr[left] < t and left < right:
                left += 1
            arr[right] = arr[left]
            arr[left] = t
        if left < mid:
            self.quicksort(arr, left + 1, height, mid)
        elif right > mid:
            self.quicksort(arr, low, right - 1, mid)
        else:
            x = float(arr[mid])
            print("x", x)
            return x

    def median(self, arr):
        l = len(arr)
        tag = l % 2  # tag = 1 取中间的数 tag = 0 取两个数/2
        mid = l // 2
        low = 0
        height = l - 1
        result = 0
        if tag:
            result = self.quicksort(arr, low, height, mid)
            print(result)
            return result
        else:
            r_left = self.quicksort(arr, low, height, mid - 1)
            r_right = self.quicksort(arr, low, height, mid - 1)
            return (r_left + r_right) / 2


