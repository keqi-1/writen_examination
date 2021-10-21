#棋盘格问题
def where(x,y,m,n):
    t = []
    if x+1 < m:
        t.append(x+1,y)
    if y+1 < m:
        t.append(x,y+1)
    return t

def getpath(m,n):
    x,y = 0,0
    res = []
    while x < m and y < n:
        t = where(x,y,m,n)
        res.append(x,y)

