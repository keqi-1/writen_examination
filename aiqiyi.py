#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re


class Solution:
    def findNSum(self, N):
        # Write Code Here
        i = 1
        j = 1
        sum = 0
        res = []
        while i <= N // 2:
            if sum < N:
                sum += j
                j += 1
            elif sum > N:
                sum -= i
                i += 1
            else:
                arr = list(range(i, j))
                res.append(arr)
                sum -= i
                i += 1
        return (res)


_N = int(input())

s = Solution()
res = s.findNSum(_N)

for res_x in res:
    for res_y in res_x:
        print(str(res_y) + " ")
    print("\n")


#################################
# !/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re


class Solution:
    def calcSumOfOnlyOne(self, arr):
        # Write Code Here
        t = []
        for i in arr:
            if i in t:
                t.remove(i)
            else:
                t.append(i)
        res = t[0] + t[1]
        return res


_arr_cnt = 0
_arr_cnt = int(input())
_arr = list(map(int, input().split()))

s = Solution()
res = s.calcSumOfOnlyOne(_arr)

print(str(res) + "\n")