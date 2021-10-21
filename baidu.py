def test(bag_size, bag_nums, weight, value):
    rows, cols = len(weight) + 1, bag_size + 1
    dp = [[0 for _ in range(cols)] for _ in range(rows)]
    res = 0
    for i in range(rows):
        dp[i][0] = 0
    item_weight, item_value = weight[0], value[0]
    for j in range(1, cols):
        if item_weight <= bag_nums:
            dp[0][j] = item_value
    for i in range(1, len(weight)):
        cur_weight, cur_val = weight[i], value[i]
        for j in range(1, cols):
            if cur_weight >= bag_nums:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] + cur_val
                if dp[i][j] > res:
                    res = dp[i][j]
    return res


if __name__ == "__main__":
    s = input()
    s = s.split()
    n = int(s[0])
    w = int(s[1])
    weight = []
    power = []
    for _ in range(n):
        s = input()
        s = s.split()
        weight.append(int(s[0]))
        power.append(int(s[1]))
    t = test(n, w, weight, power)
    print(t)



# def main():
#     a, b, x, y = map(int, input().split())
#     if x == 0: return a // y + b // y
#     if y == 0: return a // x + b // x
#     a_x, b_y = a // x, b // y
#     a_y, b_x = a // y, b // x
#     fir, sec = min(a_x, b_y), min(a_y, b_x)
#     fir = fir + min((a - fir * x) // y, (b - fir * y) // x)
#     sec = sec + min((a - sec * y) // x, (b - sec * x) // y)
#     print((a+b)//(x+y))
#     return max(fir, sec)

# print(main())