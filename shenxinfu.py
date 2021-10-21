def max_sub_matrix(matrix):
    n = len(matrix)
    m = len(matrix[0])
    dp = [[0]*m for _ in range(n)]
    dp[0][0] = matrix[0][0]
    begin_tag = [[(0,0)]*m for _ in range(n)]
    t = (0,0)
    for i in range(1,m):
        if dp[0][i-1]+matrix[0][i] > matrix[0][i]:
            dp[0][i] = dp[0][i-1]+matrix[0][i]
            begin_tag[0][i] = t
        else:
            dp[0][i] = matrix[0][i]
            begin_tag[0][i] = (0,i)
            t = (0,i)
    t = (0,0)
    for j in range(1,n):
        if dp[i-1][0]+matrix[j][0]>matrix[j][0]:
            dp[j][0] = dp[j-1][0]+matrix[j][0]
            begin_tag[j][0] = t
        else:
            dp[j][0] = matrix[j][0]
            begin_tag[i][0] = (j,0)
            t = (j,0)
    for i in range(1,n):
        t = (i-1,0)
        for j in range(1,m):
            if dp[i-1][j-1]+sum(matrix[i][:j])+sum(matrix[:i][j])+matrix[i][j]>matrix[i][j]:
                dp[i][j] = dp[i-1][j-1]+sum(matrix[i][:j])+sum(matrix[:i][j])+matrix[i][j]
                begin_tag[i][j] = t
            else:
                dp[i][j] = matrix[i][j]
                begin_tag[i][j] = (i,j)
                t = (i,j)
    print(dp)
    print(begin_tag)
    return 0
max_sub_matrix([[1,1,1], [-1,-1,-1], [-1,-1,-1]])



