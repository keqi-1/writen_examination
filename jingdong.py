class Node():
    def __init__(self,i):
        self.val = i
        self.parent = []
        self.children = []
        self.state = 0


def open(i,open_nums,Nodes):
    queue = [Nodes[i]]
    while queue:
        t = queue[0]
        t.state = 1
        queue.pop(0)
        child = t.children
        for i in child:
            if Nodes[i].state == 0:
                open_nums += 1
                queue.append(Nodes[i])
            else:
                continue
    return open_nums
def close(i,open_nums,Nodes):
    queue = [Nodes[i]]
    while queue:
        t = queue[0]
        t.state = 0
        queue.pop(0)
        child = t.children
        for i in child:
            if Nodes[i].state == 1:
                open_nums += 1
                queue.append(Nodes[i])
            else:
                continue
    return open_nums

def create(children,n):
    Nodes =[]
    for i in range(n):
        t = Node(i)
        Nodes.append(t)
    print(children)
    for i in range(n):
        for j in children[i]:
            print(children[i])
            Nodes[i].children.append(j)
            Nodes[j].parent.append(i)
    return Nodes


if __name__ == "__main__":
    s = input()
    n,q = int(s.split()[0]),int(s.split()[1])
    children = []
    for i in range(n):
        s = [int(x)-1 for x in input().split()]
        children.append(s[1:])
    Node = create(children, n)
    open_nums = 0
    # for i in Node:
    #     print(i.val,i.children,i.parent,children)
    for i in range(q):
        s = [int(x) for x in input().split()]
        if s[0] == 0:
            open_nums = close(s[1]-1, open_nums,Node)
        if s[0] == 1:
            open_nums = open(s[1]-1, open_nums,Node)
        for i in Node:
            print(i.val,i.children,i.parent,i.state)







# def main():
#     n = int(input())
#     x = [0]*n
#     for i,d in enumerate(map(int,input().split())):
#         x[i] = d
#     x.sort()
#     if n == 1:
#         return x[0]
#     if n%2 == 0:
#         tem = n // 2
#     else:
#         tem = n//2 + 1
#     cou = x[n-1]-x[0]
#     right = n-1
#     left = 0
#     for i in range(1,tem):
#         if x[right]-x[i] > x[i]-x[left] and i != n-i-1:
#             cou += x[right]-x[i]
#             right = i
#         else:
#             cou += x[i] - x[left]
#             left =i
#         if x[right] - x[n-i-1] > x[n-i-1] - x[left] and i != n-i-1:
#             cou += x[right] - x[n-i-1]
#             right = n-i-1
#         else:
#             cou += x[n-i-1] - x[left]
#             left = n-i-1
#     return cou
# main()

