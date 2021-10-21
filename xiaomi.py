def next(matrix,node,row,col):
    x = node[0]
    y = node[1]
    res =[]
    if 0<=x+1 and x+1<col and matrix[x+1][y] == 0 :
        t = [x+1,y]
        res.append(t)
    if 0<=x-1 and x-1<col and matrix[x-1][y] == 0 :
        t = [x-1,y]
        res.append(t)
    if 0<=y+1 and y+1<row and matrix[x][y+1] == 0 :
        t = [x,y+1]
        res.append(t)
    if 0<=y-1 and y-1<col and matrix[x][y-1] == 0 :
        t = [x,y-1]
        res.append(t)
    return res


def main(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    queue = []
    queue.append([0,0])
    while queue:
        l = len(queue)
        for _ in range(l):
            count+=1
            t = queue.pop()
            next_node = next(matrix, t, rows, cols)
            for i in next_node:
                queue.append(i)
                if i == [rows-1,cols-1]:
                    return count
    return -1


s = input()
t = [int(x) for x in s.split()]
matrix = [t]
n = len(t)
for _ in range(n - 1):
    s = input()
    t = [int(x) for x in s.split()]
    matrix.append(t)
res = main(matrix)
print(res)

