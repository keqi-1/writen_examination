def test(nums):
    nums.sort()
    max_num = nums[-1]
    t = []
    for i in nums:
        l = len(t)
        if i < 0 and -(i*(l+1))<max_num or i >=0:
            t.append(i)
        else:
            continue
    n = len(t)
    res = 0
    for i in range(n):
        res += (i+1)*t[i]
    return res

# !/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re


class Solution:

    def third_sum(self,nums):
        n = len(nums)
        third = []
        for i in range(n - 2):
            if i + 2 >= n:
                break
            tag = 0
            for j in range(i + 1, n - 1):
                if j + 1 >= n:
                    break
                for k in range(j + 1, n):
                    t = nums[i] + nums[j] + nums[k]
                    if t - 3 * (t // 3) == 0:
                        third.append(nums[i])
                        third.append(nums[j])
                        third.append(nums[k])
                        f1, f2, f3 = nums[i], nums[j], nums[k]
                        nums.remove(f1)
                        nums.remove(f2)
                        nums.remove(f3)
                        n -= 3
                        tag = 1
                        break
                if tag == 1:
                    break
        return third, nums

    def second_sum(self,nums):
        n = len(nums)
        second = []
        for i in range(n - 1):
            tag = 0
            if i + 1 >= n:
                break
            for j in range(n):
                if j >= n:
                    break
                t = nums[i] + nums[j]
                if t - 3 * (t // 3) == 0:
                    second.append(nums[i])
                    second.append(nums[j])
                    f1, f2 = nums[i], nums[j]
                    nums.remove(f1)
                    nums.remove(f2)
                    n -= 2
                    tag = 1
                    break
            if tag == 1:
                break
        return second

    def solution(self, d):
        nums = d
        nums.sort(reverse=True)
        t = []
        res = []
        for i in nums:
            if i - 3 * (i // 3) == 0:
                res.append(i)
            else:
                t.append(i)
        third = []
        second =[]
        if t != []:
            third, t = self.third_sum(t)
            if t!=[]:
                second = self.second_sum(t)
        res = res + third
        res = res + second
        res.sort(reverse=True)
        res = [str(x) for x in res]
        s = "".join(res)
        s = int(s)
        print(s)


_d_cnt = 0
_d_cnt = int(input())
_d_i = 0
_d = []
while _d_i < _d_cnt:
    _d_item = int(input())
    _d.append(_d_item)
    _d_i += 1

s = Solution()
res = s.solution(_d)

print(res + "\n")