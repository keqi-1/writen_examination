# def Pow(x,n): #x^n
#     if n < 0: x,n = 1/x,-n
#     elif n == 0 or x ==1 :
#         return 1
#     if n%2 == 0:
#         x = Pow(x*x,n//2)
#     else:
#         x = x*Pow(x*x,(n-1)//2)
#     return x
#
# def find(nums,m):
#     l = len(nums)
#     for i in range(l):
#         for j in range(l):
#             if i == j:continue
#             else:
#                 t = Pow(nums[i],nums[j])
#                 if t == m:
#                     return nums[i],nums[j]
#     return -1,-1
# def main():
#     nums = [2,3,4]
#     m = [4,9,16]
#     for i in range(len(m)):
#         x,y = find(nums,m[i])
#         print(x,y)
# if __name__ == '__main__':
#     s1 = input()
#     s2 = input()
#     s3 = input()
#     nm = [int(x) for x in s1.split()]
#     n = nm[0]
#     m = nm[1]
#     weight = [int(x) for x in s2.split()]
#     ms = [int(x) for x in s3.split()]
#     for i in range(m):
#         x,y = find(weight,m[i])
#         print(x,y)
#
#
# a = [[1],[2],[3]]
# print(a.index(2))
#
# def posible(x,y):
#     t1 = [x+1,y+2]
#     t2 = [x+1,y-2]
#     t3 = [x-1,y+2]
#     t4 = [x-1,y-2]
#
#     t5 = [x+2,y+1]
#     t6 = [x+2,y-1]
#     t7 = [x-2,y+1]
#     t8 = [x-2,y-1]
#     res = [t1,t2,t3,t4,t5,t6,t7,t8]
#     return res
#
# def canarrive(matrix,x,y,n,m,used):
#     res =[]
#     index = posible(x,y)
#     for xy in index:
#         x_ = xy[0]
#         y_ = xy[1]
#         if 0 <= x_ < n and 0 <= y_ < m:
#             if matrix[x][y]!=matrix[x_][y_] and used[x_][y_] == 0:
#                 res.append([x_,y_])
#     return res
#
# def main(n,m,x,y,matrix):
#     def begin(matrix,x,y):
#         next = canarrive(matrix,x,y,n,m,used)
#         l = len(next)
#         if l == 0:
#             return
#         for xy in next:
#             x_ = xy[0]
#             y_ = xy[1]
#             if used[x_][y_] == 0:
#                 used[x_][y_] = 1
#                 begin(matrix,x_,y_)
#
#     used = [[0]*n for _ in range(m)]
#     used[x][y] = 1
#     begin(matrix, x, y)
#     return used
#
# if __name__ == '__main__':
#     m = 3
#     n = 3
#     x = 1
#     y = 2
#     s = sys.stdin.readline()
#     nm = [int(x) for x in s.strip()]
#     n = nm[0]
#     m = nm[1]
#     matrix = []
#     for i in range(n):
#         line = sys.stdin.readline().strip()
#         matrix.append(line)
#     s = sys.stdin.readline()
#     xy = [int(x) for x in s.strip()]
#     x = xy[0]
#     y = xy[1]
#     matrix = [["b", "b", "b"], ["b", "b", "b"], ["r", "b", "r"]]
#     used = main(n,m,x-1,y-1,matrix)
#     count = 0
#     for i in used:
#         count += sum(i)
#     print(count)


def acc(predict,label):
    p_dic = {}
    for i in range(len(predict)):
        if predict[i] in p_dic.keys():
            p_dic[predict[i]].append(i)
        else:
            p_dic[predict[i]] = [i]
    l_dic = {}
    for i in range(len(label)):
        if label[i] in l_dic.keys():
            l_dic[label[i]].append(i)
        else:
            l_dic[label[i]] = [i]
    l = []
    for key in l_dic.keys():
        t = l_dic[key]
        for i in range(len(t)-1):
            for j in range(i+1,len(t)):
                l.append([t[i],t[j]])
    p = []
    for key in p_dic.keys():
        t = p_dic[key]
        for i in range(len(t)-1):
            for j in range(i+1,len(t)):
                p.append([t[i],t[j]])
    w = 0
    count = 0
    for i in range(len(predict)):
        for j in range(i+1,len(predict)):
            if ([i,j] in p and [i,j] in l) or ([i,j] not in p and [i,j] not in l):
                w += 1
            count += 1
    res = w/count
    return res


if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        t = input()
        predict = [int(x) for x in input().split()]
        label = [int(x) for x in input().split()]
        res = acc(predict,label)
        if res > 0.5:
            print(1)
        else:
            print(0)



def cooki(nums,n,k):
    min_ = min(nums)
    index = nums.index(min_)
    low = index-k+1
    if low<0:
        low = 0
    height = index + k -1
    if height >= n:
        height = n-1
    i = low
    j = low+k
    tag1_i = i
    tag1_j = j
    res1_ = sum(nums[i:j])
    while j <= height:
        t = sum(nums[i:j])
        if t > res1_:
            tag1_j = j
            tag1_i = i
            res1_ = t
        i+=1
        j+=1
    nums1 = nums[:tag1_i] + nums[tag1_j:]
    t = res1_/k
    nums1.append(t)



    max_ = max(nums)
    index = nums.index(max_)
    low = index-k+1
    if low<0:
        low = 0
    height = index + k -1
    if height >= n:
        height = n-1
    i = low
    j = low+k
    tag2_i = i
    tag2_j = j
    res2_ = sum(nums[i:j])
    while j <= height:
        t = sum(nums[i:j])
        if t < res2_:
            tag2_j = j
            tag2_i = i
            res2_ = t
        i+=1
        j+=1
    nums2 = nums[:tag2_i] + nums[tag2_j:]
    t = res2_/k
    nums2.append(t)

    res1 = max(nums1)-min(nums1)
    res2 = max(nums2)-min(nums2)
    res = min(res1,res2)
    if res == int(res):
        return int(res)
    else:
        return res

if __name__ == "__main__":
    s = input().split()
    n,k = int(s[0]),int(s[1])
    nums = [int(x) for x in input().split()]
    print(cooki(nums,n,k))







