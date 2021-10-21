

def link(users,case):
    pool = []
    tag = set()
    for i in case:
        a_list = set()
        b_list = set()
        tag.add(i[0])
        tag.add(i[1])
        for j in pool:
            if i[0] in j:
                a_list = j
            if i[1] in j:
                b_list = j
        if a_list!= set() and b_list!=set():
            if a_list == b_list:
                continue
            else:
                pool.remove(a_list)
                pool.remove(b_list)
                u = a_list.intersection(b_list)
                pool.append(u)
        elif a_list!=set():
            pool.remove(a_list)
            a_list.add(i[1])
            pool.append(a_list)
        elif b_list!=set():
            pool.remove(b_list)
            b_list.add(i[0])
            pool.append(b_list)
        else:
            u = {i[0],i[1]}
            pool.append(u)
    users = set(users)^tag
    res = len(pool) + len(users)
    return res

if __name__ == "__main__":
    c = int(input())
    for i in range(c):
        s = input().split()
        n = int(s[0])
        m = int(s[1])
        users = [x for x in range(n)]
        case = []
        for j in range(m):
            s = [int(x) for x in input().split()]
            case.append(s)
        res = link(users,case)
        print(res)


def largeland(island):
    def dfs(i, j):
        if not 0 <= i < rows or not 0 <= j < cols or (i, j) in visited or island[i][j] != 1:
            return 0
        else:
            res = 1
            visited.add((i, j))
            res += dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)
            print(res)
        return res

    visited = set()
    rows = len(island)
    cols = len(island[0])
    tag = set()
    for row in range(rows):
        for col in range(cols):
            if (row, col) not in visited:
                if island[row][col] == 1:
                    res = dfs(row, col)
                    tag.add(res)
    tag = list(tag)
    return max(tag)


if __name__ == "__main__":
    island = []
    while True:
        try:
            s = input()
        except:
            break
        s = s.replace("[[", "")
        s = s.replace("]]", "")
        s = s.replace("],", "")
        s = s.replace("[", "")
        s = s.replace("],", "")
        s = [int(x) for x in s.split(",")]
        island.append(s)
    res = largeland(island)
    print(res)


