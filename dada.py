
def get_s1(self, s1):
    def dfs(s1, used, size, deepth, path, res):
        if size == deepth:
            res.append(list(path))
            return
        for i in range(size):
            if used[i] == 0:
                path.append(s1[i])
                used[i] = 1
                dfs(s1, used, size, deepth + 1, path, res)
                used[i] = 0
                path.pop()

    size = len(s1)
    used = [0] * size
    res = []
    dfs(s1, used, size, 0, [], res)
    return res

def function(self, str1, str2):
    t = self.get_s1(str1)
    for i in t:
        r = "".join(i)
        if r in str2:
            return True
    return False


# def function(height):
#     n = len(height)
#     leftmax,left = height[0],1
#     rightmax,right = height[n-1],n-2
#     res = 0
#     while left <= right:
#         if leftmax < rightmax:
#             if height[left] < leftmax:
#                 res += leftmax-height[left]
#             leftmax = max(leftmax,height[left])
#             left += 1
#         else:
#             if height[right] < rightmax:
#                 res += rightmax-height[right]
#             rightmax = max(rightmax,height[right])
#             right -= 1
#     return res