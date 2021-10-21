import math
def where(x,y):
    t = int(math.log(max(x,y),2)+1)
    t = 2**(t)//2
    if x <2 and y<2:
        return 0
    if x < t and y<t:
        return "a"
    elif x < t and y >= t:
        return "b"
    elif x >= t and y < t:
        return "d"
    elif x >= t and y >= t:
        return "c"

def repooling(nums,x,y):
    # n = len(nums)
    res =0
    while x >= 2 or y >= 2:
        print(x,y)
        t = int(math.log(max(x,y),2)+1)
        t = 2**(t)//2
        w = where(x,y)
        if w == "a":
            return res
        elif w == "b":
            res += nums[0][1]
            y -= t
        elif w == "d":
            res += nums[1][0]
            x -= t
        elif w == "c":
            res += nums[1][1]
            x -= t
            y -= t
        else:
            print(w, res, x, y,t)
            break
        print(w,res,x,y,t)
    res += nums[x][y]
    return res

nums = [[1,2],[4,3]]

res = repooling(nums, 5-1,7-1)
print(res)
##################################
##################################
##################################


# def main():
#     x = int(input())
#     arr = [[0,0] for i in range(x)]
#     for i,d in enumerate(arr):
#         arr[i][0],arr[i][1] = map(int,input().split)
#     for d,i in enumerate(arr):
#         k = 1
#         cou = 1
#         while (i[0]<i[1]):
#             i[0]+=k
#             k+=1
#             if(i[0]<i[1]):
#                 cou += 1
#         if (i[0]-i[1])%2 != 0:
#             cou += 1
#     print(cou)
# main()