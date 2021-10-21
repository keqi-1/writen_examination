def f(a,b,xs):
    n = len(xs)
    res_y = 0
    res_y2 = 0
    for x in xs:
        res_y += a*(x**3+b)*x
        res_y2 += a*(x**6+b)*(x**2)
    ex = (1/n) * res_y
    print(res_y)
    ex2 = (1/n) * res_y2
    dx = ex2-ex**2
    return ex,dx
if __name__ == "__main__":
    s = [float(x) for x in input().split()]
    a,b = s[0],s[1]
    n = int(input())
    xs = []
    while len(xs) < n:
        s = [float(x) for x in input().split()]
        xs += s
    ex,dx = f(a,b,xs)
    print(ex,dx)